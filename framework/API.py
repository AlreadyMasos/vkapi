import requests
from framework.utils.data_parser import DataSetParser
from framework.utils.chekcers import check_sorted_by, check_if_json, empty_check
from framework.utils.cfg_parser import ConfigParser


class API:
    DATA = DataSetParser().get_dataset()
    cfg = ConfigParser().get_config()

    def __init__(self):
        self._response = None

    def get(self, endpoint):
        self._response = requests.get(url=self.cfg['base_url' + endpoint])

    def post(self, endpoint, data=None):
        self._response = requests.post(url=self.cfg['base_url']+endpoint, data=data.__dict__)

    def get_status_code(self):
        return self._response.status_code

    def get_json(self):
        return self._response.json()

    def check_if_sorted_by_id(self):
        return check_sorted_by(self._response, 'id')

    def check_if_json(self):
        return check_if_json(self._response)

    def check_empty(self):
        return empty_check(self._response)
