import pytest
from framework.browser.browser import Browser


@pytest.fixture(scope='session')
def pytest_session_start():
    browser = Browser()
    browser.set_url(url='https://userinyerface.com/')


@pytest.fixture(scope='session')
def pytest_session_finish(request):
    browser = Browser()
    def quit():
        browser.quit()
    request.addfinalizer(quit)
