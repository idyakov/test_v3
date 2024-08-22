from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class AddProjectPage(Page):
    #Project related locators
    SEND_AN_APPLICATION_BUTTON = (
        By.XPATH, "//input[contains(@class, 'purchase-access w-button') and contains(@value, 'Send an application')]")
    INPUT_PROJECT_EMAIL = (By.CSS_SELECTOR, '[id="Email-add-project"]')
    INPUT_PROJECT_PHONE = (By.CSS_SELECTOR, '[id="Phone"]')
    INPUT_PROJECT_NAME = (By.CSS_SELECTOR, '[id="Name-project"]')
    INPUT_PROJECT_COUNTRY = (By.CSS_SELECTOR, '[id="Country"]')
    INPUT_PROJECT_FIELD_NAME = (By.CSS_SELECTOR, '[id="Your-name"]')
    INPUT_PROJECT_FIELD_COMPANY = (By.CSS_SELECTOR, '[id="Your-company-name"]')
    INPUT_PROJECT_FIELD_ROLE = (By.CSS_SELECTOR, '[id="Role"]')
    INPUT_PROJECT_AGE = (By.CSS_SELECTOR, '[id="Age-of-the-company"]')
    ADD_PROJECT = (By.XPATH, "//div[contains(text(), 'Add a project')]")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    REELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")  # input email
    REELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")  # input password
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")
    CLICK_EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    INPUT_FIELD_VERIFICATION = (
        By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    CLICK_SAVE = (By.XPATH, "//div[contains(@wized, 'saveButtonProfile') and contains(@class, 'save-changes-button')]")
    CLICK_CLOSE = (By.XPATH, "//div[contains(@class, 'profile-button') and contains(., 'Close')]")
    CLICK_CONNECT = (By.XPATH, "//div[contains(text(), 'Connect the company')]")
    CLICK_MAIN_MENU = (By.XPATH, "//div[contains(@class, 'menu-button-text') and contains(., 'Main menu')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_save_changes_(self):
        # Get the second element that matches the XPath
        elements = self.driver.find_elements(*self.CLICK_SAVE)
        if len(elements) > 1:
            elements[0].click()
        else:
            raise Exception("The second 'Save changes' button was not found.")

    def __init__(self, driver):
        super().__init__(driver)
        self.default_pw = 'Password'

    def click_sign_in(self):
        self.click(*self.CONTINUE_BUTTON)


    def click_on_settings_(self):
        self.click(*self.CLICK_SETTINGS)

    def edit_profile(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CLICK_EDIT_PROFILE)
        ).click()

    def input_fields_(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_FIELD)
        )
        self.input_text('Hebrew, Russian, Test', *self.INPUT_FIELD)

    def verify_input_fields_(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_FIELD_VERIFICATION)
        )
        text_message = element.get_attribute('value')
        print(f'The language chosen is - "{text_message}"')

    # def click_on_save(self):
    #     WebDriverWait(self.driver, 4).until(
    #         EC.presence_of_element_located(self.CLICK_SAVE)
    #     ).click()

    def click_on_close_(self):
        # Get the second element that matches the XPath
        elements = self.driver.find_elements(*self.CLICK_CLOSE)
        if len(elements) > 1:
            elements[0].click()
        else:
            raise Exception("The second 'Close' button was not found.")

    def click_on_page_company(self):
        self.click(*self.CLICK_CONNECT)

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All_windows:', self.driver.window_handles)
        print('Switching to: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def verify_new_tap_page(self, expected_url):
        # Wait for the new page to load
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # Get the current URL
        current_url = self.driver.current_url

        # Assert that the current URL matches the expected URL
        assert current_url == expected_url, f"Expected URL {expected_url}, but got {current_url}"

        return current_url

    def click_on_main_menu(self):
        self.click(*self.CLICK_MAIN_MENU)

    def click_add_project(self):
        self.click(*self.ADD_PROJECT)

    def input_project_info(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_NAME)
        )
        self.input_text('OSTAP BENDER', *self.INPUT_PROJECT_FIELD_NAME)
        self.input_text('ROGA&KOPYTA', *self.INPUT_PROJECT_FIELD_COMPANY)
        self.input_text('DIRECTOR', *self.INPUT_PROJECT_FIELD_ROLE)
        self.input_text('EST 1884', *self.INPUT_PROJECT_AGE)
        self.input_text('Russian Empire', *self.INPUT_PROJECT_COUNTRY)
        self.input_text('ROASTEDSUHARY', *self.INPUT_PROJECT_NAME)
        self.input_text('779266', *self.INPUT_PROJECT_PHONE)
        self.input_text('rabochiy_krestyanin@gmail.com', *self.INPUT_PROJECT_EMAIL)

    def input_field_verification(self):
        element_email = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PROJECT_EMAIL)
        )
        text_message_email = element_email.get_attribute('value')
        print(f'The email input field verification - "{text_message_email}"')

        element_name = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_NAME)
        )
        text_message_name = element_name.get_attribute('value')
        print(f'The name input field verification - "{text_message_name}"')

        element_company = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_COMPANY)
        )
        text_message_company = element_company.get_attribute('value')
        print(f'The company name input field verification - "{text_message_company}"')

    def send_application_button_verification(self):
        send_application_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.SEND_AN_APPLICATION_BUTTON)
        )
        is_button_clickable = send_application_button.is_enabled() and send_application_button.is_displayed()
        print(f'The "Send an application" button is available and clickable. No error: {is_button_clickable}')

    def get_email_value(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_PROJECT_EMAIL)
        )
        return element.get_attribute('value')

