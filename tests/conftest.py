"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""

import pytest
import logging

from .commons.logger import Log
from .commons.client import Client
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# Используем алеас для драйвера firefox, что бы при реализации прочих браузеров не возникло пересечений
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .config import (
    __HOST,
    __BACKEND_PORT,
    __WEB_DRIVER_LAUNCH_PARAMETER,
    __SELENIUM_HUB
)


# UI tests fixtures
@pytest.fixture(scope='class')
def get_firefox_options() -> FirefoxOptions:
    """
    Фикстура настройки драйвера firefox
    :return: FirefoxOptions
    """
    options = FirefoxOptions()
    # При необходимости использовать options.add_argument('headless')
    options.add_argument('--window-size=1650,900')
    # Использовать Agent Spoofing requires для режима headless
    # Модифицируйте user-agent в соответствии с требованиями проекта
    options.add_argument(
        'user-agent=[User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0]')
    return options


@pytest.fixture(scope='class')
def get_webdriver(get_firefox_options) -> webdriver:
    options = get_firefox_options
    service = FirefoxService()
    if __WEB_DRIVER_LAUNCH_PARAMETER == "local":
        driver = webdriver.Firefox(options=options, service=service)
    else:
        options.add_argument('headless')
        driver = webdriver.Remote(command_executor=__SELENIUM_HUB, options=options)
    driver.maximize_window()
    # driver = EventFiringWebDriver(driver, MyListener())
    yield driver


@pytest.fixture(scope='class')
def setup(request, get_webdriver):
    driver: webdriver = get_webdriver
    url: str = f"http://{__HOST}/"
    if request.cls is not None:
        request.cls._driver = driver
        driver.get(url)
    yield driver
    driver.quit()


# Module API fixtures
@pytest.fixture(scope="class")
def create_configurations(request):
    request.cls._logger = Log(request.cls.__name__, file_handler_level=logging.DEBUG).get_logger()
    # Разделяем файлы логирования для тестов и клиента
    if request.cls is not None:
        client = Client(
            f"http://{__HOST}:{__BACKEND_PORT}",
            Log("client_logger", file_handler_level=logging.DEBUG).get_logger()) # noqa
        request.cls._http_client = client
        yield client
        del client
