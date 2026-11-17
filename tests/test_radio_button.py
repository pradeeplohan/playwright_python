import pytest
from playwright.sync_api import Playwright

from pagesObjects.radio_page import radioButtonPage

@pytest.fixture
def radio_button_page(browser_setup):
    return radioButtonPage(browser_setup)


def test_radio_button1(playwright: Playwright, browser_setup, radio_button_page):
   # radio_button_page.open_url()
    button_header = radio_button_page.get_radio_button_header()
    radio_button_page.verify_radio_button_header(button_header)
    radio_button_page.radio_button_count()

def test_select_radio_button2(playwright: Playwright, browser_setup, radio_button_page):
    radio_button_page.select_button()

