from framework.pages.base_page import BasePage
from framework.elements.text import Text
from framework.elements.button import Button
from framework.elements.checkbox import CheckBox
from framework.utils.autoit_utils import AutoItUtils
from framework.utils.string_util import validate_card
from framework.utils.random_util import random_list_element
from framework.utils.dataset_parser import DataSetParser


class FileForm(BasePage):
    DATASET = DataSetParser().get_dataset()['cards_test']
    _upload_button = ('xpath', '//a[@class="avatar-and-interests__upload-button"]', 'upload')

    text_card = Text('xpath', "//div[@class='page-indicator']", 'ind')
    upload_btn = Button(*_upload_button)
    all_inters = CheckBox('xpath', '//div[@class="avatar-and-interests__interests-list__item"]','interests')
    btn_next = Button('xpath', '//button[@class="button button--stroked button--white button--fluid"]', 'next_btn')

    def __init__(self):
        super().__init__(*self._upload_button)

    def check_number(self):
        return validate_card(self.DATASET['second_validate'], self.text_card.get_text())

    def upload_file(self):
        self.upload_btn.click()

    def click_checks(self):
        for check in self.all_inters.get_elements():
            check.click()
        for check in random_list_element(self.all_inters.get_elements(),2):
            check.click()

    def click_next(self):
        self.btn_next.click()
