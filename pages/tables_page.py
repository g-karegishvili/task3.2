from selenium.webdriver.common.by import By
from elements.button import Button
from pages.base_page import BaseForm
from elements.form import Form
from pages.main_page import MainPage
from elements.text_input import TextInput
from utilities.wait_utils import WaitUtils as waits


class TablesPage(BaseForm):
    UNIQUE_LOCATOR = (By.XPATH, "//div[text()='Web Tables']")
    NAME = 'Tables Page'
    ADD_BUTTON_LOCATOR = (By.ID, 'addNewRecordButton')
    ADD_BUTTON = Button(ADD_BUTTON_LOCATOR, 'Add Button')
    FORM_LOCATOR = (By.ID, 'userForm')
    USER_FORM = Form(FORM_LOCATOR, 'User Form')
    ID_LIST = ["firstName", "lastName", "userEmail", "age", "salary", "department"]
    SUBMIT_BTN_LOCATOR = (By.ID, 'submit')
    DELETE_BTN_LOCATOR = (By.ID, 'delete-record-4')
    DELETE_BTN = Button(DELETE_BTN_LOCATOR, "Delete button")
    SUBMIT_BTN = Button(SUBMIT_BTN_LOCATOR, 'Submit Button')

    def __init__(self):
        super().__init__(self.UNIQUE_LOCATOR, self.NAME)

    def click_add_button(self):
        self.ADD_BUTTON.do_click()

    def form_is_visible(self):
        return self.USER_FORM.get_element()

    def fill_user_form(self, keys):
        for (input_tab, key) in zip(self.ID_LIST, keys):
            element = self.driver.find_element(By.ID, input_tab)
            element.send_keys(key)

    def click_submit_btn(self):
        self.SUBMIT_BTN.do_click()

    def click_delete_btn(self):
        self.DELETE_BTN.do_click()
