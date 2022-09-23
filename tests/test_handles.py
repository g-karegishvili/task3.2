import pytest
from pages.alerts_page import AlertPage
from pages.main_page import MainPage
from pages.frames_page import FramesPage
from pages.handles_page import HandlesPage
from pages.links_page import LinksPage
from pages.tables_page import TablesPage
from utilities.file_handler import FileHandler as data
from utilities.browser_utils import BrowserUtils
from fixtures.conftest import setup


class TestToolQA:
    main_page = MainPage()
    handles_page = HandlesPage()
    links_page = LinksPage()

    def test_handles(self):
        # get to main page
        # check if main page was opened
        assert self.main_page.is_unique_element_visible(), 'main page is not open'
        # move to window page
        self.main_page.expand_afw_list()
        self.main_page.click_to_windows_btn()
        # check if windows page was opened
        assert self.handles_page.is_unique_element_visible()
        # check if new window button works
        assert self.handles_page.check_new_tab()
        # move to link page
        self.handles_page.move_to_links()
        # check if main page was opened
        assert self.links_page.check_home_link()
        # check if new tab was closed and focus returned to link page
        assert self.links_page.is_unique_element_visible()
