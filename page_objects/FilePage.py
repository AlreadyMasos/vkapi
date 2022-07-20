from framework.pages.base_page import BasePage
from framework.elements.text import Text
from framework.elements.button import Button
from framework.elements.checkbox import CheckBox
from framework.utils.autoit_utils import AutoItUtils
from framework.utils.string_util import validate_card
from framework.utils.random_util import random_list_element


class FilePage(BasePage):
    _upload_button = ('xpath', '//a[@class="avatar-and-interests__upload-button"]', 'upload')
    _page_ind = ('xpath', "//div[@class='page-indicator']", 'ind')
    _interests_loc = ('xpath', '//div[@class="avatar-and-interests__interests-list__item"]','interests')
    _next_path = ('xpath', '//button[@class="button button--stroked button--white button--fluid"]', 'next_btn')

    text_card = Text(*_page_ind)
    _upload_btn = Button(*_upload_button)
    all_inters = CheckBox(*_interests_loc)
    btn_next = Button(*_next_path)

    def __init__(self):
        super().__init__(*self._upload_button)

    def check_number(self):
        return validate_card('2', self.text_card.get_text())

    def upload_file(self):
        self._upload_btn.click()
        auto = AutoItUtils()
        auto.upload_image()

    def click_checks(self):
        for check in self.all_inters.get_elements():
            check.click()
        for check in random_list_element(self.all_inters.get_elements(),2):
            check.click()

    def click_next(self):
        self.btn_next.click()