from entitys.API import Request
from framework.utils.cfg_parser import ConfigParser


def test_step():
    cfg = ConfigParser().get_config()
    resp_first = Request(*cfg['first_req'])
    assert resp_first.check_code_200(), 'wrong code'
    assert resp_first.check_if_json(), 'not json'
    assert resp_first.check_if_sorted_by_id(), 'not sorted by id'
    resp_second = Request(*cfg['second_req'])
    assert resp_second.check_code_200(), 'wrong code'
    assert resp_second.check_99_post(), 'wrong post information'
    resp_third = Request(*cfg['third_req'])
    assert resp_third.check_empty(), 'not empty json'
    assert resp_third.check_code_404(), 'wrong code'
    resp_fourth = Request(*cfg['fourth_req'])
    assert resp_fourth.check_correct_post_req(), 'wrong post'
    assert resp_fourth.check_code_201(), 'wrong code'
    resp_fifth = Request(*cfg['fifth_req'])
    assert resp_fifth.check_if_json(), 'not json'
    assert resp_fifth.check_code_200(), 'wrong code'
    user_with_id = resp_fifth.find_user_by_id(cfg['user_id'])
    assert resp_fifth.check_correct_user(user_with_id), 'wrong user information'
    resp_sixth = Request(*cfg['sixth_req'])
    assert resp_sixth.check_code_200(), 'wrong code'
    assert resp_sixth.check_correct_user(resp_sixth.get_json()), 'wrong user information'
