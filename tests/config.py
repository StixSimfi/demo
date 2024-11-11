"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""

__HOST = "localhost"
__BACKEND_PORT = "8000"

"""
__SELENIUM_HUB - параметр содержащий путь к развернутому селениум хабу для тестирования на удаленном сервере для его 
использования установите __WEB_DRIVER_LAUNCH_PARAMETER в значение 'remote' или None.
"""
__SELENIUM_HUB = "http://selenium:4444/wd/hub"
__WEB_DRIVER_LAUNCH_PARAMETER = "remote"
#__WEB_DRIVER_LAUNCH_PARAMETER = "local"