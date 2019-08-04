import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=15, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=15, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1.0):
        self.get_element(loc, timeout, poll_frequency).click()

    def send_elements(self, loc, text, timeout=15, poll_frequency=1.0):
        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def scroll_screen(self, tag=1):
        screen = self.driver.get_window_size()
        width = screen.get('width')
        height = screen.get('height')

        time.sleep(3)
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    def get_toast_msg(self, msg):
        toast_msg = (By.XPATH, '//*[contains(@text,"{}")]'.format(msg))
        return self.get_element(toast_msg, timeout=6, poll_frequency=0.5).text

    def get_screen_shot(self, name="截图"):
        img_name = ('./image' + os.sep + '%d.png' % int(time.time()))
        self.driver.get_screenshot_as_file(img_name)
        with open(img_name, 'rb') as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)


