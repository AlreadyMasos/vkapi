from framework.API.API import API
from framework.utils.random_utils import create_random_string


class VKApiUtils(API):
    message = create_random_string(10)
    access_token = API.cfg["token"]
    owner_id = API.cfg["owner_id"]
    method_post_create = 'wall.post'
    method_post_edit = 'wall.edit'
    v = "5.131"

    def create_post(self):
        self.post(self.method_post_create, self.access_token, self.owner_id, self.message, self.v)
        print(self.message)
        return self.get_json()['response']['post_id'], self.message

    def edit_post(self, post_id):
        new_data = create_random_string(15)
        self.post(self.method_post_edit, self.access_token, self.owner_id, new_data, self.v, post_id)
        print(self.get_text())
        print(new_data)

