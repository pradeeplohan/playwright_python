import json

import pytest

from pagesObjects.frame_page import FramePage

with open('data/test_data.json') as f:
    test_data_json = json.load(f)
    test_data_list = test_data_json['test_data']

@pytest.fixture
def frame_page(browser_setup):
    return FramePage(browser_setup)

@pytest.mark.parametrize('test_data_fix', test_data_list)
@pytest.mark.smoke
def test_verify_header_title(frame_page, test_data_fix):
    header = test_data_fix['frameHeader']
    frame_page.verify_header(header)


def test_navigate_to_course_page(frame_page):
    frame_page.navigate_to_course_page()