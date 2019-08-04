from selenium.webdriver.common.by import By

from Page.page import Page
from Base.get_driver import get_driver

page_obj = Page(get_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity'))
# 点击我
page_obj.get_homepage().click_my_btn()
# 选择已注册账号
page_obj.get_choice_page().click_login_exist()
# 输入
page_obj.get_login_page().Login_in('18796773314', '1234567')
# msg = (By.XPATH, '//*[contains(@text,"密码错误")]')
# print(page_obj.get_login_page().get_element(msg, timeout=6, poll_frequency=0.5).text)
print(page_obj.get_login_page().get_toast_msg('密码错误'))
# # 个人页面
# page_obj.get_personal_page().get_per_text()
# page_obj.get_personal_page().click_setting()
# # 退出页面
# page_obj.get_setting().click_quit()
