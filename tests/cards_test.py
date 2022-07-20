from page_objects.HomePage import HomePage
from resourses.testconf import pytest_session_start, pytest_session_finish


def test_case_1(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'not loaded'
    home_page.click_start_button()
