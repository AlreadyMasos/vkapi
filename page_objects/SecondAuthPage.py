from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from framework.utils.data_parser import DataSetParser


class SecondAuthPage(BasePage):

    data = DataSetParser().get_dataset()

    password_input = TextBox('xpath', "//input[@type='password']", 'pass_inp')
    pass_button = Button('xpath', "//button[@type='submit']", 'pass_button')

    def __init__(self):
        super().__init__(self.pass_button.get_search_condition(),
                         self.pass_button.get_locator(),
                         self.pass_button.get_name())

    def insert_password(self):
        self.password_input.wait_for_is_visible()
        self.password_input.send_keys(self.data['password'])

    def click_password_button(self):
        self.pass_button.click()
