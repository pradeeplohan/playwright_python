from playwright.sync_api import Page, expect


class ShowHidePage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.element_locator = self.page.get_by_placeholder("Hide/Show Example")
        self.hide_button_locator = self.page.get_by_role("button", name = "Hide")

    def check_visibility_of(self):
        expect(self.element_locator).to_be_visible()
        self.hide_button_locator.click()
        expect(self.element_locator).to_be_hidden()
