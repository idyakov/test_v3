from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main_page for change_pwd')
def open_soft_reelly(context):
    context.app.main_page.open_main()


@when('Click on Subscription & payments option')
def click_subscr_payment(context):
    context.app.subscr_payment.click_subscr_payment()


@then('Verify the right page Subscription & payments opens and contains {url_portion}')
def verify_subscription(context, url_portion):
    context.app.subscr_payment.verify_subscription(url_portion)


@when('Verify the “Subscription & payments” title is visible')
def verify_click_subscr_payment(context):
    context.app.subscr_payment.verify_title_subscr_payment()


@then('Verify “back” and “upgrade plan” buttons are available')
def verify_buttons(context):
    context.app.subscr_payment.verify_buttons()
