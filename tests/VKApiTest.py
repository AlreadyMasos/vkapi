from page_objects.FirstAuthPage import FirstAuthPage
from page_objects.SecondAuthPage import SecondAuthPage
from page_objects.FeedPage import FeedPage
from page_objects.MyPage import MyPage
from tests.config.testconf import pytest_session_finish, pytest_session_start
from framework.API.VKApiUtils import VKApiUtils


def test(pytest_session_start):
    page_login = FirstAuthPage()
    assert page_login.is_opened()
    page_login.insert_login()
    page_login.click_login_button()
    page_password = SecondAuthPage()
    page_password.insert_password()
    page_password.click_password_button()
    feed_page = FeedPage()
    assert feed_page.is_opened()
    feed_page.click_my_page_button()
    my_page = MyPage()
    assert my_page.is_opened()
    req = VKApiUtils()
    post_id = req.create_post()
    assert my_page.check_created_post(post_id)

