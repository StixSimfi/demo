"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: ООО "Мультикарта", УТПО ДРТ, 2021-2023
"""
import logging
import os
import pathlib
from datetime import datetime
from logging import Logger


class Log:
    """ Класс логер """
    def __init__(self,
                 log_name: str = "main",
                 file_handler_level: int = logging.INFO,
                 stream_handler_level: int = logging.INFO,
                 log_path: str = ""
                 ):
        """
        :param log_name: Имя логера по умолчанию файл лога имеет вид file_name по имени файла или класса, где был
        осуществлен вызов.
        :param file_handler_level:
        :param stream_handler_level:
        :param log_path:
        """
        self.__log_name = log_name
        self._stream_handler = stream_handler_level
        self._file_handler_level = file_handler_level
        if log_path == "":
            self.__path = os.path.abspath("") + "/logs/" + log_name + "/"
        else:
            self.__path = log_path
        pathlib.Path(self.__path).mkdir(parents=True, exist_ok=True)
        self.__log_format = "%(asctime)s - [%(levelname)s] - %(name)s - " \
                            "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

    def get_file_handler(self) -> logging.FileHandler:
        now = datetime.now()
        file_handler = logging.FileHandler(
            self.__path + self.__log_name + "_{}_{}_{}_{}.{}.{}".format(
                now.day,
                now.month,
                now.year,
                now.hour,
                now.minute,
                now.second
            ) + ".log")
        file_handler.setLevel(self._file_handler_level)
        file_handler.setFormatter(logging.Formatter(self.__log_format))
        return file_handler

    def get_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(self.__log_format))
        return stream_handler

    def get_logger(self) -> Logger:
        logger = logging.getLogger(self.__log_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.get_file_handler())
        logger.addHandler(self.get_stream_handler())
        return logger
