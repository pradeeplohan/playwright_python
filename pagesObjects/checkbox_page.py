from playwright.sync_api import expect


class CheckboxPage:
    def __init__(self, page):
        self.page = page


    def checkbox_header(self):
       header = self.page.get_by_text("Checkbox Example").text_content()
       print(header)

    def verify_header(self, header):
        expect(self.page.get_by_text("Checkbox Example")).to_have_text(header)

    def checkbox_count(self):
        print(self.page.get_by_role("checkbox").count())
        expect(self.page.get_by_role("checkbox")).to_have_count(3)

    def select_checkbox(self):
        self.page.locator("#checkBoxOption2").check()
        expect(self.page.locator("#checkBoxOption2")).to_be_checked()