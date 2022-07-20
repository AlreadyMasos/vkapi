import autoit

from framework.utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


class AutoItUtils:
    def __init__(self):
        self.wait_timeout = CONFIG['autoit_wait_sec']

    def upload_image(self):
        autoit.win_wait_active(CONFIG['win_handle'], self.wait_timeout)
        autoit.control_focus(CONFIG['win_handle'], "")
        autoit.control_set_text(CONFIG['win_handle'], "Edit1", CONFIG['pic_path'])
        autoit.control_click(CONFIG['win_handle'], "Button1")
        autoit.win_wait_not_active(CONFIG['win_handle'], self.wait_timeout)

