from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Change_pwd(Page):
    USER_GUIDE = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'User guide')]")
    CHANG_PWD = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Change password')]")
    INPUT_PWD_FIELD = (By.CSS_SELECTOR, '[id="Enter-new-password"]')
    INPUT_PWD_FIELD_RPT = (By.CSS_SELECTOR, '[id="Repeat-password"]')
    PWD_BTN = (By.XPATH, "//a[contains(@class, 'submit-button-2 w-button') and contains(., 'Change password')]")

    def click_change_pwd(self):
        self.click(*self.CHANG_PWD)

    def verify_change_pwd(self, expected_url_portion):
        expected_base_pwd_url = 'https://soft.reelly.io/set-new-password'
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

    def input_test_pwd(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PWD_FIELD)
        )
        self.input_text('soft_reelly_322', *self.INPUT_PWD_FIELD)
        self.input_text('soft_reelly_322', *self.INPUT_PWD_FIELD_RPT)

    def pwd_btn_verification(self):
        connect_the_comp_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.PWD_BTN)
        )
        is_connect_the_company_button_clickable = connect_the_comp_button.is_enabled() and connect_the_comp_button.is_displayed()
        print(
            f'The "Connect the company" button is available and clickable. No error: {is_connect_the_company_button_clickable}')
