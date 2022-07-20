from page_objects.HomePage import HomePage
from page_objects.CardsPage import CardsPage
from page_objects.FilePage import FilePage
from page_objects.ThirdPage import ThirdPage
from resourses.testconf import pytest_session_start, pytest_session_finish


def test_case_cards(pytest_session_start, pytest_session_finish):
    home_page = HomePage()
    assert home_page.check_load_home_page(), 'home page not loaded'
    home_page.click_start_button()
    cards_page = CardsPage()
    assert cards_page.check_card_first(), 'not first card'
    cards_page.fill_form()
    file_page = FilePage()
    assert file_page.check_number(), 'not second card'
    file_page.click_checks()
    file_page.upload_file()
    file_page.click_next()
    third_card_page = ThirdPage()
    assert third_card_page.check_card_third(), 'not third card'
