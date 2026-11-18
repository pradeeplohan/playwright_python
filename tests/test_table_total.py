import pytest

from pagesObjects.table_total_page import TableTotalPage


@pytest.fixture
def table_total_page(browser_setup):
    return TableTotalPage(browser_setup)

@pytest.mark.smoke
def test_amount_total(table_total_page):
    table_total_page.amount_total()

def test_scroll_total(table_total_page):
    table_total_page.scroll_table()
