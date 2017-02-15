# -*-coding:utf-8 -*-
import unittest
from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class FindElementTest(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {'aut': 'com.nuomi:7.1.0'}

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities
        )
        self.driver.implicitly_wait(30)

    def test_find_element_by_id(self):
        self.driver.get('and-activity://com.baidu.bainuo.dex.InstallDexActivity')
        # self.assertTrue("and-activity://HomeScreenActivity" in self.driver.current_url)
        # my_text_field = self.driver.find_element_by_id('my_text_field')
        # my_text_field.send_keys('Hello Selendroid')
        time.sleep(10)
        self.driver.switch_to.window("NATIVE_APP")
        self.driver.find_element_by_name("海淀区").click()

        # self.assertTrue('Hello Selendroid' in my_text_field.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()