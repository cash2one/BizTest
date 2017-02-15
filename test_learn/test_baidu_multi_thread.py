# coding=utf-8
from selenium import webdriver
from HalleyTest import HalleyTestCase
from email.mime.text import MIMEText
from email.header import Header
import smtplib
# import unittest
from threading import Thread
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")


class TestBaidu(HalleyTestCase):
    def out_test(self):
        # driver = webdriver.PhantomJS()
        driver = webdriver.Chrome()
        driver.get("http://nuomi.com")
        # driver.find_element_by_id("kw").send_keys("hl")
        # driver.find_element_by_id("su").click()
        driver.refresh()
        print(driver.title)
        self.assertEqual(driver.title, "【团购】团购网站，高品质团购网站_百度糯米")
        for i in range(10):
            js = "window.scrollTo(0,document.body.scrollHeight)"
            driver.execute_script(js)
            time.sleep(1)
        time.sleep(5)
        driver.quit()

    def o_test(self):
        smtpserver = 'smtp.qq.com'
        user = '482615960@qq.com'
        password = 'hlicoffee0416'
        sender = '482615960@qq.com'
        receiver = 'tjuhanlei@163.com'
        subject = 'Test Python email'

        msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')

        smtp = smtplib.SMTP_SSL()
        smtp.connect(smtpserver)
        smtp.login(user, password)

        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

    def screenshot_test(self):
        driver = webdriver.PhantomJS()
        server = "http://www.baidu.com"
        driver.get(server)
        file_name = server.replace("http://", "")
        file_name = file_name.replace(".", "_")
        file_name = file_name.replace("/", "_")
        driver.get_screenshot_as_file(file_name+".png")
        driver.quit()


def test_baidu(browser, search):
    print('start thread: %s' % time.ctime())
    print("["+browser+"] "+search)
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.PhantomJS()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    # unittest.main()
    start = time.time()
    print('start:%s' % start)
    lists = {'chrome': ['thread', 'baidu'], 'firefox': ['webdriver', 'fire']}
    threads = []
    files = range(4)

    for browser, search in lists.items():
        for s in search:
            t = Thread(target=test_baidu, args=(browser, s))
            print(s)
            threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    end = time.time()
    print('end:%s' % end)
    print(end-start)
