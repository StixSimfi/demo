"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
import os
from dotenv import load_dotenv


"""
__SELENIUM_HUB - параметр содержащий путь к развернутому селениум хабу для тестирования на удаленном сервере для его
использования установите __WEB_DRIVER_LAUNCH_PARAMETER в значение 'remote' или None.
"""

load_dotenv()
_HOST = os.environ.get("__HOST")
_BACKEND_PORT = os.environ.get("__BACKEND_PORT")
_WEB_DRIVER_LAUNCH_PARAMETER = os.environ.get("__WEB_DRIVER_LAUNCH_PARAMETER")
_SELENIUM_HUB = os.environ.get("__SELENIUM_HUB")
_BACKEND_HOST = os.environ.get("__BACKEND_HOST")
print(_BACKEND_HOST)
