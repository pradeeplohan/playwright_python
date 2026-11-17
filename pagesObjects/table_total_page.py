import time

from playwright.sync_api import Page, expect


class TableTotalPage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.table_locator = self.page.locator(".tableFixHead")
        self.col_locator = self.page.locator("//table[@id = 'product']/thead/tr/th")
        self.rows_loc = self.page.locator("//div[@class = 'tableFixHead']/table/tbody/tr")
        self.total_amount_locator = self.page.locator(".totalAmount")

    def amount_total(self):

        self.table_locator.scroll_into_view_if_needed()
        expect(self.table_locator).to_be_visible()

        col_count = self.col_locator.count()
        total = 0

        for index in range(col_count):
            if self.col_locator.nth(index).filter(has_text="Amount").count() > 0:
                amount_col_index = index
                print("Amount col index value::", amount_col_index)

        row_count = self.rows_loc.count()
        for i in range(row_count):
            row_price = self.rows_loc.nth(i).locator("td").nth(amount_col_index).text_content()
            print(row_price)
            total += int(row_price)

        print("Total of table amount::", total)

        expected_total = int(self.total_amount_locator.text_content().split(":")[1].strip())
        print(expected_total)
        assert expected_total == total



    def scroll_table(self):
        self.table_locator.scroll_into_view_if_needed()
        self.table_locator.hover()
        self.page.mouse.wheel(0, 500)
        time.sleep(2)
        self.page.mouse.wheel(0, -200)
        time.sleep(2)





