"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
import time

import allure
import pytest
from tests.commons.models.pom.docker_list_page import DockerListPageModel


@pytest.mark.usefixtures('setup')
class TestDockerManagerUi:
    """

    """

    @allure.feature('Наличие заголовка H1')
    @allure.story('Проверяем наличие заголовка H1 и его соответсвие ожидаемому результату')
    @pytest.mark.ui
    def test_docker_manager_page(self):
        docker_list_page: DockerListPageModel = DockerListPageModel(self._driver)
        # Снимаем скрин тестируемой страницы
        docker_list_page.get_screenshot(name="main_page.png")
        # Проверяем наличие заголовка H1 и его соответсвие ожидаемому результату
        docker_list_page.check_page_header("Docker Manager")

    @allure.feature('Проверка статуса кнопок управления start, stop')
    @allure.story('Проверяем работоспособность кнопок start, stop и изменение текстового описания состояния контейнера.')
    @pytest.mark.ui
    @pytest.mark.parametrize("command, pid", [("start", "1"), ("stop", "2")])
    def test_start_stop_command_buttons(self, command: str, pid: str):
        docker_list_page: DockerListPageModel = DockerListPageModel(self._driver)
        docker_list_page.get_screenshot(name=f"check_{command}_button_before.png")
        docker_list_page.check_button(
            f'//*/tbody/tr[1]/td[7]/button[{pid}]',
            command
        )
        time.sleep(1)
        docker_list_page.check_container_status("//*/tbody/tr[1]/td[2]/strong", command)
        docker_list_page.get_screenshot(name=f"check_{command}_button_after.png")

    @allure.feature('Проверка статуса кнопок управления restart')
    @allure.story('Проверяем работоспособность кнопок restart и изменение текстового описания состояния контейнера.')
    @pytest.mark.ui
    def test_restart_command_buttons(self):
        docker_list_page: DockerListPageModel = DockerListPageModel(self._driver)
        docker_list_page.get_screenshot(name="check_restart_button_before.png")
        docker_list_page.check_restart_button(
            "//*/tbody/tr[1]/td[7]/button[3]",
            "//*/tbody/tr[1]/td[2]/strong")
        docker_list_page.get_screenshot(name="check_restart_button_after.png")
