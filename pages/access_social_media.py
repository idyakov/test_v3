from lib2to3.fixes.fix_input import context

from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AccessSocialMedia(Page):
    SUB_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Subscription & payments')]")
    BACK_BTN = (By.XPATH, "//div[contains(@class, 'next-step-- black') and contains(., '<- Back')]")
    UPGRD_BTN = (By.XPATH, "//div[contains(@class, 'next-step--') and contains(., 'Upgrade plan')]")
    SPRT_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'Support')]")
    TTL_SUB = (
        By.XPATH, "//div[contains(@class, 'lotion-your-h3--price size') and contains(., 'Subscription & payments')]")
    NEWS_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'News')]")

    def click_sprt_btn(self):
        self.click(*self.SPRT_BTN)

    def switch_to_new_tab_win(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All_windows:', self.driver.window_handles)
        print('Switching to: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def verify_new_tab_page(self, expected_url_portion):
        expected_base_pwd_url = 'https://api.whatsapp.com/send?phone=971568098349&text=Please%20describe%20your%20problem%20or%20ask%20a%20question.%0A%0A'
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

    def go_back_tab_page(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All_windows:', self.driver.window_handles)
        print('Switching to: ', all_windows[0])
        self.driver.switch_to.window(all_windows[0])

    def click_news_btn(self):
        self.click(*self.NEWS_BTN)

    def verify_new_telegram_tab_page(self, expected_url_portion_tme):
        expected_base_tme_pwd_url = 'https://t.me/reellydxb'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_base_tme_pwd_url))
        current_url = self.driver.current_url
        try:
            assert expected_base_tme_pwd_url in current_url, f"Expected URL {expected_base_tme_pwd_url}, but got {current_url}"
            assert expected_url_portion_tme in current_url, f"Expected URL to contain '{expected_url_portion_tme}', but got '{current_url}'"
            print(f"Successfully verified the contact page with URL: {current_url}")
            print(f"URL contains expected portion: '{expected_url_portion_tme}'")
        except AssertionError as e:
            print(f"URL verification failed: {str(e)}")
            raise
        return current_url
