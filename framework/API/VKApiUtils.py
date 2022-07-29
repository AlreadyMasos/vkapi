from framework.API.API import API
from framework.utils.random_utils import create_random_string


class VKApiUtils(API):
    message = create_random_string(10)

    def create_post(self):
        access_token = self.cfg["token"]
        owner_id = self.cfg["owner_id"]
        method = 'wall.post'
        v = "5.131"
        self.post(method, access_token, owner_id, self.message, v)
        print(self.message)
        return self.get_json()['response']['post_id'], self.message
