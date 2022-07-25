from API import Request


def test_step():
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/')
    assert resp.status_code_check(200)
    assert resp.check_if_json()
    assert resp.check_if_sorted_by_id()
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/99')
    assert resp.status_code_check(200)
    assert resp.check_99_post()
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/150')
    assert resp.check_empty()
    assert resp.status_code_check(404)
    resp = Request('post', 'https://jsonplaceholder.typicode.com/posts/')
    assert resp.check_correct_post_req() and resp.status_code_check(201)
    resp = Request('get', 'https://jsonplaceholder.typicode.com/users/')
    assert resp.check_if_json() and resp.status_code_check(200)
    user_with_id = resp.find_user_by_id(5)
    assert resp.check_correct_user(user_with_id)
    resp = Request('get', 'https://jsonplaceholder.typicode.com/users/5')
    assert resp.status_code_check(200)
    assert resp.check_correct_user(resp.get_json())
