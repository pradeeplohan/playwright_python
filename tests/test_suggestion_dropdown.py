import pytest

from pagesObjects.suggestion_dropdown_page import SuggestionDropdownPage


@pytest.fixture
def suggestion_dropdown_page(browser_setup):
    return SuggestionDropdownPage(browser_setup)


def test_header_verify(suggestion_dropdown_page):
    suggestion_dropdown_page.header_verify("Suggession Class Example")

def test_select_keyword(suggestion_dropdown_page):
    suggestion_dropdown_page.select_keyword("ind", "India")