from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage
from framework_UI.Steps.Steps import Steps
from framework_UI.utils.random_util import get_random_password_and_email


def test_case_cards(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'home page not loaded'
    home_page.click_start_button()
    register_page = RegisterPage()
    assert register_page.check_card_first(), 'not first card'
    register_page.fill_form(*get_random_password_and_email())
    assert register_page.file_form.check_number(), 'not second card'
    register_page.file_form.click_checks()
    register_page.file_form.click_upload_file_button()
    Steps.upload_image()
    register_page.file_form.click_next()
    assert register_page.info_form.check_card_third(), 'not third card'
