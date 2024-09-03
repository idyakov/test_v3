from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Subscription(Page):
    SUB_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Subscription & payments')]")
    BACK_BTN = (By.XPATH, "//div[contains(@class, 'next-step-- black') and contains(., '<- Back')]")
    UPGRD_BTN = (By.XPATH, "//div[contains(@class, 'next-step--') and contains(., 'Upgrade plan')]")
    TTL_SUB = (
    By.XPATH, "//div[contains(@class, 'lotion-your-h3--price size') and contains(., 'Subscription & payments')]")

    def verify_subscription(self, expected_url_portion):
        expected_base_pwd_url = 'https://soft.reelly.io/subscription'
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

    def verify_title_subscr_payment(self):
        subscr_payment_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.TTL_SUB)
        )
        is_subscr_payment_button_visible = subscr_payment_button.is_displayed()
        print(
            f'The "Subscription & payments" button is visible. No error: {is_subscr_payment_button_visible}')

    def verify_buttons(self):
        connect_the_comp_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.UPGRD_BTN)
        )
        is_subscr_payment_button_clickable = connect_the_comp_button.is_enabled() and connect_the_comp_button.is_displayed()
        print(
            f'The "back" and "upgrade plan" buttons are available and clickable. No error: {is_subscr_payment_button_clickable}')

    def click_subscr_payment(self):
        self.click(*self.SUB_BTN)
