from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TitleVerification(Page):
    USER_GUIDE = (By.XPATH, "//div[contains(@class, 'setting-text') and contains(., 'User guide')]")
    TITLE_LIST = (By.CSS_SELECTOR, "a.ytp-title-link.yt-uix-sessionlink")

    def click_on_user_guide(self):
        self.click(*self.USER_GUIDE)

    def verify_title_page(self, expected_url_portion):
        expected_base_url = 'https://soft.reelly.io/user-guide'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_base_url))
        current_url = self.driver.current_url
        try:
            assert expected_base_url in current_url, f"Expected URL {expected_base_url}, but got {current_url}"
            assert expected_url_portion in current_url, f"Expected URL to contain '{expected_url_portion}', but got '{current_url}'"
            print(f"Successfully verified the contact page with URL: {current_url}")
            print(f"URL contains expected portion: '{expected_url_portion}'")
        except AssertionError as e:
            print(f"URL verification failed: {str(e)}")
            raise
        return current_url

    def verify_all_lesson(self):
        def verify_all_lesson(self):
            titles = self.driver.find_elements(*self.TITLE_LIST)
            if not titles:
                raise Exception("No titles found.")

            for index, title in enumerate(titles, start=1):
                title_text = title.text.strip()
                assert title_text, f"Lesson {index} is missing a title!"
                print(f"Lesson {index} has the title: '{title_text}'")
