from Base.base import Base
from Page.pageElements import PageElements


class PersonalPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_per_text(self):
        return self.get_element(PageElements.person_shopcart_id).text

    def click_setting(self):
        self.click_element(PageElements.person_setting_btn_id)
