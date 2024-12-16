"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
import json

import allure
import pytest


@pytest.mark.usefixtures('create_configurations')
class TestBackendDockerManagerApi:
    """
    Тесты проверки API основного функционала приложения
    """
    @allure.feature('Команды управления контейнерами')
    @allure.story('Проверяем команды управления контейнерам: start, stop, restart')
    @pytest.mark.api
    @pytest.mark.parametrize(
        "command, container_name",
        [
            ("start", "rabbit"),
            ("stop", "rabbit"),
            ("restart", "rabbit"),
            ("start", "sbp_nspk_sanbox-nginx-1"),
            ("stop", "sbp_nspk_sanbox-nginx-1"),
            ("restart", "sbp_nspk_sanbox-nginx-1")
        ]
    )
    def test_start_command_buttons(self, command, container_name):
        answer: str = ""
        resp = self._http_client.get(f"/api/docker-qa-manage/{command}/{container_name}")
        self._logger.debug(resp.status_code)
        self._logger.debug(resp.text)
        with allure.step("Команда отправлеена получаем данные из ответа"):
            answer = json.loads(resp.text)
        assert answer["command"] == command
        assert answer["status"] == "success"
        assert resp.status_code == 200, f"Статус код {resp.status_code} не соответствует ожидаемому значению"

    @allure.feature('Команда получения списка контейнеров')
    @allure.story('Проверяем список контейнеров')
    @pytest.mark.api
    def test_getting_container_list(self):
        answer: str = ""
        resp = self._http_client.get("/api/docker-qa-manage/ps")
        self._logger.debug(resp.status_code)
        self._logger.debug(resp.text)
        with allure.step("Команда отправлеена получаем данные из ответа"):
            answer = json.loads(resp.text)
        assert answer is not None
        assert resp.status_code == 200, f"Статус код {resp.status_code} не соответствует ожидаемому значению"
