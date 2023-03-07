import allure
from common.base import Base
from common.config import host

add_project_url = host + '/add_project.html'

class AddProject(Base):
    ''' 新增项目页面 '''
    loc_1 = ('id', 'project_name')    # 项目名称定位
    loc_2 = ('id', 'publish_app')    # 所属应用定位
    loc_3 = ('id', 'project_desc')    # 项目描述定位
    loc_4 = ('id', 'save_project')    # 提交按钮
    # loc_5 = ('text_link', '新增项目')
    loc_5 = ('xpath', '//*[@id="left"]/div[2]/div/ul/li[1]/a')
    # 验证操作定位
    loc_classify_plist = ('xpath', '//*[@id="left"]/div[2]/div/ul/li[2]/a')
    loc_list_pname = ('xpath', '//*[@id="table"]/tbody/tr/td[3]/a')
    loc_add_fail = ('xpath', '//*[@class="bootbox-body"]')
    loc_add_fail_c = ('xpath', '/html/body/div[2]/div/div/div[3]/button')    # 新增失败弹窗-确定按钮

    @allure.step('新增项目步骤：输入项目名称')
    def input_p_name(self, project_name):
        ''' 输入项目名称 '''
        self.send(self.loc_1, project_name)

    @allure.step('新增项目步骤：输入所属应用')
    def input_p_app(self, publish_app):
        ''' 输入所属应用 '''
        self.send(self.loc_2, publish_app)

    @allure.step('新增项目步骤：输入项目描述')
    def input_p_desc(self, project_desc):
        ''' 输入项目描述 '''
        self.send(self.loc_3, project_desc)

    @allure.step('新增项目步骤：点击新增按钮')
    def click_botton(self):
        ''' 点击按钮 '''
        self.click(self.loc_4)

    @allure.step('新增项目步骤：点击新增项目分类')
    def click_classify(self):
        ''' 点击分类 '''
        self.click(self.loc_5)

    @allure.step('点击项目列表')
    def click_classify_verify(self):
        ''' 点击项目列表 '''
        self.click(self.loc_classify_plist)    # 点击项目列表

    @allure.step('判断新增成功')
    def is_add_suc(self, text='测试项目01'):
        ''' 验证是否新增成功'''
        self.click(self.loc_classify_plist)  # 点击项目列表
        list_pname= self.get_text(self.loc_list_pname)
        print(list_pname)
        return list_pname == text

    @ allure.step('判断新增失败')
    def is_add_fail(self, text):
        ''' 验证新增失败 '''
        fail_msg = self.get_text(self.loc_add_fail)
        self.click(self.loc_add_fail_c)
        print(fail_msg)
        return fail_msg == '操作异常：{"project_name":"%s 已存在"}'%text

    @allure.step('调用新增')
    def add(self, project_name= '测试项目02', publish_app= '测试应用01', project_desc= '测试内容01'):
        ''' 新增项目 '''
        # self.driver.get(add_project_url)
        self.input_p_name(project_name)
        self.input_p_app(publish_app)
        self.input_p_desc(project_desc)
        self.click_botton()

if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    driver = webdriver.Chrome()
    web = LoginPage(driver)    # 调用前先实例化
    web.login()
    res1 = web.is_login_success()
    print('登录结果为：%s'%res1)

    # 新增
    add_p = AddProject(driver)    # 实例化
    add_p.click_classify()
    add_p.add()
    res2 = add_p.is_add_suc(text='测试项目02')
    print('新增结果为：%s'%res2)



