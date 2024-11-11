"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""

import requests
from .logger import Log
from .interfaces import IClient


class Client(IClient):
    """
        Класс клиент, предназначен для организации подключений к серверам данных.
    """

    def __init__(self,
                 remote_server_address: str,
                 logger: Log
                 ):
        """
        Конструктор класса клиента, реализован на базе библиотеки requests
        :param remote_server_address: Адрес удаленного сервера
        :param logger: Объект логера
        """
        super().__init__(
            remote_server_address=remote_server_address,
            logger=logger
        )
        self._URL = remote_server_address
        self._logger = logger
        self.__session = self.__make_session()

    @staticmethod
    def __make_session() -> requests.Session:
        return requests.Session()

    def __str__(self) -> str:
        return f"Клиент создан. Адрес удаленного подключения: {self._URL}.\n"

    def post(self, route: str, json=None, data=None) -> requests.Response:
        """
        Реализация метода отправки POST запроса.
        :param route: URI сервера.
        :param json: JSON объект с данными.
        :param data: Прочие данные, например текст или массив байт.
        :return: requests.Response
        """
        response = self.__session.post(
            self._URL + route,
            data=data,
            headers={"Content-Type": "application/soap+xml"}
        ) if data is not None else self.__session.post(self._URL + route, json=json)
        # пишет текстовое представление response, при необходимости можно расширить и писать JSON объекты.
        self._logger.debug(response.text)  # noqa
        return response

    def get(self, route: str) -> requests.Response:
        """
        Реализация метода отправки GET запроса.
        :param route: URI сервера.
        :return: requests.Response
        """
        response = requests.get(self._URL + route)
        self._logger.debug(response.text)  # noqa
        return response

    def put(self, route: str, data) -> requests.Response:
        """
        Реализация метода отправки PUT запроса.
        :param route: URI сервера.
        :param data:
        :return: requests.Response
        """
        response = requests.put(self._URL + route, json=data)
        self._logger.debug(response.text)  # noqa
        return response

    def delete(self, route: str) -> requests.Response:
        """
        Реализация метода отправки DELETE запроса.
        :param route: URI сервера.
        :return: requests.Response
        """
        response = requests.delete(
            url=self._URL + route
        )
        self._logger.debug(response.text)  # noqa
        return response

    def patch(self, route: str, data) -> requests.Response:
        """
        Реализация метода отправки PUTCH запроса.
        :param route: URI сервера.
        :param data:
        :return: requests.Response
        """
        response = requests.patch(self._URL + route, json=data)
        self._logger.debug(response.text)  # noqa
        return response

    def send(self, raw_data):
        ...
