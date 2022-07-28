from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage
from config.testconf import pytest_session_start, pytest_session_finish


def test_case_timer(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    home_page.click_start_button()
    register_page = RegisterPage()
    assert register_page.validate_timer(), 'timer starts with wrong time'
