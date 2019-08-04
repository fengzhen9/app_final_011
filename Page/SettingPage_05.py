from Base.base import Base
from Page.pageElements import PageElements


class Setting(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_quit(self, tag=1):
        self.scroll_screen()
        self.click_element(PageElements.setting_logout_btn_id)
        if tag == 1:
            self.click_element(PageElements.setting_acc_logout_btn_id)
        if tag == 2:
            self.click_element(PageElements.setting_dis_logout_btn_id)
