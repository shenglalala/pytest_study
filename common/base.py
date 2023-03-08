

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

'''封装selenium基本操作'''

# 定位类型错误异常



class LocatorTypeError(Exception):
    pass

class ElementNotFound(Exception):
    pass

class Base():
    ''' 基于原生selenium的二次封装 '''
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # # chrome_options.add_argument('--window-size=1920,1080')
    # co_driver = webdriver.Chrome('chromedriver', options=chrome_options)

    def __init__(self, driver:webdriver.Chrome, timeout=10, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t


    def find(self, locator):
        ''' 定位到元素返回元素对象，没定位到timeout异常 '''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        else:
            # print("正在定位元素")
            # presence_of_element_located()判断一个元素是否存在于页面DOM树中，存在则返回元素本身，不存在则报错。
            try:
                ele =WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound('定位元素超时')
        return ele

    def finds(self,locator):
        ''' 复数定位，返回elements对象 '''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        else:
            print("正在定位元素")
            # presence_of_element_located()判断一个元素是否存在于页面DOM树中，存在则返回元素本身，不存在则报错。
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return eles

    def send(self, locator, text=''):
        ''' 输入文本 '''
        ele = self.find(locator)
        if ele.is_displayed():
            try:
                ele.send_keys(text)
            except:
                print('输入失败')
        else:
            raise ElementNotVisibleException('元素不可见或不唯一')

    def click(self, locator):
        ''' 点击元素 '''
        ele = self.find(locator)
        if ele.is_displayed():
            try:
                ele.click()
            except:
                print('点击失败')
        else:
            raise ElementNotVisibleException('元素不可见或不唯一')

    def clear(self, locator):
        ''' 清空输入框文本 '''
        ele = self.find(locator)
        try:
            ele.clear()
        except:
            print('清空内容失败')

    def is_selected(self, locator):
        ''' 判断元素是否被选中,返回bool值 '''
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        ''' 判断单个元素是否存在 '''
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self, title=''):
        ''' 判断title是否存在 is'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title=''):
        '''判断title是否存在 contains(包含)'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=''):
        ''' 判断内容是否在text里面 '''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value=''):
        ''' 判断内容是否在value里面 '''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        ''' 判断alert弹窗及操作 '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        ''' 获取页面title '''
        return self.driver.title

    def get_text(self, locator):
        ''' 获取元素文本值（默认)'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        try:
            t = self.find(locator).text
            return t
        except:
            print("获取text值失败")

    def get_attribute(self, locator, name):
        ''' 获取当前元素属性 attribute:获取的元素属性, name:属性  className、name、text、value···'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        try:
            ele = self.find(locator)
            return ele.get_attribute(name)
        except:
            print(f"获取 {name} 值失败，返回")
            return ''

    def js_focus_element(self, locator):
        ''' 聚焦元素 '''
        if not isinstance(locator, type):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        ''' 滚动到顶部 '''
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        ''' 滚动到底部 '''
        js = 'window.scrollTo(%s, document.body.scrollHeight)'%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        ''' 下拉框选择 根据下标index（从0开始）'''
        if not isinstance(locator, type):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        element = self.find(locator)    # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        ''' 下拉框选择 根据value '''
        if not isinstance(locator, type):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        ''' 下拉框选择 根据选项的文本值 '''
        if not isinstance(locator, type):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        ''' 切换至iframe '''
        try:
            if isinstance(id_index_locator, int):    # 如果传入的是数字，则以该数字为下标取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):    # 如果传入的是字符串，则用iframe名字取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):    # 如果是元祖，则根据传入的locator取值
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print('iframe切换异常')

    def switch_handle(self, window_name):
        ''' 根据句柄名字切换句柄 '''
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        ''' 切换至alert弹窗 '''
        r = self.is_alert()
        if not r:
            print('alert不存在')
        else:
            return r

    def move_to_element(self, locator):
        ''' 鼠标悬停操作 '''
        if not isinstance(locator, type):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id', 'value')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = Base(driver)    # 实例化
    driver.get('https://www.baidu.com')
    loc_1 = ('id', 'kw')
    a = web.find(loc_1)
    print(a)
    web.send(loc_1, 'hello')

    driver.close()
