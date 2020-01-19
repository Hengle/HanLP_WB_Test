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
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.warning('%s is running' % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    def bar():
        print('i am bar')

    """
    这一句代码中，将 bar 函数作为变量传入 decorator 装饰器中，然后 bar 方法在 decorator 中的函数 wrapper 函数实现，
    同时包装新的功能，将新的函数 wrapper 作为变量返回 ，所以 bar 的新值是 经过 decorator 装饰的 wrapper 新方法。
    """
    bar = decorator(bar)  # 神奇，函数可以被作为参数传递，也可以接受另外一个函数的返回
    bar()


# test_02()


def modify(func):  # 定义函数装饰器 传入 原本需要执行的函数
    def w(*args):  # 定义 包裹函数 传入 参数，在此函数中，将 装饰器代码 和 原本需要执行的代码 包裹在一起
        logging.warning('%s is running' % func.__name__)  # 装饰器代码
        return func(*args)  # 原版需要执行的代码

    return w  # 把 包裹函数 扔回去


@modify  # 代替 b = modify(b)
def b(myinput):  # 原版需要执行的函数
    print('-= %s =-' % myinput)


b('WB')


class Foo(object):  # 定义类装饰器
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('\n~~~ -= class decorator runing =- ~~~')
        self._func(*args)
        print('~~~ -= class decorator ending =- ~~~')


@Foo
def d(myinput):
    print('-= %s =-' % myinput)


d('XXX')
