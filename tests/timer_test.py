from resourses.testconf import pytest_session_finish, pytest_session_start
from page_objects.HomePage import HomePage
from page_objects.CardsPage import CardsPage


def test_case_timer(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    home_page.click_start_button()
    cards_page = CardsPage()
    assert cards_page.validate_timer(), 'timer starts with wrone time'
