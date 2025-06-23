import re
from playwright.sync_api import Page, expect, BrowserContext, APIRequestContext


# struecture
#
# Playwright
# Browser + Context
# Page - tab inside browser - Incognito mode


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    (expect(page.get_by_role("heading", name="Installation")).to_be_visible())


def test_example(page: Page, context: BrowserContext, api_context: APIRequestContext):
    page.goto("https://playwright.dev/")
    context.storage_state() # to save cookies
    context.clear_cookies() # to clear the cookies

    # same thing in API requests. in Page can do that.
    # page.request.get("https://playwright.dev/")
    # api_context.get("https://playwright.dev/")




    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    (expect(page.get_by_role("heading", name="Installation")).to_be_visible())
