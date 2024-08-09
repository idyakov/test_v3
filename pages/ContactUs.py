from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ContactUs(Page):
    CLICK_CONTACT_US = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Contact us')]")
    ICON_INSTAGRAM = (By.XPATH, "//div[contains(@class, 'text-social') and contains(., 'Instagram')]")
    ICON_TELEGRAM = (By.XPATH, "//div[contains(@class, 'text-social') and contains(., 'Telegram')]")
    ICON_YOUTUBE = (By.XPATH, "//div[contains(@class, 'text-social') and contains(., 'Youtube')]")
    ICON_LINKEDIN = (By.XPATH, "//div[contains(@class, 'text-social') and contains(., 'LinkedIn')]")
    CONNECT_THE_COMPANY_BUTTON = (By.CSS_SELECTOR, '[id="w-node-_3e5a3d2d-27b1-b6a3-63ba-8fa23fdaf2c2-7f66debb"]')
    SOCIAL_MEDIA_ICONS = [ICON_INSTAGRAM, ICON_TELEGRAM, ICON_YOUTUBE, ICON_LINKEDIN]

    def count_social_media_icons(self):
        try:
            icon_count = 0
            for icon_locator in self.SOCIAL_MEDIA_ICONS:
                if self.is_element_present(icon_locator):
                    icon_count += 1

            assert icon_count >= 4, f"Expected at least 4 social media icons, but found {icon_count}"
            print(f"Found {icon_count} social media icons")

            return icon_count
        except Exception as e:
            print(f"Error counting social media icons: {e}")
            return 0

    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    def click_on_contact_us(self):
        self.click(*self.CLICK_CONTACT_US)

    def verify_contact_tab_page(self):
        expected_url = 'https://soft.reelly.io/contact-us'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL {expected_url}, but got {current_url}"
        print(f"Successfully verified the contact page with URL: {current_url}")

        return current_url

    def connect_the_company_button_verification(self):
        connect_the_comp_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CONNECT_THE_COMPANY_BUTTON)
        )
        is_connect_the_company_button_clickable = connect_the_comp_button.is_enabled() and connect_the_comp_button.is_displayed()
        print(
            f'The "Connect the company" button is available and clickable. No error: {is_connect_the_company_button_clickable}')
