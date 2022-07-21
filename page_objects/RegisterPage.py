from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.text import Text
from framework.elements.checkbox import CheckBox
from framework.elements.button import Button
from framework.elements.form import Form
from framework.utils.config_parser import ConfigParser
from framework.utils.random_util import get_random_password_and_email
from framework.utils.string_util import validate_timer_string, validate_card
from page_objects.FileForm import FileForm
from page_objects.InfoForm import InfoForm


class RegisterPage(BasePage):

    CONFIG = ConfigParser().get_config()
    _timer = ('xpath', '//div[@class="timer timer--white timer--center"]', 'cards')

    password_textbox = TextBox('xpath', "//input[@placeholder='Choose Password']", 'pass')
    email_textbox = TextBox('xpath', "//input[@placeholder='Your email']", 'email')
    domain_textbox = TextBox('xpath', "//input[@placeholder='Domain']", 'dom')
    page_ind_text = Text('xpath', "//div[@class='page-indicator']", 'ind')
    button_drop = Button('xpath', '//div[@class="dropdown dropdown--gray"]', 'dropdown')
    accept_checkbox = CheckBox('xpath', '//span[@class="checkbox__box"]', 'checkbox')
    next_button = Button('xpath', '//a[@class="button--secondary"]', 'next_btn')
    org_button = Button('xpath', "//div[text()='.org']", 'org')
    timer = TextBox(*_timer)
    accept_cookie_button = Button('xpath', '//button[@class="button button--solid button--transparent"]', 'cookie_accept')
    cookie_form = TextBox('xpath', '//p[@class="cookies__message"]', 'cookie_form')
    help_button = Button('xpath', '//button[@class="button button--solid button--blue help-form__send-to-bottom-button"]', 'help')
    help_form = Form('xpath', '//div[@class="help-form__container"]', 'help_form')

    def __init__(self):
        super().__init__(*self._timer)
        self.file_form = FileForm()
        self.info_form = InfoForm()

    def fill_form(self):
        password, email, domain = get_random_password_and_email()
        self.password_textbox.clear_field()
        self.password_textbox.send_text(password)
        self.email_textbox.clear_field()
        self.email_textbox.send_text(email)
        self.domain_textbox.clear_field()
        self.domain_textbox.send_text(domain)
        self.accept_checkbox.click()
        self.button_drop.click()
        self.org_button.wait_for_is_visible()
        self.org_button.click()
        self.next_button.click()

    def check_card_first(self):
        return validate_card('1', self.page_ind_text.get_text())

    def validate_timer(self):
        return validate_timer_string(self.timer.get_text())

    def cookie_accept(self):
        self.accept_cookie_button.click()

    def check_if_cookie_form_closed(self):
        return True if not self.cookie_form.is_displayed() else False

    def click_hide_help_form(self):
        self.help_button.click()

    def check_help_form_vis(self):
        self.help_form.wait_for_invisibility()
        return True if not self.help_form.is_displayed() else False
