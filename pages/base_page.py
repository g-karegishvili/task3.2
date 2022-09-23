from abc import ABC, abstractmethod
from utilities.browser import Browser
from utilities.wait_utils import WaitUtils as waits


class BaseForm(ABC):

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.driver = Browser.return_browser()

    def is_unique_element_visible(self):
        element = waits.wait_until_element_is_visible(self.locator)
        return element
