#!/usr/bin/python
# coding=utf-8
import sys
import unittest
from appium import webdriver
from uiautomator import device as d
reload(sys)
sys.setdefaultencoding("utf8")


class BizareaopTest(unittest.TestCase):
    def setUp(self):
        d.screen.on()
        d.press.home()
        d(text="百度糯米").click()
        d(textContains="北京").click()
        d(textContains="上海市").click()
        print("Start...")

    def tearDown(self):
        print("tearDown...")

    @staticmethod
    def testReturn():
        # d(text="商圈头条").click()
        d.press.back()
        print("test")
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4.2',
            'deviceName': 'Nexus_5X',
            'appPackage': 'com.google.android.calculator',
            'appActivity': 'com.android.calculator2.CalculatorGoogle'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.find_element_by_name("1").click()
        driver.quit()

if __name__ == '__main__':
    unittest.main()


