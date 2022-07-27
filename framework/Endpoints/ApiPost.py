from framework.API import API
from framework.utils.data_parser import DataSetParser
from framework.utils.random_utils import random_data_generator
from entitys.Post import Post


class PostApi(API):
    DATA = DataSetParser().get_dataset()
    ENDPOINT = 'posts/'
    data = random_data_generator()

    def get_post(self):
        self.get(self.ENDPOINT)
        expected = 200
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def get_post_99(self):
        self.get(self.ENDPOINT + '99')

    def get_post_150(self):
        self.get(self.ENDPOINT + '150')
        expected = 404
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def check_99_post(self):
        real_post = Post(self.DATA['post'])
        current_post = Post(self.get_json())
        return real_post == current_post

    def check_correct_post_req(self):
        expected = 201
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'
        return Post(self.get_json()) == Post(self.data)
