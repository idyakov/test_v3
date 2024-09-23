from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click on support option')
def click_on_support(context):
    context.app.access_social_media.click_sprt_btn()


@when('Switch to the new tab')
def switch_to_new_tab_win(context):
    context.app.access_social_media.switch_to_new_tab_win()


@when('Verify the right tab page opens and contains {url_portion}')
def verify_new_tab_page(context, url_portion):
    context.app.access_social_media.verify_new_tab_page(url_portion)


@then('Go back')
def go_back_tab_page(context):
    context.app.access_social_media.go_back_tab_page()


@then('Click on news option')
def go_back_tab_page(context):
    context.app.access_social_media.click_news_btn()


@when('Verify the right tab telegram page opens and contains {url_portion}')
def verify_new_tab_page(context, url_portion):
    context.app.access_social_media.verify_new_telegram_tab_page(url_portion)
