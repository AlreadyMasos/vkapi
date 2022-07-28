from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from framework.utils.data_parser import DataSetParser


class FirstAuthPage(BasePage):

    data = DataSetParser().get_dataset()

    login_input = TextBox('xpath', '//input[@class="VkIdForm__input"]', 'log_inp')
    login_button = Button('xpath', '//button[@class="FlatButton FlatButton--primary FlatButton--size-l '
                                   'FlatButton--wide VkIdForm__button VkIdForm__signInButton"]', 'log_button')

    def __init__(self):
        super().__init__(self.login_input.get_search_condition(),
                         self.login_input.get_locator(),
                         self.login_input.get_name())

    def insert_login(self):
        self.login_input.send_keys(self.data['login'])

    def click_login_button(self):
        self.login_button.click()
