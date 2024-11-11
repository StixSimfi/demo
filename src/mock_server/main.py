"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
import logging
from typing import Dict

from aiohttp import web
# import aiohttp_cors
from configargparse import Namespace
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from aiomisc.log import LogFormat, basic_config


from commons.logger import Log
from handlers import HANDLERS
from utils.argpars import positive_int

# По умолчанию размер запроса к aiohttp ограничен 1 мегабайтом:
# Модифицируйте размер под свои нужды
# Параметры забиты гвоздями, но можно вынести их в ENV или БД
MEGABYTE = 1024 ** 2
MAX_REQUEST_SIZE = 3 * MEGABYTE


def load_data() -> Dict:
    answers = {}
    with open("data/ps.dat", "r") as data:
        answers["ps"] = data.read()
    return answers


DOCKER = load_data()


parser = ArgumentParser(
    allow_abbrev=False,
    formatter_class=ArgumentDefaultsHelpFormatter
)

# Передачу аргументов настройте в poetry.test.Dockerfile или в профиле запуска IDE
group = parser.add_argument_group('API Options')
group.add_argument('--api-address', default='0.0.0.0',
                   help='IPv4/IPv6 address API server would listen on')
group.add_argument('--api-port', type=positive_int, default=8089,
                   help='TCP port API server would listen on')

group = parser.add_argument_group('Logging options')
group.add_argument('--log-level', default='info',
                   choices=('debug', 'info', 'warning', 'error', 'fatal'))
group.add_argument('--log-format', choices=LogFormat.choices(),
                   default='color')


def create_app(args: Namespace, log: logging) -> web.Application:
    """
        Создает экземпляр приложения, готового к запуску.
        Добавьте мидлвары при необходимости и опишите их в отдельном модуле
        Например: обработчики ошибок middlewares=[error_middleware, validation_middleware]
    """
    app = web.Application(
        client_max_size=MAX_REQUEST_SIZE
    )
    app.__setattr__("answer", DOCKER)
    app.__setattr__("logger", log)

    # Регистрация обработчиков
    for handler in HANDLERS:
        log.debug('Registering handler %r as %r', handler, handler.URL_PATH)
        app.router.add_route("*", handler.URL_PATH, handler.get)

    return app


def main() -> None:
    # Получаем параметры конфигурации, которые можно передать как аргументами
    # командной строки, так и переменными окружения
    args = parser.parse_args()

    log = Log(
        file_handler_level=logging.getLevelName(args.log_level.upper()),
        stream_handler_level=logging.getLevelName(args.log_level.upper())).get_logger()

    # Чтобы логи не блокировали основной поток (и event loop) во время операций
    # записи в stderr или файл - логи можно буфферизовать и обрабатывать в
    # отдельном потоке (aiomisc.basic_config настроит буфферизацию
    # автоматически).
    basic_config(args.log_level, args.log_format, buffered=True)

    # Запускаем приложение на указанном порту и адресе
    app = create_app(args, log)

    # При необходимости подкрутите КОРСЫ
    """
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*"
            )
        })

        for route in list(app.router.routes()):
            cors.add(route)
    """

    web.run_app(app, host=args.api_address, port=args.api_port)


if __name__ == "__main__":
    main()
