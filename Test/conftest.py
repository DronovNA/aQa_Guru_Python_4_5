import pytest
from selene import browser


@pytest.fixture
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def open_browser_form(window_size):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.hold_browser_open = True
