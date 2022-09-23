from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from utilities.wait_utils import WaitUtils


class Form(BaseElement):

    def __init__(self, locator, name):
        super().__init__(locator, name)


