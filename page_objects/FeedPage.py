from framework.pages.base_page import BasePage
from framework.elements.button import Button


class FeedPage(BasePage):

    my_page_button = Button('xpath', '//li[@id="l_pr"]', 'my_page_button')

    def __init__(self):
        super().__init__(self.my_page_button.get_search_condition(),
                         self.my_page_button.get_locator(),
                         self.my_page_button.get_name())

    def click_my_page_button(self):
        self.my_page_button.click()
