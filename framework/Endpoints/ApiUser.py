from framework.API import API
from framework.utils.data_parser import DataSetParser
from entitys.User import User


class UserApi(API):
    DATA = DataSetParser().get_dataset()
    ENDPOINT = '/users/'

    def get_user(self):
        self.get(self.ENDPOINT)
        expected = 200
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def find_user_by_id(self, number):
        listed = self.get_json()
        return listed[int(number)-1]

    def check_correct_user_with_id(self):
        return User(self.find_user_by_id(self.DATA['user_id'])) == User(self.DATA['user'])

    def get_user_with_id(self):
        self.get(self.ENDPOINT + self.DATA['user_id'])
        expected = 200
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def check_correct_user(self):
        return User(self.get_json()) == User(self.DATA['user'])
