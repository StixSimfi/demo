"""
Base seleniun class
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BaseSelenium:
    """

    """

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 100, 0.3)

    def __selenium_find_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'id': By.ID,
            'class': By.CLASS_NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'name': By.NAME
        }
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str) -> WebElement:
        """
        Waiting on element and return WebElement if it is visible
        """
        return self.__wait.until(
            ec.visibility_of_element_located((self.__selenium_find_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """
        Waiting on element and return WebElement if it is present on DOM
        """
        return self.__wait.until(
            ec.presence_of_element_located((self.__selenium_find_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """
        Wait on element until it disappears
        """
        return self.__wait.until(
            ec.invisibility_of_element_located((self.__selenium_find_by(find_by), locator)), locator_name)

    def is_element_clickable(self, element: WebElement) -> bool:
        """
        Wait on element until and check is clickable
        """
        return self.__wait.until(ec.element_to_be_clickable(element))

    def alert_is_present(self):
        return self.__wait.until(ec.alert_is_present())

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """
        Waiting on elements and return WebElements if they are visible
        """
        return self.__wait.until(
            ec.visibility_of_all_elements_located((self.__selenium_find_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """
        Waiting on elements and return WebElements if they are present on DOM
        """
        return self.__wait.until(
            ec.presence_of_all_elements_located((self.__selenium_find_by(find_by), locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        """
        The input should be a list of WebElements, where we read text from each element and Return a List[String]
        """
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        """
        The input should be a list of WebElements, from which we return a single WebElement found by it's name
        """
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def get_list_cookies(self) -> List[dict]:
        return self.driver.get_cookies()

    def delete_cookie(self, cookie_name: str) -> None:
        """
        Delete a cookie by a name
        """
        self.driver.delete_cookie(cookie_name)

    def delete_all_cookies(self) -> None:
        """
        Delete all cookie
        """
        self.driver.delete_all_cookies()

    def get_page_title(self) -> str:
        """
        Return current title web page from web driver
        """
        return self.driver.title
