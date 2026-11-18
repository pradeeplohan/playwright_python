import json

import pytest

from pagesObjects.alert_popup_page import AlertPopupPage

with open('data/test_data.json') as f:
    test_data_json = json.load(f)
    print(test_data_json)
    test_data_list = test_data_json['test_data']

@pytest.fixture
def alert_popup_page(browser_setup):
    return AlertPopupPage(browser_setup)

@pytest.mark.parametrize("test_data", test_data_list)
@pytest.mark.smoke
def test_accept_alert(alert_popup_page, browser_setup, test_data):
    name = test_data['firstName']
    browser_setup.on("dialog", lambda dialog: dialog.accept())
    alert_popup_page.accept_alert(name)

@pytest.mark.parametrize("test_data", test_data_list)
def test_dismiss_alert(alert_popup_page, browser_setup, test_data):
    lastname = test_data['lastName']
   # browser_setup.on("dialog", lambda dialog: dialog.dismiss())
    alert_popup_page.dismiss_alert(lastname)
