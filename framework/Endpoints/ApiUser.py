from framework.API.API import API
from framework.utils.data_parser import DataSetParser
from entitys.User import User


class UserApi(API):
    DATA = DataSetParser().get_dataset()
    ENDPOINT = '/users/'
    user_id = DATA['user_id']

    def get_user(self, status_code=200):
        self.get(self.ENDPOINT)
        real = self.get_status_code()
        assert real == status_code, f'{real} != {status_code}'

    def find_user_by_id(self, number):
        listed = self.get_json()
        return listed[int(number)-1]

    def check_correct_user_with_id(self, user_id=user_id):
        return User(self.find_user_by_id(user_id)) == User(user_id)

    def get_user_with_id(self, user_id=user_id, status_code=200):
        self.get(self.ENDPOINT + user_id)
        actual_code = self.get_status_code()
        assert actual_code == status_code, f'{actual_code} != {status_code}'

    def check_correct_user(self):
        return User(self.get_json()) == User(self.DATA['user'])
