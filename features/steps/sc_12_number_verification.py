from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Verify the right page opens and contains {url_portion}')
def verify_right_tab_page(context, url_portion):
    context.app.number_options_verification.verify_right_tab_page(url_portion)


@when('Verify there are 12 options for the settings')
def verify_numbers_options(context):
    context.app.number_options_verification.verify_numbers_options()


@when('Verify “connect the company” button is available')
def verify_connect_button(context):
    context.app.number_options_verification.verify_connect_button()
