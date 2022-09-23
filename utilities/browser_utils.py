from utilities.browser import Browser
from utilities.file_handler import FileHandler as FH
from selenium.webdriver.common.action_chains import ActionChains


class BrowserUtils:
    DRIVER = Browser.return_browser()
    URL = FH.get_config_data('url')

    @classmethod
    def get_to_main_page(cls):
        cls.DRIVER.get(cls.URL)

    @classmethod
    def refresh(cls):
        cls.DRIVER.refresh()

    @classmethod
    def scroll_to_bottom(cls):
        cls.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @classmethod
    def scroll_to_element(cls, element):
        cls.DRIVER.execute_script("return arguments[0].scrollIntoView(true);", element)
