import requests
from framework.utils.data_parser import DataSetParser
from framework.utils.chekcers import check_sorted_by, check_if_json, check_post, empty_check
from framework.utils.random_utils import create_random_string
from entitys.Post import Post
from entitys.User import User


class Request:
    DATA = DataSetParser().get_dataset()

    def __init__(self, req_type, link):
        if req_type == 'get':
            self.resp = requests.get(link)
        if req_type == 'post':
            self.data = {'title': create_random_string(10),
                         'body': create_random_string(15),
                         'userId': '1'}
            self.resp = requests.post(link, data=self.data)

    def status_code_check(self, code_number):
        return self.resp.status_code == code_number

    def get_json(self):
        return self.resp.json()

    def check_if_sorted_by_id(self):
        return check_sorted_by(self.resp, 'id')

    def check_if_json(self):
        return check_if_json(self.resp)

    def check_99_post(self):
        real_post = Post(self.DATA['post'])
        current_post = Post(self.get_json())
        return check_post(real_post, current_post)

    def check_empty(self):
        return empty_check(self.resp)

    def check_correct_post_req(self):
        return Post(self.get_json()) == Post(self.data)

    def check_correct_user(self, user):
        return User(user) == User(self.DATA['user'])

    def find_user_by_id(self, number):
        listed = self.get_json()
        return listed[number-1]
