import pytest

@pytest.fixture(scope='session')
def login_ke18():
    print('前置操作：登录')

    yield
    print('后置操作：关闭')