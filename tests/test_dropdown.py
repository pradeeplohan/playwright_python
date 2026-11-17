import pytest
from playwright.sync_api import Playwright

from pagesObjects.dropdown_page import Dropdown


@pytest.fixture
def dropdown_page(browser_setup):
    return Dropdown(browser_setup)

def test_dropdown1(dropdown_page):
    header = dropdown_page.dropdown_header()

def test_verify_header(dropdown_page):
    header = "Dropdown Example"
    dropdown_page.verify_header(header)

def test_select_dropdown(dropdown_page):
    dropdown_page.select_dropdown()