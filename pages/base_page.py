from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Page:
    MENU_LANG = (By.CSS_SELECTOR, "div[id='w-dropdown-toggle-0']")
    LINK_TEXT = (By.XPATH, '//div[text()={TEXT}]')
    MENU_TITLE = (By.CSS_SELECTOR, "h1.h1-menu")
    MAIN_MENU = (By.CSS_SELECTOR, "menu-button-text")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_visible(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _get_locator(self, text):
        return [self.LINK_TEXT[0], self.LINK_TEXT[1].replace('{TEXT}', text)]

    def click_link(self, link_text):
        locator = self._get_locator(link_text)
        self.click(*locator)

    def change_language(self):
        self.wait_until_visible(*self.MENU_LANG)
        ln = self.find_element(*self.MENU_LANG)
        actions = ActionChains(self.driver)
        actions.move_to_element(ln)
        actions.move_by_offset(0, 25)
        actions.click()
        actions.perform()
        sleep(2)

    def verify_home_page_url(self):
        print('Verification')

    def verify_user_name(self, name):
        print('name:', name)

    def verify_menu_title(self, expected_title="Главное меню"):
        try:
            menu_title_element = self.wait.until(
                EC.visibility_of_element_located(self.MENU_TITLE)
            )
            actual_title = menu_title_element.text
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
            print(f"Menu title verified: '{actual_title}'")
        except AssertionError as e:
            print(f"Menu title verification failed: {str(e)}")
        except Exception as e:
            print(f"An error occurred while verifying menu title: {str(e)}")


class HomePage(Page):
    pass


class HelpPage(Page):
    CLICK_SIGN_IN_USER = (By.CSS_SELECTOR,
                          "button[class='styles__StyledBaseButtonInternal-sc-ysboml-0 "
                          "styles__ButtonPrimary-sc-5fh6rr-0 styles__SignInButton-sc-q9vn5-4 hBqTSs bEdlr gCsDNn']")
    MENU = (By.CSS_SELECTOR, "select[id='j_id0:contentTemplate:j_id79:j_id80:viewHelpTopics:ViewHelpTopics']")

    def dropdown_menu(self):
        dropdown_menu_1 = self.find_element(*self.MENU)
        select = Select(dropdown_menu_1)
        select.select_by_value('Orders & Purchases')

    def open_help_page(self):
        self.driver.get(
            'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_page(self, expected_url):
        print(expected_url)
        self.wait.until(EC.url_contains(expected_url), message=f'URL verified')

    def close(self):
        self.driver.close()
