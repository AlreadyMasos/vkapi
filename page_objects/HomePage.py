from framework.pages.base_page import BasePage
from framework.elements.button import Button


class HomePage(BasePage):
    _no_button_path = "//button[@class='start__button']"
    _start_link_path = "//a[@class='start__link']"
    start_button = Button('xpath', _start_link_path,'start button')

    def __init__(self):
        super().__init__('xpath', self._no_button_path, 'home page')

    def check_load_home_page(self):
        return super().is_opened()

    def click_start_button(self):
        self.start_button.click()

