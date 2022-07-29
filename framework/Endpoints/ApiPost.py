from framework.API.API import API
from framework.utils.data_parser import DataSetParser
from framework.utils.random_utils import random_data_generator
from entitys.Post import Post


class PostApi(API):
    DATA = DataSetParser().get_dataset()
    ENDPOINT = '/posts/'
    data = random_data_generator()

    def get_posts(self):
        self.get(self.ENDPOINT)
        expected = 200
        real = self.get_status_code()
        assert real == expected, f'{real} != {expected}'

    def get_post_99(self):
        self.get(self.ENDPOINT + '99')

    def get_post_150(self, status_code=400):
        self.get(self.ENDPOINT + '150')
        real = self.get_status_code()
        assert real == status_code, f'{real} != {status_code}'

    def check_99_post(self):
        real_post = Post(self.DATA['post'])
        current_post = Post(self.get_json())
        return real_post == current_post

    def check_correct_post_req(self):
        return Post(self.get_json()) == Post(self.data)

    def create_post(self):
        self.post(self.ENDPOINT, data=self.data)
