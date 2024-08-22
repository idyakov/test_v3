from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main_page')
def open_soft_reelly(context):
    context.app.main_page.open_main()


@given('Log in to the main page')
def input_credentials(context):
    context.app.login_page.input_credentials()


@given('Click on continue button')
def click_search_icon(context):
    context.app.login_page.click_sign_in()


@when('Click on settings open')
def click_on_settings(context):
    context.app.login_page.click_on_settings()


@when('Click on Community option')
def click_on_community(context):
    context.app.community_page.click_on_community()


@then('Verify expected URLVerify the right page opens')
def verify_page(context):
    context.app.community_page.verify_expected_page()


@then('Verify “Contact support” button is available and clickable')
def contact_support_button_verification(context):
    context.app.community_page.contact_support_button_verification()


@then('Verify the right_page opens and contains {url_portion}')
def verify_new_tab_page(context, url_portion):
    expected_url = f'https://soft.reelly.io/{url_portion}'
    context.app.community_page.verify_expected_page(expected_url, url_portion)


@then('Verify “Telegram_english_chat” button is available and clickable')
def contact_support_button_verification(context):
    context.app.community_page.join_english_button_verification()


@then('Verify “Telegram_russian_chat” button is available and clickable')
def contact_support_button_verification(context):
    context.app.community_page.join_russian_button_verification()
