#!/usr/bin/python
# coding=utf-8
import sys
import unittest
from appium import webdriver
import time
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
            'platformVersion': '6.0',
            'deviceName': 'Nexus 5X',
            'appPackage': 'com.halley.halleyheaven',
            'appActivity': 'com.halley.halleyheaven.plugins.checkin.LayoutLockActivity',
            # 'appActivity': 'com.baidu.bainuo.home.FirstStartActivity'
            # 'appWaitActivity': 'com.baidu.bainuo.home.HomeTabActivity'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        contexts = driver.contexts
        print(len(contexts))
        # driver.switch_to.context("WEBVIEW")
        # driver.tap([(225, 980), (900, 1090)]), (225, 719)
        # el = driver.find_element_by_class_name('android.webkit.WebView')
        # el = el.find_element_by_class_name('android.webkit.WebView')
        # driver.find_element_by_name("美食").click()
        # driver.find_element_by_id('com.nuomi:id/home_category_icon').click()
        # driver.find_element_by_android_uiautomator('new UiSelector().description(\"美食\")').click()
        driver.tap([(100, 600)])
        time.sleep(20)
        driver.quit()

if __name__ == '__main__':
    unittest.main()


