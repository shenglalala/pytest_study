import pytest
import allure

@allure.step('用例步骤1')
def step1():
    print('用例步骤1')

@allure.step('用例步骤2')
def step2():
    print('用例步骤2')
@allure.step('用例步骤3')
def step3():
    print('用例步骤3')

# 功能模块feature
@allure.feature('功能模块1')
class TestDemo:
    ''' 功能模块描述  '''

    @allure.title('测试用例标题')
    def test_1(self,login):
        ''' 用例描述'''
        step1()

    @allure.story('测试用例story1')
    def test_2(self, login):
        step2()
        step3()

    @allure.story('测试用例story2')
    def test_3(self, login):
        step1()
        step2()
        step3()