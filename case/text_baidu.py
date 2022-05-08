import unittest
from selenium import webdriver
import time
from pages.baidu_search import SeachPage

class TestBaidu(unittest.TestCase):
    # ==========================================================
    # 设置启动后后的初始化浏览器驱动（setUp） ，和运行完毕后的操作（tearDown）
    # ==========================================================
    # 运行准备（必须有！）
    def setUp(self) ->None:
        self.driver = webdriver.Chrome()
        # 这个是设置加载驱动的超时时间
        self.driver.implicitly_wait(10)

    # 运行完毕后（）
    def tearDown(self) ->None:
        self.driver.quit()
    # ==========================================================
    '''这一步设置运行的顺序和数据参数的传输'''
    def test_search(self):
        # 初始化 （self.driver是给三个文件进行绑定，"https://www.baidu.com"，是给BasePage里面的get传参数用）
        sp = SeachPage(self.driver, "https://www.baidu.com")
        # ==========================================================
        # 动作行为逻辑操作（只需调整摆放顺序、输入和获取到的数据参数）
        time.sleep(3)# 等待3秒
        sp.go_baidu()# 访问百度
        time.sleep(3)# 等待3秒
        sp.locate_search_input("张三") #填写数据
        time.sleep(3)# 等待3秒
        sp.click_baidu_btn() # 点击操作
        # ==========================================================
        # 循环等待，防止浏览器自动关闭
        while True:
            pass
        # ==========================================================
