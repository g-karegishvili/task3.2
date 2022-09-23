from elements.base_element import BaseElement
from utilities.wait_utils import WaitUtils


class TextInput(BaseElement):

    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys(self, text):
        element = WaitUtils.wait_until_element_is_visible(self.locator)
        element.send_keys(text)
