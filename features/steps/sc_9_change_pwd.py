from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main_page for change_pwd')
def open_soft_reelly(context):
    context.app.main_page.open_main()


@when('Click on change password')
def click_change_pwd(context):
    context.app.change_pwd.click_change_pwd()


@then('Verify the right page "set-new-password" opens and contains {url_portion}')
def verify_contact_tab_page(context, url_portion):
    context.app.change_pwd.verify_change_pwd(url_portion)


@then('Add some test password to the input fields')
def input_test_pwd(context):
    context.app.change_pwd.input_test_pwd()


@then('Verify the “Change password” button is available')
def pwd_btn_verification(context):
    context.app.change_pwd.pwd_btn_verification()
