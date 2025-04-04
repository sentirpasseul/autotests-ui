import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.registration_page import RegistrationPage
from time import sleep

@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email", "username", "password",
    [
        ('user.name@gmail.com'),
        ('username'),
        ('password')
    ]
)
def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')

    chromium_page.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        page.wait_for_timeout(5000)


