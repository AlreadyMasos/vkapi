from framework.API.API import API
from framework.utils.random_utils import create_random_string
from framework.utils.data_parser import DataSetParser

class VKApiUtils(API):

    FIRST_MESSAGE = create_random_string(10)
    SECOND_MESSAGE = create_random_string(15)
    COMMENT = create_random_string(20)
    ACCESS_TOKEN = API.cfg["token"]
    OWNER_ID = API.cfg["owner_id"]
    METHOD_POST_CREATE = 'wall.post'
    METHOD_POST_EDIT = 'wall.edit'
    METHOD_COMMENT_CREATE = 'wall.createComment'
    METHOD_GET_LIKES = 'wall.getLikes'
    METHOD_DELETE_POST = 'wall.delete'
    VERSION = "5.131"

    def create_post(self):
        self.post(self.METHOD_POST_CREATE, self.ACCESS_TOKEN, self.OWNER_ID, self.FIRST_MESSAGE, self.VERSION)
        return self.get_json()['response']['post_id'], self.FIRST_MESSAGE

    def edit_post(self, post_id, attachment=(API.DATA['owner_id'], API.DATA['media_id'])):
        self.post(self.METHOD_POST_EDIT, self.ACCESS_TOKEN, self.OWNER_ID, self.SECOND_MESSAGE,
                  self.VERSION, post_id, attachment)
        return self.SECOND_MESSAGE

    def create_post_comment(self, post_id):
        self.post(self.METHOD_COMMENT_CREATE, self.ACCESS_TOKEN, self.OWNER_ID, self.COMMENT, self.VERSION, post_id)
        return self.get_json()['response']['comment_id'], self.COMMENT

    def check_like(self, post_id):
        self.get(self.METHOD_GET_LIKES, self.ACCESS_TOKEN, self.OWNER_ID, self.VERSION, post_id)
        return (self.get_json()['response']['count'] == 1 and
                int(self.cfg['owner_id']) == self.get_json()['response']['users'][0]['uid'])

    def delete_post(self, post_id):
        self.post(self.METHOD_DELETE_POST, self.ACCESS_TOKEN, self.OWNER_ID,
                  v=self.VERSION, post_id=post_id, message='')
        return self.get_json()['response'] == 1
