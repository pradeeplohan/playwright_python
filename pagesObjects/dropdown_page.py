from playwright.sync_api import expect


class Dropdown:

    def __init__(self, page):
        self.page = page

    def dropdown_header(self):
        header = self.page.get_by_text("Dropdown Example").text_content()
        print(header)
        return header

    def verify_header(self, header):
        expect(self.page.get_by_text("Dropdown Example")).to_have_text(header)

    def select_dropdown(self):
        self.page.get_by_role("combobox").select_option("option2")
        selected_option = self.page.get_by_role("combobox").input_value()
        print(selected_option)
        expect(self.page.get_by_role("combobox")).to_have_value("option2")