import pytest
import allure
import os

from pages.add_project_page import AddProject
from common.read_yml import readyml

'''
allure用例等级划分
blocker   #  阻塞缺陷（功能未实现，无法下一步）
critical    # 严重缺陷（功能点缺失）
normal    # 一般缺陷（边界问题，格式错误）
minor   # 次要缺陷（界面错误与UI不一致）
trivial    # 轻微缺陷（必须项无提示，或者提示不规范）
'''
# test_data_demo = [
#                   ({'p_name': 'param_demo_04', 'pu_app': 'param_pa_04', 'p_desc': 'param_pd_04'},
#                    'param_demo_04'),
#                   ({'p_name': 'param_demo_05', 'pu_app': 'param_pa_05', 'p_desc': 'param_pd_05'},
#                    'param_demo_05'),
#                   ({'p_name': 'param_demo_06', 'pu_app': 'param_pa_06', 'p_desc': 'param_pd_06'},
#                    'param_demo_06')]

# os.path.realpath(__file__)  获取当前文件绝对路径，包括当前文件
# os.path.dirname(__file__)  获取当前文件的上一层绝对路径，不包括当前文件
curpath = os.path.dirname(os.path.realpath(__file__))
data_file = curpath + '/test_data.yml'    # 拼接
test_demo_data = readyml(data_file)['test_add_project_param_demo']

@allure.feature('添加项目测试用例')
class TestAddProject:

    # # 缺陷划分-一般缺陷
    # @allure.severity('normal')
    # # 关联测试用例
    # @allure.testcase('xxx')
    # # 关联bug
    # @allure.issue('xxx')
    # @allure.title('新增项目：成功')
    # def test_add_project_01(self, login):
    #     ''' 用例描述：1.先登录
    #      2.点击新增项目导航
    #      3.新增项目页输入：项目名称：测试项目04，所属应用：测试应用01， 项目描述：项目描述01
    #      4.点击保存按钮'''
    #     driver = login  # 登录
    #     add_p = AddProject(driver)  # 实例化AddProject页面
    #     add_p.click_classify()
    #     add_p.add(project_name='测试项目06', publish_app='测试应用01', project_desc='项目描述01')
    #     res_add = add_p.is_add_suc(text='测试项目06')
    #     print('是否新增成功：%s' % res_add)
    #     assert res_add  # 断言结果


    @allure.testcase('xxx')
    @allure.issue('xxx')
    @allure.title('新增项目：新增已存在项目名称项目失败')
    def test_add_project_02(self, login):
        ''' 用例描述：已存在 测试项目02
         1.先登录
         2.点击新增项目导航
         3.新增项目页输入：项目名称：测试项目01，所属应用：测试应用02， 项目描述：项目描述01
         4.点击保存按钮'''
        driver = login  # 登录
        add_p = AddProject(driver)  # 实例化AddProject页面
        add_p.click_classify()
        add_p.add(project_name='测试项目02', publish_app='测试应用01', project_desc='项目描述01')
        res_add = add_p.is_add_fail(text='测试项目02')
        print('是否新增失败：%s' % res_add)
        assert res_add  # 断言结果

    # 参数化添加项目demo
    @pytest.mark.parametrize('test_add_demo, expected', test_demo_data)
    def test_add_project_param_demo(self, login, test_add_demo, expected):
        project_name = test_add_demo['p_name']
        publish_app = test_add_demo['pu_app']
        project_desc = test_add_demo['p_desc']
        expected = expected

        dirver = login    # 登录
        add_p = AddProject(dirver)    # 实例化
        add_p.click_classify()
        add_p.add(project_name= project_name, publish_app= publish_app, project_desc= project_desc)
        res_add = add_p.is_add_suc(text= expected)
        print('是否新增成功：%s' % res_add)
        assert res_add  # 断言结果