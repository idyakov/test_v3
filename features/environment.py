from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use Selenium Manager
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 3)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    try:
        browser_init(context)
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()