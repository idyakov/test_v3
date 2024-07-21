from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open soft.reelly main page')
def open_soft_reelly(context):
    context.app.main_page.open_main()
    sleep(5)


@given('Login to the main page')
def input_credentials(context):
    context.app.login_page.input_credentials()


@given('Click on continue button__')
def click_search_icon(context):
    context.app.login_page.click_sign_in()


@given('Store original window page')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print("Current:", context.original_window)
    print('All windows: ', context.driver.window_handles)


@given('Click on “Connect the company” button')
def click_on_page_company(context):
    context.app.login_page.click_on_page_company()


@given('Switch to new window page')
def click_on_page_company(context):
    context.app.login_page.switch_to_new_window()


@given('Verify the right tab open page')
def verify_new_tab_page(context):
    expected_url = 'https://soft.reelly.io/book-presentation'
    actual_url = context.app.login_page.verify_new_tap_page(expected_url)
    assert actual_url == expected_url, f"Expected URL {expected_url}, but got {actual_url}"


@given('Close the current main page and switch back')
def close_and_switch_back(context):
    # Close the current window
    context.driver.close()
    # Switch back to the original window
    context.driver.switch_to.window(context.original_window)
