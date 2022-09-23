from selenium.webdriver.common.by import By
from elements.button import Button
from elements.text_output import TextOutput
from pages.base_page import BaseForm
from utilities.file_handler import FileHandler as fh
from utilities.browser_utils import BrowserUtils
from utilities.logger import Logger


class HandlesPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//div[text()='Browser Windows']")
    NAME = 'Handles Page'
    NEW_TAB_BTN_LOCATOR = (By.ID, 'tabButton')
    NEW_TAB_BTN = Button(NEW_TAB_BTN_LOCATOR, "New Tab")
    TO_ELEMENTS_LOCATOR = (By.XPATH, "//div[text()='Elements']")
    TO_ELEMENTS_BTN = Button(TO_ELEMENTS_LOCATOR, "Elements")
    TO_LINKS_LOCATOR = (By.XPATH, "//span[text()='Links']")
    TO_LINKS_BTN = Button(TO_LINKS_LOCATOR, "Links")
    NEW_TAB_TEXT_LOCATOR = (By.ID, 'sampleHeading')
    NEW_TAB_TEXT = TextOutput(NEW_TAB_TEXT_LOCATOR, "New Tab Text")
    logger = Logger.logger()

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def check_new_tab(self):
        main_handle = self.driver.current_window_handle
        self.NEW_TAB_BTN.do_click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_handle:
                self.driver.switch_to.window(handle)
                break
        text = self.NEW_TAB_TEXT.get_text()
        self.driver.close()
        self.driver.switch_to.window(main_handle)
        self.logger.info("focus switched to main handle")
        return text == fh.get_test_data("new_tab_text")

    def move_to_links(self):
        self.TO_ELEMENTS_BTN.do_click()
        BrowserUtils.scroll_to_element(self.TO_LINKS_BTN.get_element())
        self.TO_LINKS_BTN.do_click()






