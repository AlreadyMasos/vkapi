from framework.Endpoints.ApiPost import PostApi
from framework.Endpoints.ApiUser import UserApi


def test_step():
    posts = PostApi()
    posts.get_posts()
    assert posts.check_if_json(), 'not json'
    assert posts.check_if_sorted_by_id(), 'not sorted by id'
    posts.get_post_99()
    assert posts.check_99_post(), 'wrong post information'
    posts.get_post_150()
    assert posts.check_empty(), 'not empty json'
    posts.create_post()
    assert posts.check_correct_post_req(), 'wrong random post info'
    user = UserApi()
    user.get_user()
    assert user.check_if_json(), 'not json'
    assert user.check_correct_user_with_id(), 'wrong user information'
    user.get_user_with_id()
    assert user.check_correct_user(), 'wrong user information'
