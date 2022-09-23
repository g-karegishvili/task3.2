from selenium.webdriver.common.by import By
from elements.button import Button
from pages.base_page import BaseForm
from pages.main_page import MainPage


class LinksPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//div[text()='Links']")
    NAME = 'Links Page'
    HOME_BTN_LOCATOR = (By.ID, 'simpleLink')
    HOME_BTN = Button(HOME_BTN_LOCATOR, "To Home")
    MAIN_PAGE = MainPage()

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def check_home_link(self):
        current_handle = self.driver.current_window_handle
        self.HOME_BTN.do_click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break
        element = self.MAIN_PAGE.is_unique_element_visible()
        self.driver.close()
        self.driver.switch_to.window(current_handle)
        return element is not None


