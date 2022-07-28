from framework.utils.autoit_utils import AutoItUtils


class Steps:

    @staticmethod
    def upload_image():
        auto = AutoItUtils()
        auto.upload_image()
