import time
import pytest
import platform
from selenium import webdriver
from pages.login_page import LoginPage


def pytest_addoption(parser):
    ''' pytest钩子函数，自定义命令行输入'''
    parser.addoption('--headless',
                     action = 'store',
                     default = 'no',
                     help = 'set chrome headless option yes or no')

# 全局fixture
@pytest.fixture(scope='session')
def driver(request):
    ''' 定义全局driver '''
    # 判断操作系统
    # if platform.system() == 'Windows':
    #     _driver = webdriver.Chrome()
    # elif platform.system() == 'Darwin':
    #     _driver = webdriver.Chrome()
    # elif platform.system() == 'Linux':
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-gpu')    # 禁用GPU硬件加速
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     chrome_options.add_argument('--window-size=1920,1080')    # 设置当前窗口宽度和高度
    #     _driver = webdriver.Chrome('chromedriver', options=chrome_options)

    # config.getoption()    读取自定义参数值
    headless = request.config.getoption('--headless')
    if headless == 'yes':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')    # 禁用GPU硬件加速
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')    # 设置当前窗口宽度和高度
        _driver = webdriver.Chrome('chromedriver', options=chrome_options)
    else:
        _driver = webdriver.Chrome()


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