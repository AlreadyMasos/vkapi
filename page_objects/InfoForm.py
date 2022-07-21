from framework.pages.base_page import BasePage
from framework.elements.text import Text
from framework.utils.string_util import validate_card


class InfoForm(BasePage):
    _page_ind = ('xpath', "//div[@class='page-indicator']", 'ind')

    page_ind_text = Text(*_page_ind)

    def __init__(self):
        super().__init__(*self._page_ind)

    def check_card_third(self):
        return validate_card('3', self.page_ind_text.get_text())
