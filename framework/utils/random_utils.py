import random
import string


def create_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def random_data_generator():
    return {'body' : create_random_string(15),
            'title' : create_random_string(10)}
