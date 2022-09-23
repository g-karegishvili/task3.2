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



class TestFrames:
    main_page = MainPage()
    frame_page = FramesPage()

    def test_frames(self):
        # get to main page
        # assert if main page was open
        assert self.main_page.is_unique_element_visible(), "main page is not open"
        # move to frames
        self.main_page.expand_afw_list()
        self.main_page.click_to_frames_btn()
        # check if frames pages was opened
        assert self.frame_page.is_unique_element_visible(), "frames page is not open"
        # check if frames are visible
        assert self.frame_page.messages_are_visible(data.get_test_data("parent_frame"),
                                                    data.get_test_data("child_frame")), "frames aren't visible"
