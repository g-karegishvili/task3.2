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


class TestTables:
    main_page = MainPage()
    tables_page = TablesPage()
    first_set_values = list(data.get_test_data("first_set").values())
    second_set_values = list(data.get_test_data("second_set").values())
    @pytest.mark.parametrize("test_input", [first_set_values, second_set_values])
    def test_tables(self, test_input):
        self.main_page.expand_element_list()
        self.main_page.click_to_tables_btn()
        self.tables_page.click_add_button()
        assert self.tables_page.form_is_visible()
        self.tables_page.fill_user_form(test_input)
        self.tables_page.click_submit_btn()
        self.tables_page.click_delete_btn()
