from selenium.webdriver.common.by import By
from pages.base_page import BaseForm
from elements.button import Button
from utilities.browser_utils import BrowserUtils
from utilities.logger import Logger


class MainPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//img[@alt='Selenium Online Training']")
    NAME = "Main Page"
    AFW_BTN_LOCATOR = (By.XPATH, "(//div[contains(@class, 'top-card')])[3]")  # AFW  - Alerts, Frames and Windows
    AFW_BTN = Button(AFW_BTN_LOCATOR, "alert_button")
    ELEMENTS_BTN_LOCATOR = (By.XPATH, "(//div[contains(@class, 'top-card')])[1]")
    ELEMENTS_BTN = Button(ELEMENTS_BTN_LOCATOR, "Elements Button")
    TO_ALERT_BTN_LOCATOR = (By.XPATH, "//span[ text()='Alerts']")
    TO_ALERT_BTN = Button(TO_ALERT_BTN_LOCATOR, "alert button")
    TO_NESTED_FRAMES_LOCATOR = (By.XPATH, "//span[text()='Nested Frames']")
    TO_NESTED_FRAMES_BTN = Button(TO_NESTED_FRAMES_LOCATOR, "nested frames button")
    TO_WINDOWS_LOCATOR = (By.XPATH, "//span[text()='Browser Windows']")
    To_WINDOWS_BTN = Button(TO_WINDOWS_LOCATOR, "browser windows button")
    TO_TABLES_BTN_LOCATOR = (By.XPATH, "//span[text()='Web Tables']")
    TO_TABLES_BTN = Button(TO_TABLES_BTN_LOCATOR, 'Tables Button')
    logger = Logger.logger()

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def expand_afw_list(self):
        self.AFW_BTN.do_click()
        self.logger.info("alerts, frames, windows element expanded")

    def expand_element_list(self):
        self.ELEMENTS_BTN.do_click()

    def click_to_alert_btn(self):
        self.TO_ALERT_BTN.do_click()

    def click_to_frames_btn(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.TO_NESTED_FRAMES_BTN.do_click()

    def click_to_windows_btn(self):
        self.To_WINDOWS_BTN.do_click()

    def click_to_tables_btn(self):
        self.TO_TABLES_BTN.do_click()
