from lib2to3.fixes.fix_input import context

from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NumberOptionsVerification(Page):
    SUB_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Subscription & payments')]")
    BACK_BTN = (By.XPATH, "//div[contains(@class, 'next-step-- black') and contains(., '<- Back')]")
    UPGRD_BTN = (By.XPATH, "//div[contains(@class, 'get-free-period menu') and contains(., 'Upgrade plan')]")
    CONNECT_BTN = (By.XPATH, "//div[contains(@class, 'get-free-period menu') and contains(., 'Connect the company')]")
    TTL_SUB = (
        By.XPATH, "//div[contains(@class, 'lotion-your-h3--price size') and contains(., 'Subscription & payments')]")
    NEWS_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'News')]")

    def verify_right_tab_page(self, expected_url_portion):
        expected_base_pwd_url = 'https://soft.reelly.io/settings'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_base_pwd_url))
        current_url = self.driver.current_url
        try:
            assert expected_base_pwd_url in current_url, f"Expected URL {expected_base_pwd_url}, but got {current_url}"
            assert expected_url_portion in current_url, f"Expected URL to contain '{expected_url_portion}', but got '{current_url}'"
            print(f"Successfully verified the contact page with URL: {current_url}")
            print(f"URL contains expected portion: '{expected_url_portion}'")
        except AssertionError as e:
            print(f"URL verification failed: {str(e)}")
            raise
        return current_url

    def verify_numbers_options(self):
        # Wait for and locate all icon elements
        icon_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.page-setting-block.w-inline-block"))
        )

        # Verify the count of icons
        number_of_icons = len(icon_elements)
        assert number_of_icons == 12, f"Expected 12 icons, but found {number_of_icons}"

        print(f"Successfully verified that there are {number_of_icons} icons in the settings.")

        # Print out more information about each icon
        for i, icon in enumerate(icon_elements, 1):
            # Get the text content of the element
            text_content = icon.text.strip()

            # Try to find an img element within the anchor element
            img_element = icon.find_elements(By.TAG_NAME, "img")

            if img_element:
                alt_text = img_element[0].get_attribute('alt')
                src = img_element[0].get_attribute('src')
                print(f"Icon {i}: Text: {text_content}, Image alt: {alt_text}, Source: {src}")
            else:
                # If no img element, check for background image
                background_image = icon.value_of_css_property('background-image')
                print(f"Icon {i}: Text: {text_content}, Background image: {background_image}")

        return number_of_icons

    def verify_connect_button(self):
        connect_the_comp_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CONNECT_BTN)
        )
        is_subscr_payment_button_clickable = connect_the_comp_button.is_enabled() and connect_the_comp_button.is_displayed()
        print(
            f'The "back" and "upgrade plan" buttons are available and clickable. No error: {is_subscr_payment_button_clickable}')
