from utilities.browser import Browser
from utilities.file_handler import FileHandler
import pytest
import time

CHROME_BROWSER = FileHandler.get_config_data("chrome_browser")
FIREFOX_BROWSER = FileHandler.get_config_data("firefox_browser")


@pytest.fixture(autouse=True)
def setup():
    driver = Browser.return_browser()
    url = FileHandler.get_config_data('url')
    driver.get(url)
    #request.cls.driver = driver
    yield
    driver.quit()



# def pytest_addoption(parser):
#     parser.addoption("--browser", action='store', default='chrome', help='choose: chrome or firefox')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")
