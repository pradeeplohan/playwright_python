from playwright.sync_api import Locator, Page, Response


class AutomationPracticePage:
    URL = "https://rahulshettyacademy.com/AutomationPractice/#"
    LINK_NAMES = ("REST API", "SoapUI", "Appium", "JMeter")

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> Response | None:
        return self.page.goto(self.URL, wait_until="domcontentloaded")

    def scroll_to_bottom(self) -> None:
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def link(self, name: str) -> Locator:
        return self.page.get_by_role("link", name=name, exact=True)

    def get_target_links(self) -> dict[str, str | None]:
        return {
            name: self.link(name).get_attribute("href")
            for name in self.LINK_NAMES
        }
