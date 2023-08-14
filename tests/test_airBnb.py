import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import HomePage


@pytest.mark.sanity
def test_signin(automation_manager):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=automation_manager.browser_headless_mode)
        page = browser.new_page()
        page.goto(automation_manager.test_parameters["URL"])
        home_page = HomePage(page, automation_manager.test_parameters)
        home_page.profile_button.click()
        print("fdsfdf")