#! python3
# coding=gbk
import logging


# ��ʹ��װ����
def test_01():
    def use_logging(func):
        logging.warning('%s is running' % func.__name__)
        func()

    def foo():
        print('i am foo')

    use_logging(foo)


# test_01()


# ��װ����
def test_02():
    def use_logging(func):
        def xxxwrapper(*args, **kwargs):
            logging.warning('%s is running' % func.__name__)
            # func()
            return func(*args, **kwargs)

        return xxxwrapper

    def bar():
        print('i am bar')

    bar = use_logging(bar)  # ���棬�������Ա���Ϊ�������ݣ�Ҳ���Խ�������һ�������ķ���
    bar()


# test_02()


def modify(func):  # ���庯��װ���� ���� ԭ����Ҫִ�еĺ���
    def w(*args):  # ���� �������� ���� �������ڴ˺����У��� װ�������� �� ԭ����Ҫִ�еĴ��� ������һ��
        logging.warning('%s is running' % func.__name__)  # װ��������
        return func(*args)  # ԭ����Ҫִ�еĴ���

    return w  # �� �������� �ӻ�ȥ


@modify  # ���� b = modify(b)
def b(myinput):  # ԭ����Ҫִ�еĺ���
    print('-= %s =-' % myinput)


b('WB')


class Foo(object):  # ������װ����
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator runing ----------')
        self._func()
        print('class decorator ending ----------')


@Foo
def d():
    print('-= i am d =-')


d()
