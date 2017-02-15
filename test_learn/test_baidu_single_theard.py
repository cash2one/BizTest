# coding=utf-8
from selenium import webdriver
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")


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
    start = time.time()
    print('start:%s' % start)
    lists = {'chrome': ['thread', 'baidu'], 'firefox': ['webdriver', 'fire']}
    threads = []
    files = range(4)

    for browser, search in lists.items():
        for s in search:
            test_baidu(browser, s)
    end = time.time()
    print('end:%s' % end)
    print(end-start)
