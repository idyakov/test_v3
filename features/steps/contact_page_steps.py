from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click on Contact us option')
def click_search_icon(context):
    context.app.contact_page.click_on_contact_us()


@then('Verify the right page opens and contains {url_portion}')
def verify_contact_tab_page(context, url_portion):
    context.app.contact_page.verify_contact_tab_page()


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.contact_page.count_social_media_icons()


@then('Verify “Connect the company” button is available and clickable')
def connect_company_button_verification(context):
    context.app.contact_page.connect_the_company_button_verification()
