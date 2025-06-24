from playwright.sync_api import Page, expect


def test_page(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    page.get_by_role("link", name="Multiple selects").click()
    page.locator('[name="choose_the_place_you_want_to_go"]').select_option("Ocean")
    page.locator('[name="choose_how_you_want_to_get_there"]').select_option("Car")
    page.locator('[name="choose_when_you_want_to_go"]').select_option("Today")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator('[id="result-text"]')).to_have_text("to go by car to the ocean today")
