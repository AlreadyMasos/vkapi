from API import Request


def test_step():
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/')
    assert resp.status_code_check(200)
    assert resp.check_if_json()
    assert resp.check_if_sorted('id')
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/99')
    assert resp.status_code_check(200)
    assert resp.check_post()
    resp = Request('get', 'https://jsonplaceholder.typicode.com/posts/150')
    assert resp.check_empty()
    assert resp.status_code_check(404)

