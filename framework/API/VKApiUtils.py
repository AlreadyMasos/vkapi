from framework.API.API import API
from framework.utils.random_utils import create_random_string


class VKApiUtils(API):

    first_message = create_random_string(10)
    second_message = create_random_string(15)
    comment = create_random_string(20)
    access_token = API.cfg["token"]
    owner_id = API.cfg["owner_id"]
    method_post_create = 'wall.post'
    method_post_edit = 'wall.edit'
    method_comment_create = 'wall.createComment'
    method_get_likes = 'wall.getLikes'
    method_delete_post = 'wall.delete'
    v = "5.131"

    def create_post(self):
        self.post(self.method_post_create, self.access_token, self.owner_id, self.first_message, self.v)
        return self.get_json()['response']['post_id'], self.first_message

    def edit_post(self, post_id, attachment=(API.cfg['owner_id'], API.cfg['media_id'])):
        self.post(self.method_post_edit, self.access_token, self.owner_id, self.second_message, self.v, post_id,
                  attachment)
        return self.second_message

    def create_post_comment(self, post_id):
        self.post(self.method_comment_create, self.access_token, self.owner_id, self.comment, self.v, post_id)
        return self.get_json()['response']['comment_id'], self.comment

    def check_like(self, post_id):
        self.get(self.method_get_likes, self.access_token, self.owner_id, self.v, post_id)
        return (self.get_json()['response']['count'] == 1 and
                int(self.cfg['owner_id']) == self.get_json()['response']['users'][0]['uid'])

    def delete_post(self, post_id):
        self.post(self.method_delete_post, self.access_token, self.owner_id, v=self.v, post_id=post_id, message='')
        return self.get_json()['response'] == 1
