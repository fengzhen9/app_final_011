import pytest

import os, sys

sys.path.append(os.getcwd())

from selenium.common.exceptions import TimeoutException

from Base.get_driver import get_driver
from Page.page import Page


from Base.get_login_data import Get_Login_Data


def get_data():
    suc_list = []
    fail_list = []
    data = Get_Login_Data().get_yaml_data('login_data.yml')
    for i in data.keys():
        # print(i) 打印出用例编号
        if data.get(i).get('toast'):
            fail_list.append((i, data.get(i).get('username'),
                              data.get(i).get('passwd'),
                              data.get(i).get('toast'),
                              data.get(i).get('expect_data')))
        else:
            suc_list.append((i, data.get(i).get('username'),
                             data.get(i).get('passwd'),
                             data.get(i).get('expect_data')))
    return {'suc': suc_list, 'fail': fail_list}


class Test:
    def setup_class(self):
        self.page_obj = Page(get_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity'))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        self.page_obj.get_homepage().click_my_btn()
        self.page_obj.get_choice_page().click_login_exist()

    @pytest.mark.parametrize("caseNo,username,password,excp", get_data().get('suc'))
    def test_login_suc(self, caseNo, username, password, excp):
        self.page_obj.get_login_page().Login_in(username, password)  # 登录
        try:
            res = self.page_obj.get_personal_page().get_per_text()
            try:  # 断言
                assert res == excp
            except AssertionError:  # 断言失败
                self.page_obj.get_login_page().get_screen_shot()  # 截图
                assert False
            finally:

                self.page_obj.get_personal_page().click_setting()  # 点击设置
                self.page_obj.get_setting().click_quit()  # 退出操作
        except TimeoutException:
            self.page_obj.get_login_page().get_screen_shot()  # 截图
            self.page_obj.get_login_page().close_page()
            assert False

    @pytest.mark.parametrize("caseNo,username,password,toast,excp", get_data().get('fail'))
    def test_login_fail(self, caseNo, username, password, toast, excp):
        """

        :param caseNo: 用例编号
        :param username: 账号
        :param password: 密码
        :param toast: 提示信息
        :param excp: 预期结果
        :return:
        """
        self.page_obj.get_login_page().Login_in(username, password)  # 登录
        try:
            """找到toast"""
            res = self.page_obj.get_login_page().get_toast_msg(toast)  # 获取toast消息
            try:
                assert res == excp  # 断言
            except AssertionError:
                self.page_obj.get_login_page().get_screen_shot()  # 截图
                assert False
        except TimeoutException:
            self.page_obj.get_login_page().get_screen_shot()  # 截图
            assert False
        finally:
            try:
                """登录按钮是否存在"""
                self.page_obj.get_login_page().if_login_btn() # 判断登录按钮
                self.page_obj.get_login_page().close_page()  # 关闭登录页面
            except TimeoutException:
                """登录按钮不存在"""
                self.page_obj.get_personal_page().click_setting()  # 点击设置
                self.page_obj.get_setting().click_quit()  # 退出页面
                assert False
