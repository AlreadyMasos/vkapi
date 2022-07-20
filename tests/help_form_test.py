from resourses.testconf import pytest_session_finish, pytest_session_start
from page_objects.HomePage import HomePage
from page_objects.CardsPage import CardsPage


def test_case_help(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'home page not loaded'
    home_page.click_start_button()
    cards_page = CardsPage()
    cards_page.click_hide_help_form()
    assert cards_page.check_help_form_vis(), 'help form not closed'
