from framework.API import API
from framework.utils.data_parser import DataSetParser
from entitys.User import User


class UserApi(API):
    DATA = DataSetParser().get_dataset()
    ENDPOINT = 'users/'

    def get_user(self):
        self.get(self.ENDPOINT)
        expected = 200
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def find_user_by_id(self, number):
        listed = self.get_json()
        return listed[number-1]

    def check_correct_user(self, user):
        return User(user) == User(self.DATA['user'])
