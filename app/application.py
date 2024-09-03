# from pages.HomePage import HomePage
from pages.AddprojectPage import AddProjectPage
from pages.base_page import Page
from pages.MainPage import MainPage
# from pages.header import Header
from pages.LoginPage import LoginPage
from pages.community_page import CommunityPage
from pages.ContactUs import ContactUs
from pages.title_verification import TitleVerification
from pages.change_pwd import Change_pwd
from pages.subscr_payment import Subscription


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        # self.header = Header(driver)
        self.login_page = LoginPage(driver)
        self.project_page = AddProjectPage(driver)
        self.community_page = CommunityPage(driver)
        self.contact_page = ContactUs(driver)
        self.title_verification = TitleVerification(driver)
        self.change_pwd = Change_pwd(driver)
        self.subscr_payment = Subscription(driver)
        # self.home_page = HomePage(driver)
