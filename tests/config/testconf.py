import pytest
from framework.browser.browser import Browser
from framework.utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


@pytest.fixture(scope='session')
def pytest_session_start():
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(url=CONFIG['base_url'])


@pytest.fixture(scope='session')
def pytest_session_finish(request):
    browser = Browser()
    def quit():
        browser.quit()
    request.addfinalizer(quit)
