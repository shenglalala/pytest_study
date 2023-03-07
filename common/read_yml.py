import yaml
import os

def readyml(yamlpath):
    ''' 读取yaml文件内容
    参数path：相对路径，起始路径：项目的根目录
    realpath：文件的真实路径，绝对路径地址'''
    # os.path.isfile() 判断某一对象是否为文件
    # os.path.isdir() 判断某一对象是否为目录
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError('文件路径不存在: %s'%yamlpath)
    with open(yamlpath, 'r', encoding='utf-8') as f:
        cfg = f.read()
        d = yaml.load(cfg, Loader=yaml.FullLoader)    # load方法转字典
        print('读取数据为：%s'%d)
        return d

if __name__ == '__main__':
    path = '../case/test_data.yml'
    readyml(path)