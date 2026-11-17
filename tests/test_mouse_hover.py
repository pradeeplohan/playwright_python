import json

import pytest

from pagesObjects.mouse_hover_page import MouseHoverPage

with open('data/test_data.json') as f:
    test_data_json = json.load(f)
    test_data_list = test_data_json['test_data']

@pytest.fixture
def mouse_hover_page(browser_setup):
    return MouseHoverPage(browser_setup)

@pytest.mark.parametrize('test_data_fix', test_data_list, indirect=True)
def test_verify_header_title(mouse_hover_page, test_data_fix):
    header = test_data_fix['mouseHoverHeader']
    mouse_hover_page.verify_header(header)

def test_select_top(mouse_hover_page):
    mouse_hover_page.select_top()