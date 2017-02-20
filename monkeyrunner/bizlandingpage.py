#!/usr/bin/python
# coding:utf-8
# --------------------------
# terminal command:
# monkeyrunner D:\HanLeiDOC\HanLeiDOC\Python\BizTest\monkeyrunner\bizlandingpage.py
# --------------------------
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

POS_TAB_Cuisine = [200, 200]
POS_TAB_Parent_Offspring = [500, 200]
POS_TAB_Entertainment = [900, 200]
POSs = [
    # have city_global_column
    {
        "tab": {"pos": POS_TAB_Cuisine, "next_page": [1, 1]},
        "ugc": {"entrance": [500, 1200], "to_poi_detail": [500, 200]},
        "ranking_list": {"entrance": [800, 530], "to_poi_detail": [500, 800]},
        "column": {"entrance": [500, 1200]},
        "poi": {"to_poi_detail": [500, 500]}
    },
    # without city_global_column and not from nuomi_home
    {
        "tab": {"pos": POS_TAB_Parent_Offspring, "next_page": [0, 0]},
        "ugc": {"entrance": [500, 500], "to_poi_detail": [500, 200]},
        "ranking_list": {"entrance": [800, 750], "to_poi_detail": [500, 800]},
        "column": {"entrance": [500, 1000]},  # 此处为排行榜show的poi
        "poi": {"to_poi_detail": [500, 1500]}
    },
    # have city_global_column but from nuomi_home
    {
        "tab": {"pos": POS_TAB_Cuisine, "next_page": [1, 1]},
        "ugc": {"entrance": [500, 500], "to_poi_detail": [500, 200]},
        "ranking_list": {"entrance": [200, 850], "to_poi_detail": [500, 800]},
        "column": {"entrance": [500, 1300]},  # 此处为FEED里的POI
        "poi": {"to_poi_detail": [500, 1600]},  # 此处为Video Column
        "extra": {"pos": [500, 1000]}
    },
]


class TestLandingPage:
    TOUCH_TYPE = "DOWN_AND_UP"
    SLEEP_TIME = 3
    HEIGHT_TITLE_BAR = 189
    HEIGHT_NUOMI_HOME = 1794
    HEIGHT_COMPONENT = HEIGHT_NUOMI_HOME - HEIGHT_TITLE_BAR
    POS_TAB_Cuisine = [200, 200]
    POS_TAB_Parent_Offspring = [500, 200]
    POS_TAB_Entertainment = [900, 200]

    def __init__(self, device, positions):
        self.POS = positions
        self.device = device

    def tear_down(self, msg, filename=None):
        print(msg)
        time.sleep(self.SLEEP_TIME)
        if filename is not None:
            result = self.device.takeSnapshot()
            result.writeToFile('C:/users/hanlei08/desktop/test_result/'
                               + filename + '.png', 'png')
    '''
        点击页面某处
    '''
    def touch(self, xy):
        self.device.touch(xy[0], xy[1], self.TOUCH_TYPE)
    '''
        初始化 刷新页面
    '''
    def init_home(self):
        self.device.drag((250, self.HEIGHT_TITLE_BAR),
                         (250, self.HEIGHT_COMPONENT), 0.1, 10)
        # self.device.drag((250, self.HEIGHT_COMPONENT),
        #                  (250, self.HEIGHT_TITLE_BAR), 0.1, 10)
        time.sleep(5)
        print("-------init finished------")
    '''
        switch tab
    '''
    def switch_tab(self):
        self.touch(self.POS['tab']['pos'])
        self.tear_down(msg="switch tab...", filename='tab')
    '''
        进入落地页
    '''
    def tap_to_landing_page(self):
        time.sleep(self.SLEEP_TIME)
        self.device.touch(500, 700, self.TOUCH_TYPE)
        self.tear_down(msg="tap to landing page...", filename='landing_page')
    '''
        滚动到下一屏
    '''
    def next_page(self,  index):
        if self.POS['tab']['next_page'][index] == 0:
            return
        self.device.drag((250, self.HEIGHT_COMPONENT),
                         (250, 0), 1, 10)
        time.sleep(self.SLEEP_TIME)
    '''
        返回到前一个页面
    '''
    def back(self, msg="prior"):
        # self.device.touch(50, 120, self.TOUCH_TYPE)
        self.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
        self.tear_down(msg="back to "+msg+"...")

    '''
        从落地页点击进入ugc列表页
    '''
    def tap_to_ugc(self):
        self.touch(self.POS['ugc']['entrance'])
        self.tear_down(msg="tap to ugc...", filename='ugc')
        # 跳转店铺页
        self.touch(self.POS['ugc']['to_poi_detail'])
        self.tear_down(msg="tap to ugc poi detail...", filename='ugc_poi')
        # 返回
        self.back("ugc")
        self.back("landing_page")

    '''
        从落地页点击进入排行榜详情页
    '''
    def tap_to_ranking_list(self):
        self.touch(self.POS['ranking_list']['entrance'])
        self.tear_down(msg="tap to ranking_list...", filename='rank')
        # 跳转店铺页
        self.touch(self.POS['ranking_list']['to_poi_detail'])
        self.tear_down(msg="tap to ranking_list poi detail...", filename='rank_poi')
        # 返回
        self.back("ranking_list")
        self.back("landing_page")

    '''
        从落地页点击进入专栏详情页
    '''
    def tap_to_column(self):
        self.touch(self.POS['column']['entrance'])
        self.tear_down(msg="tap to column...", filename='column')
        # 返回
        self.back("landing_page")

    '''
        从落地页点击进入POI详情页
    '''
    def tap_to_poi(self):
        self.touch(self.POS['poi']['to_poi_detail'])
        self.tear_down(msg="tap to feed poi detail...", filename='poi')
        # 返回
        self.back("landing_page")
    '''

    '''
    def tap_to_city_global_column(self):
        if self.POS.get('extra') is not 'None':
            self.touch(self.POS['extra']['pos'])
            self.tear_down(msg="tap to column...", filename='column')
            # 返回
            # self.back("landing_page")
    '''
        test suite for Bizareatop_Landing_Page
    '''
    def start(self):
        self.init_home()
        self.tap_to_landing_page()
        self.switch_tab()

        self.tap_to_ugc()
        self.tap_to_city_global_column()

        self.next_page(0)
        self.tap_to_ranking_list()
        self.tap_to_column()

        self.next_page(1)
        self.tap_to_poi()
        self.back("nuomi_home")
        print("-------test finished------\n")

    def test(self):
        self.init_home()
        self.tap_to_landing_page()
        self.switch_tab()
        self.next_page(0)
        self.next_page(1)
        # self.next_page(1)


def test_landing_page(device):
    # TestLandingPage(device=device, positions=POSs[0]).start()
    TestLandingPage(device=device, positions=POSs[2]).start()
    TestLandingPage(device=device, positions=POSs[1]).start()  # 亲子
    POSs[1]['tab']['pos'] = POS_TAB_Entertainment
    TestLandingPage(device=device, positions=POSs[1]).start()  # 休闲娱乐


def biz_test():
        device = MonkeyRunner.waitForConnection()
        package = 'com.nuomi'
        activity = 'com.baidu.bainuo.dex.InstallDexActivity'
        run_component = package + '/' + activity
        device.startActivity(component=run_component)
        print("start activity...")
        test_landing_page(device)


if __name__ == "__main__":
    biz_test()
