import requests
from utils.chekcers import check_sorted_by, check_if_json, check_post, empty_check
from utils.random_utils import create_random_string
from Post import Post


class Request:

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

    def check_if_sorted(self, param):
        return check_sorted_by(self.resp, param)

    def check_if_json(self):
        return check_if_json(self.resp)

    def check_post(self):
        real_post = Post({'userId': 10, 'title':'temporibus sit alias delectus eligendi possimus magni',
                          'body':'quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia'})
        current_post = Post(self.get_json())
        return check_post(real_post, current_post)

    def check_empty(self):
        return empty_check(self.resp)

    def check_correct_post(self):
        return Post(self.resp.json()) == Post(self.data)
