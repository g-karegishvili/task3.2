from selenium.webdriver.common.by import By
from elements.frame import Frame
from elements.text_output import TextOutput
from pages.base_page import BaseForm


class FramesPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//div[text()='Nested Frames']")
    NAME = "Frames Page"
    PARENT_IFRAME_LOCATOR = (By.ID, "frame1")
    PARENT_IFRAME = Frame(PARENT_IFRAME_LOCATOR, "Parent iFrame")
    PARENT_TEXT_LOCATOR = (By.TAG_NAME, 'body')
    PARENT_TEXT = TextOutput(PARENT_TEXT_LOCATOR, "Parent Text")
    CHILD_IFRAME_LOCATOR = (By.XPATH, '/iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_IFRAME = Frame(CHILD_IFRAME_LOCATOR, "Child iFrame")
    CHILD_TEXT_LOCATOR = (By.TAG_NAME, 'p')
    CHILD_TEXT = TextOutput(CHILD_TEXT_LOCATOR, "Child Text")

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def messages_are_visible(self, parent_text_exp, child_text_exp):
        self.PARENT_IFRAME.switch_to()
        parent_text = self.PARENT_TEXT.get_text()
        self.CHILD_IFRAME.switch_to_child()
        child_text = self.CHILD_TEXT.get_text()
        return parent_text == parent_text_exp and child_text == child_text_exp
