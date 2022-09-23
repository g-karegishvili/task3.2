from abc import ABC, abstractmethod
from utilities.browser import Browser
from utilities.wait_utils import WaitUtils
from selenium.webdriver import ActionChains


class BaseElement(ABC):

    @abstractmethod
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.driver = Browser.return_browser()

    def get_element(self):
        element = WaitUtils.wait_until_element_is_present(self.locator)
        return element

    def do_click(self):
        element = WaitUtils.wait_until_element_is_clickable(self.locator)
        element.click()



