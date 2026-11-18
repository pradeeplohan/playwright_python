import os

from playwright.sync_api import Page

from aipageObjects.login_page import LoginPage


def test_login(page: Page) -> None:
    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")
    assert username, "LOGIN_USERNAME must be set in the environment"
    assert password, "LOGIN_PASSWORD must be set in the environment"

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    login_page.expect_logged_in()
