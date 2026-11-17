import time

import pytest
from playwright.sync_api import expect




class radioButtonPage:

    def __init__(self, page):
        self.page = page

    def open_url(self):
        self.page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    def get_radio_button_header(self):
        button_header = self.page.get_by_text("Radio Button Example").text_content()
        print("Radio Button header::", button_header)
        return button_header


    def verify_radio_button_header(self, button_header):
        expect(self.page.get_by_text("Radio Button Example")).to_contain_text(button_header)

    def radio_button_count(self):
        print("Count of radio buttons::",self.page.locator("//div[@id='radio-btn-example']/fieldset/label").count())

    def select_button(self):
        self.page.locator("input[value='radio2']").check()
        self.page.locator("input[value='radio2']").screenshot(path="screenshot/file1.png")
        expect(self.page.locator("input[value='radio2']")).to_be_checked()


