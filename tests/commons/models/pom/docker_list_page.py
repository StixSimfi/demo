import time
from pathlib import Path
from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from tests.commons.models.base.base_selenium import BaseSelenium


class DockerListPageModel(BaseSelenium):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_alert(self, alert_str: str = None):
        try:
            self.alert_is_present()
            alert = self.driver.switch_to.alert
            if alert_str is not None:
                assert str(alert.text).find(alert_str)
            alert.accept()
        except TimeoutException:
            assert False, "Alert timeout exception"

    def get_list_web_elements(self, xpath: str) -> List[WebElement]:
        return self.are_present('xpath', xpath, f"find element by xpath: {xpath}")

    def get_screenshot(self, name: str = "screenie.png", path: str = Path.cwd(), delay: int = 1):
        try:
            time.sleep(delay)
            self.driver.save_screenshot(f"{path}/{name}")
        except OSError:
            assert False, f"Не могу создать скриншот {name}"

    def check_page_header(self, header: str):
        header_obj = self.is_present("tag_name", "h1")
        assert header_obj.text == header

    def check_button(self, xpath: str, command: str):
        button_obj = self.is_present('xpath', xpath)
        assert button_obj
        button_obj.click()
        time.sleep(1)
        self.check_alert(f"will be {command}ed")

    def check_restart_button(self, btn_xpath: str, state_xpath: str):
        button_obj = self.is_present('xpath', btn_xpath)
        assert button_obj
        button_obj.click()
        time.sleep(1)
        self.check_alert("will be restarted")
        time.sleep(2)
        self.get_screenshot(name="check_restart_button_state_restarted.png")
        state_obj = self.is_present('xpath', state_xpath)
        assert state_obj.text == "restarting"
        time.sleep(1)

    def check_container_status(self, xpath: str, command: str):
        status_odj = self.is_present('xpath', xpath)
        st = "running" if command == "start" else "stopped"
        print(st)
        print(status_odj.text)
        assert status_odj.text == st
