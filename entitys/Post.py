

class Post:

    def __init__(self, json):
        self.user_id = json['userId']
        self.title = json['title']
        self.body = json['body']

    def __eq__(self, other):
        return (self.title == other.title
                and self.body == other.body
                and self.user_id == other.user_id)
