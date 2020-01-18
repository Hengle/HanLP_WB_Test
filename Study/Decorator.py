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
        def wrapper(*args, **kwargs):
            logging.warning('%s is running' % func.__name__)
            # func()
            return func(*args, **kwargs)
        return wrapper

    def bar():
        print('i am bar')

    bar = use_logging(bar)
    bar()


test_02()
