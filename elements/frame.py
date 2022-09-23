from elements.base_element import BaseElement
from utilities.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class Frame(BaseElement):

    def __init__(self, locator, name):
        super().__init__(locator, name)

    def switch_to(self):
        frame = WaitUtils.wait_until_element_is_visible(self.locator)
        self.driver.switch_to.frame(frame)

    def switch_to_child(self):
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
