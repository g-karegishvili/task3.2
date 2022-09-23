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


class TestAlerts:
    main_page = MainPage()
    alert_page = AlertPage()

    def test_alerts(self):
        # check if main page is open
        assert self.main_page.is_unique_element_visible(), "main page is not open"
        # move to alert page
        self.main_page.expand_afw_list()
        self.main_page.click_to_alert_btn()
        # check if page is open
        assert self.alert_page.is_unique_element_visible(), "alert page is not open"
        # check first alert button
        self.alert_page.click_alert_btn()
        assert self.alert_page.alert_is_visible(data.get_test_data("first_alert_text")), "alert is not visible"
        # check second alert button (with confirm)
        self.alert_page.click_confirm_btn()
        assert self.alert_page.alert_is_visible(data.get_test_data("second_alert_text")), "alert is not visible"
        # check if expected text was printed out on a page
        assert self.alert_page.check_for_confirm_text(data.get_test_data("text_after_ok")), "text wasn't printed"
        # check if prompt box is open and works
        self.alert_page.click_prompt_button()
        assert self.alert_page.check_prompt_button(data.get_test_data("name_prompt_text")), "text wasn't printed"
