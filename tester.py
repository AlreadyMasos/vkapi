import requests
from utils.chekcers import check_if_json, check_sorted_by


def test_step():
    resp = requests.get('https://jsonplaceholder.typicode.com/posts/')
    #assert check_if_json(resp), 'not json'
    assert check_sorted_by(resp.json(), 'id')
