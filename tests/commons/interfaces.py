"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
import logging
from abc import ABC, abstractmethod
from typing import Any


class IClient(ABC):

    """
        Интерфейс класса, позволит объявить контракт интерфейса и реализовать классы на основе различных библиотек.
        Объявляет основные абстрактные методы клиента.
    """

    def __init__(self, remote_server_address: str, logger: logging):
        """
        Клас наследник должен принимать адрес удаленного серверу и объект логера.
        :param remote_server_address: Адрес удаленного сервера.
        :param logger: Объект класса логера.
        """
        self._remote_server_address = remote_server_address
        self.__logger = logger

    @abstractmethod
    def get(self, route: str):
        ...

    @abstractmethod
    def post(self, route: str, data: Any):
        ...

    @abstractmethod
    def put(self, route: str, data: Any):
        ...

    @abstractmethod
    def delete(self, route: str):
        ...

    @abstractmethod
    def patch(self, route: str, data: Any):
        ...
