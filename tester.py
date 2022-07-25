from entitys.API import Request
from framework.utils.cfg_parser import ConfigParser


def test_step():
    cfg = ConfigParser().get_config()
    resp_first = Request(*cfg['first_req'])
    assert resp_first.check_code_200()
    assert resp_first.check_if_json()
    assert resp_first.check_if_sorted_by_id()
    resp_second = Request(*cfg['second_req'])
    assert resp_second.check_code_200()
    assert resp_second.check_99_post()
    resp_third = Request(*cfg['third_req'])
    assert resp_third.check_empty()
    assert resp_third.check_code_404()
    resp_fourth = Request(*cfg['fourth_req'])
    assert resp_fourth.check_correct_post_req() and resp_fourth.check_code_201()
    resp_fifth = Request(*cfg['fifth_req'])
    assert resp_fifth.check_if_json() and resp_fifth.check_code_200()
    user_with_id = resp_fifth.find_user_by_id(cfg['user_id'])
    assert resp_fifth.check_correct_user(user_with_id)
    resp_sixth = Request(*cfg['sixth_req'])
    assert resp_sixth.check_code_200()
    assert resp_sixth.check_correct_user(resp_sixth.get_json())
