from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main_page for guide')
def open_soft_reelly(context):
    context.app.title_verification.open_main()


@when('Click on User Guide option')
def click_search_icon(context):
    context.app.title_verification.click_on_user_guide()


@then('Verify the right page user_guide opens and contains {url_portion}')
def verify_contact_tab_page(context, url_portion):
    context.app.title_verification.verify_title_page(url_portion)


@then('Verify all lesson videos contain titles')
def verify_social_media_icons(context):
    context.app.title_verification.verify_all_lesson()
