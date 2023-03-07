import pytest
import random

def test_1(login_ke18):
    print('测试用例1')

def test_2(login_ke18):
    num = random.randint(0, 5)
    print('随机数为：%s'%num)
    assert 5 == num

@pytest.mark.repeat(3)
def test_3(login_ke18):
    print('测试用例3')