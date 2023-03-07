import time
import allure

from common.base import Base
from common.config import host
# host = 'http://47.108.155.10'
login_url = host + '/login.html'

class LoginPage(Base):
    ''' 登录页面 '''

    # 定位元素
    loc_1 = ('id', 'username')    # 账号
    loc_2 = ('id', 'password')    # 密码
    # loc_3 = ('xpath', '//input[contains(@class, "btn")]')
    loc_3 = ('id', 'loginBtn')    # 登录按钮

    loc_suc = ('id', 'login-user')

    @allure.step('登录步骤：输入账号')
    def input_user(self, username):
        ''' 输入账号 '''
        self.send(self.loc_1, username)

    @allure.step('登录步骤：输入密码')
    def input_pwd(self, pwd):
        ''' 输入密码 '''
        self.send(self.loc_2, pwd)

    @allure.step('登录步骤：点击登录按钮')
    def click_botton(self):
        ''' 点击按钮 '''
        self.click(self.loc_3)

    @allure.step('调用登录')
    def login(self, username="shengyoyo", pwd="S122333_yoyo"):
        ''' 登录 '''
        self.driver.get(login_url)  # 获取地址
        self.input_user(username)
        self.input_pwd(pwd)
        self.click_botton()

    @allure.step('判断是否登录成功')
    def is_login_success(self):
        ''' 判断是否登录成功 '''
        text = self.get_text(self.loc_suc)
        print('该页面判断元素为：%s'%text)
        return text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)    # 实例化
    web.login('shengyoyo', 'S122333_yoyo')

    # 判断是否登录成功
    time.sleep(10)
    result = web.is_login_success()
    assert result == 'shengyoyo'

