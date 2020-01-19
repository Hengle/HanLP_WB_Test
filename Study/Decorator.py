#! python3
# coding=gbk
import logging


# 不使用装饰器
def test_01():
    def use_logging(func):
        logging.warning('%s is running' % func.__name__)
        func()

    def foo():
        print('i am foo')

    use_logging(foo)


# test_01()


# 简单装饰器
def test_02():
    def use_logging(func):
        def xxxwrapper(*args, **kwargs):
            logging.warning('%s is running' % func.__name__)
            # func()
            return func(*args, **kwargs)

        return xxxwrapper

    def bar():
        print('i am bar')

    bar = use_logging(bar)  # 神奇，函数可以被作为参数传递，也可以接受另外一个函数的返回
    bar()


# test_02()


def modify(func):  # 传入 原本需要执行的函数
    def w():  # 定义 函数 2，函数 2 只是把 修饰器添加的代码 和 原本要执行的函数的代码 打包到一起
        logging.warning('%s is running' % func.__name__)
        return func()

    return w  # 把打包好的 函数 2 扔回去


@modify  # 代替 b = modify(b)
def b():
    print('-= x =-')  # 原本需要执行的代码


b()
