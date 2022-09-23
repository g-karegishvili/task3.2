from elements.base_element import BaseElement
from utilities.wait_utils import WaitUtils


class TextOutput(BaseElement):

    def __init__(self, locator, name):
        super().__init__(locator, name)

    def get_text(self):
        element = WaitUtils.wait_until_element_is_visible(self.locator)
        return element.text
