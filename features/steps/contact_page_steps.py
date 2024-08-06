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
    expected_url = 'https://soft.reelly.io/contact-us'
    actual_url_page = context.app.contact_page.verify_contact_tab_page(expected_url)
    assert actual_url_page == expected_url, f"Expected URL {expected_url}, but got {actual_url_page}"
    print(f"Successfully verified the community page with '{url_portion}' content")
    actual_url = context.driver.current_url
    assert actual_url.startswith(actual_url), f"URL does not start with {actual_url}"
    assert url_portion.lower() in actual_url.lower(), f"URL does not contain '{url_portion}'"


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    icon_count = context.app.contact_page.count_social_media_icons()
    assert icon_count >= 4, f"Expected at least 4 social media icons, but found {icon_count}"
    print(f"Found {icon_count} social media icons")


@then('Verify “Connect the company” button is available and clickable')
def connect_company_button_verification(context):
    context.app.contact_page.connect_the_company_button_verification()



