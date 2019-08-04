from Page.HomePage01 import HomePage
from Page.choice_login02 import Choice_Login
from Page.Login03 import Login
from Page.personal_page_04 import PersonalPage
from Page.SettingPage_05 import Setting


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_homepage(self):
        return HomePage(self.driver)

    def get_choice_page(self):
        return Choice_Login(self.driver)

    def get_login_page(self):
        return Login(self.driver)

    def get_personal_page(self):
        return PersonalPage(self.driver)

    def get_setting(self):
        return Setting(self.driver)
