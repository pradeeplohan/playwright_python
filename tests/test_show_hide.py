import pytest

from pagesObjects.show_hide_page import ShowHidePage


@pytest.fixture
def show_hide_page(browser_setup):
    return ShowHidePage(browser_setup)

def test_check_visibility_of_ele(show_hide_page):
    show_hide_page.check_visibility_of()