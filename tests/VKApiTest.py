from page_objects.FirstAuthPage import FirstAuthPage
from page_objects.SecondAuthPage import SecondAuthPage
from page_objects.FeedPage import FeedPage
from page_objects.MyPage import MyPage
from tests.config.testconf import pytest_session_finish, pytest_session_start
from framework.API.VKApiUtils import VKApiUtils


def test(pytest_session_start, pytest_session_finish):
    page_login = FirstAuthPage()
    assert page_login.is_opened(), 'auth page not opened'
    page_login.insert_login()
    page_login.click_login_button()
    page_password = SecondAuthPage()
    page_password.insert_password()
    page_password.click_password_button()
    feed_page = FeedPage()
    assert feed_page.is_opened(), 'feed page not opened'
    feed_page.click_my_page_button()
    my_page = MyPage()
    assert my_page.is_opened(), 'my page not opened'
    req = VKApiUtils()
    post_info = req.create_post()
    post_created = my_page.check_created_post(post_info)
    assert post_created[0], 'post not displayed'
    assert post_created[1], 'wrong post text'
    new_mes = req.edit_post(post_info[0])
    check_edited_post = my_page.check_edited_post(post_info, new_mes)
    assert check_edited_post[0], 'post not created'
    assert check_edited_post[1], 'post text not correct'
    assert check_edited_post[2], 'wrong picture'
    comment_info = req.create_post_comment(post_info[0])
    assert my_page.check_comment(comment_info), 'comment not created'
    my_page.like_post(post_info[0])
    assert req.check_like(post_info[0]), 'like is absent'
    req.delete_post(post_info[0])
    assert my_page.check_post_deleted(post_info[0]), 'post not deleted'
