from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from abc import ABCMeta, abstractmethod, ABC
from utilities.file_handler import FileHandler




class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Browser(metaclass=SingletonMeta):
    @staticmethod
    def return_browser(cmdopt='chrome'):
        if cmdopt == "chrome":
            return ChromeBrowser().get_driver()
        elif cmdopt == "firefox":
            return FireFoxBrowser().get_driver()


class ChromeBrowser(Browser):

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_driver(self):
        return self.driver


class FireFoxBrowser(Browser):
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def get_driver(self):
        return self.driver
