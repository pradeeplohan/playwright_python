import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def browser_setup(page:Page):
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context()
    #page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    return page
    #browser.close()
    #context.close()

@pytest.fixture(scope='session')
def test_data_fix(request):
    return request.param