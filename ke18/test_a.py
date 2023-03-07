import pytest


# 标记为demo
@pytest.mark.demo
# 参数化
@pytest.mark.parametrize('test_input, expected',
                         [['1+3', 4],
                          ['2*3', 6],
                          ['2-3', -1]])
def test_demo(test_input, expected):
    a = test_input
    print(a)
    assert eval(a) == expected


# 标记为web
@pytest.mark.web
# 笛卡尔积
@pytest.mark.parametrize('password', ['', 'admin_pwd', '54321'])
@pytest.mark.parametrize('username', ['', 'amdin', '12345'])
def test_login(username, password):
    print('username: %s, password：%s'%(username, password))
    result = False

    # 期望结果只能取一个，所以结果应一致
    assert not result

# 一一对应
test_data = [({'user': 'admin', 'pwd': 'admin'}, True),
             ({'user': 'admin', 'pwd': '123456'}, False),
             ({'user': 'admin', 'pwd': ''}, False)]
@pytest.mark.parametrize('test_input, expected', test_data)
def test_login1(test_input, expected):
    print('user: %s, pwd: %s'%(test_input['user'], test_input['pwd']))
    result = True    # 实际结果

    assert result == expected