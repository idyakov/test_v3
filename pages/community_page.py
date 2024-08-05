from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CommunityPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")
    CLICK_MAIN_MENU = (By.XPATH, "//div[contains(@class, 'menu-button-text') and contains(., 'Main menu')]")
    CLICK_COMMUNITY_PAGE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Community']")
    CONTACT_SUPPORT_BUTTON = (
        By.XPATH, "(//a[@href='https://t.me/reelly_dubai_bot?start=w18415667' and contains(text(), 'Contact "
                  "support')])[2]")
    REELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")  # input email
    REELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")  # input password

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.default_pw = 'Password'

    def input_credentials(self):
        self.input_text('dyak.ilya@gmail.com', *self.REELLY_EMAIL)  #input your own registered email
        self.input_text('XrvzakG!E4i@Zzh', *self.REELLY_PASSWORD)  #input your own registered password

    def click_sign_in(self):
        self.click(*self.CONTINUE_BUTTON)

    def click_on_settings(self):
        self.click(*self.CLICK_SETTINGS)

    def click_on_community(self):
        self.click(*self.CLICK_COMMUNITY_PAGE)

    def verify_expected_page(self, verify_expected_page):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(verify_expected_page))
        current_url = self.driver.current_url
        assert current_url == verify_expected_page, f"Expected URL {verify_expected_page}, but got {current_url}"
        return current_url

    def contact_support_button_verification(self):
        contact_support_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CONTACT_SUPPORT_BUTTON)
        )
        is_support_button_clickable = contact_support_button.is_enabled() and contact_support_button.is_displayed()
        print(f'The "Contact support" button is available and clickable. No error: {is_support_button_clickable}')
