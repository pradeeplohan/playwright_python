import pytest

from pagesObjects.checkbox_page import CheckboxPage


@pytest.fixture
def checkbox_page(browser_setup):
    return CheckboxPage(browser_setup)


@pytest.mark.smoke
def test_checkbox(checkbox_page):
    checkbox_page.checkbox_header()

@pytest.mark.smoke
def test_verify_header(checkbox_page):
    checkbox_page.verify_header("Checkbox Example")

@pytest.mark.smoke
def test_checkbox_count(checkbox_page):
    checkbox_page.checkbox_count()

def test_select_checkbox(checkbox_page):
    checkbox_page.select_checkbox()