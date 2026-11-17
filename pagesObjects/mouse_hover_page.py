import time

from playwright.sync_api import Page, expect


class MouseHoverPage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.header_locator = self.page.get_by_text("Mouse Hover Example")
        self.mouse_hover_locator = self.page.get_by_role("button", name ="Mouse Hover")
        self.top_locator = self.page.get_by_role("link", name = "Top")


    def verify_header(self, header):
        expect(self.header_locator).to_have_text(header)

    def select_top(self):
        self.mouse_hover_locator.hover()
        time.sleep(2)
        self.top_locator.click()

