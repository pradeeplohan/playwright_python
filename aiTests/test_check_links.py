from playwright.sync_api import Page, expect

from aipageObjects.automation_practice_page import AutomationPracticePage


def test_footer_links_return_200(page: Page) -> None:
    practice_page = AutomationPracticePage(page)
    response = practice_page.open()
    assert response is not None and response.status == 200

    practice_page.scroll_to_bottom()
    links = practice_page.get_target_links()

    assert set(links) == set(practice_page.LINK_NAMES)
    for name, href in links.items():
        link = practice_page.link(name)
        expect(link).to_be_visible()
        assert href, f"{name} link has no destination"

        link_response = page.request.get(href, timeout=60_000)
        assert link_response.status == 200, (
            f"{name} link returned HTTP {link_response.status}: {href}"
        )
