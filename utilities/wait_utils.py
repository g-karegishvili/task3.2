from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.browser import Browser
from utilities.file_handler import FileHandler as fh


class WaitUtils:
    driver = Browser.return_browser()
    wait = WebDriverWait(driver, fh.get_config_data("wait_time"))

    @classmethod
    def wait_until_element_is_clickable(cls,  locator):
        return cls.wait.until(EC.element_to_be_clickable(locator))

    @classmethod
    def wait_until_element_is_visible(cls, locator):
        return cls.wait.until(EC.visibility_of_element_located(locator))

    # @classmethod
    # def wait_until_new_window_is_opened(cls):
    #     cls.wait.until(EC.new_window_is_opened(cls.driver.window_handles))

    @classmethod
    def wait_until_element_is_present(cls, locator):
        return cls.wait.until(EC.presence_of_element_located(locator))

    @classmethod
    def wait_until_alert_is_present(cls):
        return cls.wait.until(EC.alert_is_present())


