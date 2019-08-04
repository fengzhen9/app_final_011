from Base.base import Base
from Page.pageElements import PageElements


class Choice_Login(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_login_exist(self):
        self.click_element(PageElements.choice_login_exits_account_id)