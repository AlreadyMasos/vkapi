from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text import Text
from framework.elements.link import Link
from framework.utils.cfg_parser import ConfigParser


class MyPage(BasePage):
    cfg = ConfigParser().get_config()
    all_posts_button = Button('xpath', '//li[@class="_wall_tab_all"]', 'all_posts_button')

    def __init__(self):
        super().__init__(self.all_posts_button.get_search_condition(),
                         self.all_posts_button.get_locator(),
                         self.all_posts_button.get_name())

    def click_my_page_button(self):
        self.all_posts_button.click()

    def check_created_post(self, post_id):
        try:
            post_with_id = Text('xpath', f'//div[@id="wpt{self.cfg["owner_id"]}_{post_id[0]}"]',"post_with_id]")
            post_with_id.wait_for_is_visible()
            assert post_id[1] == post_with_id.get_text(), 'wrong post text'
            return post_with_id.is_displayed() and post_id[1] == post_with_id.get_text()
        except TimeoutError:
            return False

    def check_edited_post(self, post_info, new_message):
        try:
            post_with_id = Text('xpath', f'//div[@id="wpt{self.cfg["owner_id"]}_{post_info[0]}"]', "post_with_id]")
            post_with_id.wait_for_is_visible()
            link_photo = Link('xpath', f'//a[@href="/photo{self.cfg["owner_id"]}_{self.cfg["media_id"]}"]',"link")
            assert post_info[1] != new_message, 'wrong post text after edit'
            return link_photo.is_displayed() and post_info[1] != new_message
        except RuntimeError:
            return False

    def check_comment(self, comment_info):
        try:
            show_comments_button = Button('xpath', '//a[@class="replies_next replies_next_main replies_next_shown"]',
                                          'shw_cmnt_btn')
            show_comments_button.wait_for_is_visible()
            show_comments_button.click()
            comment_text = Text('xpath', f'//div[@id="wpt{self.cfg["owner_id"]}_{comment_info[0]}"]', 'comment_text')
            assert comment_text.get_text() == comment_info[1], 'wrong comment text'
            return comment_text.get_text() == comment_info[1]
        except TimeoutError:
            return False

    def like_post(self, post_info):

        like_button = Button('xpath', f'//div[@data-reaction-target-object="wall{self.cfg["owner_id"]}_{post_info}"]',
                             'like_btn')
        like_button.click()

    def check_post_deleted(self, post_id):
        post = Text('xpath', f'//div[@id="post{self.cfg["owner_id"]}_{post_id}"]', 'post')
        return post.is_exist()
