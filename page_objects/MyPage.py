from framework.pages.base_page import BasePage
from framework.elements.button import Button


class MyPage(BasePage):

    all_posts_button = Button('xpath', '//li[@class="_wall_tab_all"]', 'all_posts_button')

    def __init__(self):
        super().__init__(self.all_posts_button.get_search_condition(),
                         self.all_posts_button.get_locator(),
                         self.all_posts_button.get_name())

    def click_my_page_button(self):
        self.all_posts_button.click()
