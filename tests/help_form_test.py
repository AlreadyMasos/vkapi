from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage
from config.testconf import pytest_session_start, pytest_session_finish


def test_case_help(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'home page not loaded'
    home_page.click_start_button()
    register_page = RegisterPage()
    register_page.click_hide_help_form()
    assert register_page.check_help_form_vis(), 'help form not closed'
