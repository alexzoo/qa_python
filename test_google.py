import pytest
from selene import have
from selene.support.shared import browser


def test_google_should_find():
    browser.open('https://google.com')

    query = browser.element('[name="q"]')
    query.type('Selene ui').press_enter()

    browser.element('#res').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


@pytest.fixture()
def change_resolution():
    browser.driver.set_window_size(800, 600)
