from playwright.sync_api import Page


class AlertPopupPage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.enter_name_locator = self.page.get_by_placeholder("Enter Your Name")
        self.alert_locator = self.page.get_by_role("button", name = "Alert")
        self.confirm_locator = self.page.get_by_role("button", name = "Confirm")

    def accept_alert(self, name):
        self.enter_name_locator.fill(name)
        self.alert_locator.click()

    def dismiss_alert(self, name):
        self.enter_name_locator.fill(name)
        dialog_message = []

        def handle_dialog(dialog):
            dialog_message.append(dialog.message)
            dialog.dismiss()

        self.page.on("dialog", handle_dialog)
        self.confirm_locator.click()

        print("Alert message::",dialog_message[0])

        expected_message = f"Hello {name}, Are you sure you want to confirm?"

        assert dialog_message[0] == expected_message



