#!/usr/bin/python
# coding=utf-8
import sys
import unittest
from appium import webdriver
reload(sys)
sys.setdefaultencoding("utf8")


class BizareaopTest(unittest.TestCase):
    def setUp(self):
        print("Start...")

    def tearDown(self):
        print("tearDown...")

    @staticmethod
    def testRun():
        print("testRun")
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


