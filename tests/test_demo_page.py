from playwright.sync_api import Page, expect

base_url = "https://devexpress.github.io/testcafe/example/"

# def test_demo_page_loaded(page: Page):
#     page.goto(base_url)
#     print(page.url)
#     # assert page.url == base_url+"/home-page" - failed immediately
#     # expect(page).to_have_url(base_url+"/home-page", timeout=7500) # try to do it, until the timeout -> 7.5 secondes
#     expect(page).to_have_url(base_url, timeout=7500)
#
#
# def test_demo_page_title(page: Page):
#     page.goto(base_url)
#     expect(page).to_have_title("TestCafe Example Page")


def test_user_name_presented(page: Page):
    page.goto(base_url)
    name = "Dvora Hirshaut"
    i=3

    #fill only in input or texteara
    #press_sequentially no matter what the type.
    page.locator("#developer-name").press_sequentially(name, delay=30)

    page.get_by_test_id("remote-testing-checkbox").check()
    page.get_by_test_id("reusing-js-code-checkbox").check()
    page.get_by_test_id("parallel-testing-checkbox").uncheck()
    page.get_by_test_id("ci-checkbox").uncheck()
    page.get_by_test_id("analysis-checkbox").check()


    expect(page.locator("header h1")).to_have_text("Example")
    expect(page.locator(".main-content header p").first).to_contain_text("This webpage is used as a sample in TestCafe tutorials.")


    page.get_by_test_id("windows-radio").check()
    page.locator('select#preferred-interface').select_option("JavaScript API")

    page.locator('[name="tried-test-cafe"]').check()
    if page.locator('[name="tried-test-cafe"]').is_checked():
        page.locator('[class="ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"]').focus()
        page.locator('[class="ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"]').click(position={"x": 650, "y": 5})



    page.wait_for_timeout(3000)
    page.get_by_test_id("comments-area").fill("This is comment area")

    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_test_id("thank-you-header")).to_contain_text(f"Thank you, {name}")
    expect(page).to_have_url(f"{base_url}thank-you.html")
    expect(page.locator(".result-content p").first).to_have_text(f"To learn more about TestCafe, please visit:\ndevexpress.github.io/testcafe")

    page.wait_for_timeout(3000)

