from playwright.sync_api import Page, expect


class FramePage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.header_locator = self.page.get_by_text("iFrame Example")
        self.frame_loc = self.page.frame_locator("#courses-iframe")
        self.courses_loc = self.frame_loc.get_by_role("link", name = "All Access plan")
        self.verify_text_loc = self.frame_loc.locator("//div[@class='text']/p[1]")
       # self.page.locator("[data-heap-producttype='course']")

    def verify_header(self, header):
        expect(self.header_locator).to_have_text(header)

    def navigate_to_course_page(self):
        self.courses_loc.click()
        verify_text = self.verify_text_loc.text_content().split("to")[0].split("Get")[1].strip()
        print(verify_text)
