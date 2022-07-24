import requests
from utils.chekcers import check_sorted_by

class API:

    def __init__(self, req_type, link, data=None):
        if req_type == 'get':
            self.resp = requests.get(link)
        if req_type == 'post':
            self.resp = requests.post(link, data=data)

    def status_code_check(self, code_number):
        return self.resp.status_code == code_number

    def check_if_sorted(self, param):
        return check_sorted_by(self.resp, param)

    def check_if_json(self):
