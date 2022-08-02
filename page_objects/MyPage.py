from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text import Text
from framework.elements.link import Link
from framework.utils.data_parser import DataSetParser
from framework.utils.picture_utils import check_if_pics_same
import urllib3 as url


class MyPage(BasePage):
    DATA = DataSetParser().get_dataset()
    all_posts_button = Button('xpath', '//li[@class="_wall_tab_all"]', 'all_posts_button')
    link_photo = Link('xpath', f'//a[@href="/photo{DATA["owner_id"]}_{DATA["media_id"]}"]', "link")
    show_comments_button = Button('xpath', '//a[@class="replies_next replies_next_main replies_next_shown"]',
                                  'shw_cmnt_btn')
    img = Button('xpath', "//div[@id='pv_photo']//img", 'img')
    close_img = Button('xpath', '//div[@class="pv_close_btn"]', 'close_btn')

    def __init__(self):
        super().__init__(self.all_posts_button.get_search_condition(),
                         self.all_posts_button.get_locator(),
                         self.all_posts_button.get_name())

    def click_my_page_button(self):
        self.all_posts_button.click()

    def check_created_post(self, post_id):
        try:
            post_with_id = Text('xpath', f'//div[@id="wpt{self.DATA["owner_id"]}_{post_id[0]}"]',"post_with_id]")
            post_with_id.wait_for_is_visible()
            return post_with_id.is_displayed(), post_id[1] == post_with_id.get_text()
        except TimeoutError:
            return False

    def check_edited_post(self, post_info, new_message):
        try:
            post_with_id = Text('xpath', f'//div[@id="wpt{self.DATA["owner_id"]}_{post_info[0]}"]', "post_with_id]")
            post_with_id.wait_for_is_visible()
            picture_check = check_if_pics_same(r'/second_task/tests/test_data/picture.png',
                                               r'/second_task/tests/test_data/picture_original.png')
            return self.link_photo.is_displayed(), post_info[1] != new_message, picture_check
        except RuntimeError:
            return False

    def check_comment(self, comment_info):
        try:
            self.show_comments_button.wait_for_is_visible()
            self.show_comments_button.click()
            comment_text = Text('xpath', f'//div[@id="wpt{self.DATA["owner_id"]}_{comment_info[0]}"]', 'comment_text')
            return comment_text.get_text() == comment_info[1]
        except TimeoutError:
            return False

    def like_post(self, post_info):
        like_button = Button('xpath', f'//div[@data-reaction-target-object="wall{self.DATA["owner_id"]}_{post_info}"]',
                             'like_btn')
        like_button.click()

    def check_post_deleted(self, post_id):
        post = Text('xpath', f'//div[@id="post{self.DATA["owner_id"]}_{post_id}"]', 'post')
        return post.is_exist()

    def click_photo(self):
        self.link_photo.click()
        src = self.img.get_attribute('src')
        url.urlretrieve(src, r'/second_task/tests/test_data/picture_original.png')
        self.close_img.click()
