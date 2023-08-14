from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page, test_params) -> None:
        self.test_params = test_params
        self.page = page

        # button
        self.profile_button = page.locator('data-testid=cypress-headernav-profile')
        self.login_button = page.locator('data-testid=cypress-headernav-login')
        self.signup_button = page.locator('data-testid=cypress-headernav-signup')
