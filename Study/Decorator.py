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
"""
* 和 **
    实际上，真正的 Python 参数传递语法是 * 和 **。*args 和 **kwargs 只是一种约定俗成的编程实践。我们也可以写成 *vars 和 **kvars。
    这两个是 python 中的可变参数。*args 表示任何多个无名参数，它是一个 tuple，**kwargs 表示关键字参数，它是一个 dict。
    并且同时使用 *args 和 **kwargs 时，必须将 *args 放在 **kwargs 之前。
"""


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
    所以，装饰器装饰函数的时候，是将函数作为变量传入装饰器内部，实际调用的是装饰器内部的函数（添加新功能之后的函数）
    """
    bar = decorator(bar)  # 神奇，函数可以被作为参数传递，也可以接受另外一个函数的返回
    bar()


# test_02()


def modify(func):  # 定义函数装饰器 传入 原本需要执行的函数
    def w(*args):  # 定义 包裹函数 传入 参数，在此函数中，将 装饰器代码 和 原本需要执行的代码 包裹在一起
        logging.warning('%s is running' % func.__name__)  # 装饰器代码
        return func(*args)  # 原版需要执行的代码

    return w  # 把 包裹函数 扔回去


@modify  # 代替 b = modify(b)，Python 中，在函数定义的时候就加上 @+装饰器名字 可以代替赋值语句。
def b(myinput):  # 原版需要执行的函数
    print('-= %s =-' % myinput)


b('WB')


class Foo(object):  # 定义类装饰器
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('\n~~~ -= class decorator runing =- ~~~')
        self._func(*args, **kwargs)
        print('~~~ -= class decorator ending =- ~~~')


@Foo
def d(*args, **kwargs):
    for arg in args:
        print('-= %s =-' % arg)
    if kwargs is not None:
        for key, value in kwargs.items():
            print('{} = {}'.format(key, value))


d('a', 'b', 'c', '1', '2', '3', n1='python', n2='C++', n3='125', n4=125)
d()

s = map(lambda x: 2 * x + 1, range(6))
for i in s:
    print(i)
