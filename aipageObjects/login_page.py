import re

from playwright.sync_api import Locator, Page, expect


class LoginPage:
    URL = "https://rahulshettyacademy.com/client/#/auth/login"

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def username_input(self) -> Locator:
        return self.page.locator("#userEmail")

    @property
    def password_input(self) -> Locator:
        return self.page.locator("#userPassword")

    @property
    def login_button(self) -> Locator:
        return self.page.locator("#login")

    @property
    def sign_out_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign Out", exact=True)

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_logged_in(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/client/#/dashboard/.*"))
        expect(self.sign_out_button).to_be_visible()
