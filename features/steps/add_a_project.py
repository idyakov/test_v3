from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Click on Add a project')
def click_search_icon(context):
    context.app.login_page.click_add_project()


@given('Add test information to the input fields')
def input_project_info(context):
    context.app.login_page.input_project_info()
    sleep(3)


@given('Verify the right information is present in the input field')
def input_field_verification(context):
    context.app.login_page.input_field_verification()
    sleep(3)


@then('Verify _Send an application_ button is available and clickable')
def send_application_button_verification(context):
    context.app.login_page.send_application_button_verification()
    sleep(3)
