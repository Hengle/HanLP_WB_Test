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
"""
* �� **
    ʵ���ϣ������� Python ���������﷨�� * �� **��*args �� **kwargs ֻ��һ��Լ���׳ɵı��ʵ��������Ҳ����д�� *vars �� **kvars��
    �������� python �еĿɱ������*args ��ʾ�κζ����������������һ�� tuple��**kwargs ��ʾ�ؼ��ֲ���������һ�� dict��
    ����ͬʱʹ�� *args �� **kwargs ʱ�����뽫 *args ���� **kwargs ֮ǰ��
"""


# ��װ����
def test_02():
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.warning('%s is running' % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    def bar():
        print('i am bar')

    """
    ��һ������У��� bar ������Ϊ�������� decorator װ�����У�Ȼ�� bar ������ decorator �еĺ��� wrapper ����ʵ�֣�
    ͬʱ��װ�µĹ��ܣ����µĺ��� wrapper ��Ϊ�������� ������ bar ����ֵ�� ���� decorator װ�ε� wrapper �·�����
    ���ԣ�װ����װ�κ�����ʱ���ǽ�������Ϊ��������װ�����ڲ���ʵ�ʵ��õ���װ�����ڲ��ĺ���������¹���֮��ĺ�����
    """
    bar = decorator(bar)  # ���棬�������Ա���Ϊ�������ݣ�Ҳ���Խ�������һ�������ķ���
    bar()


# test_02()


def modify(func):  # ���庯��װ���� ���� ԭ����Ҫִ�еĺ���
    def w(*args):  # ���� �������� ���� �������ڴ˺����У��� װ�������� �� ԭ����Ҫִ�еĴ��� ������һ��
        logging.warning('%s is running' % func.__name__)  # װ��������
        return func(*args)  # ԭ����Ҫִ�еĴ���

    return w  # �� �������� �ӻ�ȥ


@modify  # ���� b = modify(b)��Python �У��ں��������ʱ��ͼ��� @+װ�������� ���Դ��渳ֵ��䡣
def b(myinput):  # ԭ����Ҫִ�еĺ���
    print('-= %s =-' % myinput)


b('WB')


class Foo(object):  # ������װ����
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
