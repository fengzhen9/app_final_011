from selenium.webdriver.common.by import By

from Base.base import Base
from Page.pageElements import PageElements


class Login(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def Login_in(self, username, pwd):
        self.send_elements(PageElements.login_name_id, username)
        self.send_elements(PageElements.login_passwd_id, pwd)
        self.click_element(PageElements.login_btn_id)

    def close_page(self):
        self.click_element(PageElements.exit_btn_id)

    def if_login_btn(self):
        self.get_element(PageElements.login_btn_id)