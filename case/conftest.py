import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from common.driver_handless import d_hless

# 全局fixture
@pytest.fixture(scope='session')
def driver(request):
    ''' 定义全局driver '''
    # _driver = webdriver.Chrome()
    # _driver.maximize_window()    # 最大化窗口

    # 无头模式
    d_h = d_hless()
    _driver = d_h.handless_driver()

    def end():
        ''' 测试用例完成后，执行终结函数 '''
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope='session')
def login(driver):
    ''' 前置-登录 '''
    web = LoginPage(driver)
    web.login()
    return driver