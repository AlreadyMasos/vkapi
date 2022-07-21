from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage
from config.testconf import pytest_session_start, pytest_session_finish


def test_case_cookie(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'home page not loaded'
    home_page.click_start_button()
    register_page = RegisterPage()
    register_page.cookie_accept()
    assert register_page.check_if_cookie_form_closed(), 'cookie form not closed'
