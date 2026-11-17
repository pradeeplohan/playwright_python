from playwright.sync_api import Page, expect


class SuggestionDropdownPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.header_locator = self.page.get_by_text("Suggession Class Example")
        self.suggestion_input_locator = self.page.get_by_placeholder("Type to Select Countries")
        self.countries = self.page.locator("#ui-id-1 li")

    def header_verify(self, header_line):
       header = self.header_locator.text_content()
       print(header)
       expect(self.header_locator).to_have_text(header_line)


    def select_keyword(self, keyword, country):
        self.suggestion_input_locator.fill(keyword)

        self.countries.first.wait_for(state="visible")
        countries_list = self.countries.all_text_contents()
        print(countries_list)

        for item in range(len(countries_list)):
            if countries_list[item].strip() == country:
                self.countries.nth(item).click()
                break


        print(self.suggestion_input_locator.input_value())
        expect(self.suggestion_input_locator).to_have_value(country)
