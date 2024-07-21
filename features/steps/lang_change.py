from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open soft.reelly page main page')
def open_soft_reelly(context):
    context.app.main_page.open_main()
    sleep(5)


@given('Login to the soft.reelly page')
def input_credentials(context):
    context.app.login_page.input_credentials()


@given('Click on continue button of the login page')
def click_search_icon(context):
    context.app.login_page.click_sign_in()


@given('Click on menu')
def click_on_menu(context):
    context.app.login_page.click_on_main_menu()


@given('Change the language of the main page')
def dropdown_language(context):
    context.app.base_page.change_language()


@given('Verify the languange has changed')
def verify_menu_title(context):
    context.app.base_page.verify_menu_title()
