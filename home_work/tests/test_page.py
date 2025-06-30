from xml.etree.ElementTree import QName

from playwright.sync_api import Page, expect


def test_page(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    page.get_by_role("link", name="Multiple selects").click()

    place = "Ocean"
    way = "Car"
    time = "Today"

    page.locator('[name="choose_the_place_you_want_to_go"]').select_option(place)
    page.locator('[name="choose_how_you_want_to_get_there"]').select_option(way)
    page.locator('[name="choose_when_you_want_to_go"]').select_option(time)

    page.get_by_role("button", name="Submit").click()

    expect(page.locator('[id="result-text"]').first).to_have_text(f"to go by {way.lower()} to the {place.lower()} {time.lower()}")
