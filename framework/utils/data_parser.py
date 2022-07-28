import json

from framework.singleton import Singleton


class DataSetParser(metaclass=Singleton):
    dataset = None

    def open_dataset(self):
        with open(r'C:\Users\User\Desktop\second_lvl\tests\test_data\test_data.json', 'r') as fd:
            self.dataset = json.load(fd)

    def get_dataset(self):
        if self.dataset is None:
            self.open_dataset()
        return self.dataset
