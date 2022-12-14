import requests
from framework.utils.data_parser import DataSetParser
from framework.utils.random_utils import create_random_string
from framework.utils.chekcers import check_sorted_by, check_if_json, empty_check
from framework.utils.cfg_parser import ConfigParser


class API:
    DATA = DataSetParser().get_dataset()
    cfg = ConfigParser().get_config()

    def __init__(self):
        self._response = None

    def get(self, method, access_token, owner_id, v, post_id):
        self._response = requests.get(url=f'{self.cfg["base_url_api"]}{method}?owner_id={owner_id}&'
                                          f'access_token={access_token}&v={v}&post_id={post_id}')

    def post(self, method, access_token, owner_id, message, v, post_id='', attachment=''):
        if post_id == '':
            self._response = requests.post(url=f'{self.cfg["base_url_api"]}{method}?owner_id={owner_id}&'
                                           f'access_token={access_token}&message={message}&v={v}')
        else:
            if attachment != '':
                self._response = requests.post(url=f'{self.cfg["base_url_api"]}{method}?owner_id={owner_id}&'
                                               f'access_token={access_token}&message={message}&v={v}&post_id={post_id}'
                                               f'&attachments=photo{attachment[0]}_{attachment[1]}')
            else:
                self._response = requests.post(url=f'{self.cfg["base_url_api"]}{method}?owner_id={owner_id}&'
                                               f'access_token={access_token}&message={message}&v={v}&post_id={post_id}')

    def get_status_code(self):
        return self._response.status_code

    def get_json(self):
        return self._response.json()

    def get_text(self):
        return self._response.text

    def check_if_sorted_by_id(self):
        return check_sorted_by(self._response, 'id')

    def check_if_json(self):
        return check_if_json(self._response)

    def check_empty(self):
        return empty_check(self._response)
