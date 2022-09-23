from selenium.webdriver.common.by import By
from pages.base_page import BaseForm
from elements.button import Button
from utilities.wait_utils import WaitUtils as waits
from utilities.file_handler import FileHandler
from selenium.common.exceptions import NoAlertPresentException
from elements.text_output import TextOutput
from utilities.RandomUtils import RandomUtils as rand
from utilities.logger import Logger


class AlertPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//div[text()='Alerts']")
    NAME = 'Alert Page'
    CLICK_ALERT_BTN_LOCATOR = (By.ID, 'alertButton')
    CLICK_ALERT_BTN = Button(CLICK_ALERT_BTN_LOCATOR, "Click Alert")
    CONFIRM_BTN_LOCATOR = (By.ID, 'confirmButton')
    CONFIRM_BTN = Button(CONFIRM_BTN_LOCATOR, 'Confirm Button')
    CONFIRM_TEXT_LOCATOR = (By.ID, 'confirmResult')
    CONFIRM_TEXT = TextOutput(CONFIRM_TEXT_LOCATOR, "confirm text")
    PROMPT_BTN_LOCATOR = (By.ID, 'promtButton')
    PROMPT_BTN = Button(PROMPT_BTN_LOCATOR, 'Prompt Button')
    PROMPT_RESULT_LOCATOR = (By.ID, 'promptResult')
    PROMPT_RESULT = TextOutput(PROMPT_RESULT_LOCATOR, "Prompt result")
    log = Logger.logger()

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def click_alert_btn(self):
        self.CLICK_ALERT_BTN.do_click()

    def alert_is_visible(self, expected_text):
        alert = waits.wait_until_alert_is_present()
        text = alert.text
        alert.accept()
        self.log.info("alert is closed")
        return text == expected_text

    # @staticmethod
    # def alert_is_closed():
    #     try:
    #         alert = WaitUtils.wait_until_alert_is_present()
    #     except NoAlertPresentException:
    #         return True

    def click_confirm_btn(self):
        self.CONFIRM_BTN.do_click()

    def check_for_confirm_text(self, expected_result):
        return self.CONFIRM_TEXT.get_text() == expected_result

    def click_prompt_button(self):
        self.PROMPT_BTN.do_click()

    def check_prompt_button(self, expected_text):
        alert = waits.wait_until_alert_is_present()
        text = alert.text
        random_text = rand.get_random_text()
        alert.send_keys(random_text)
        alert.accept()
        self.log.info("alert was closed")
        return random_text in self.PROMPT_RESULT.get_text() and text == expected_text
