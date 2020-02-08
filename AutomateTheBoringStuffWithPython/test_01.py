#! python3
# coding=gbk

import pprint
import copy
import re
import os
from pathlib import Path
import shelve
import json

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('������')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def test_01():
    name = ''
    while name != 'WB':
        print('Please type your name.')
        name = input()
    print('Thank you!')


# test_01()


def test_02():
    name = ''
    print('Enter your name:')
    while not name:
        name = input()

    print('How many guests will you have?')
    num = int(input())
    if num:
        print('Be sure to have enough room for all your guests.')
    print('Done')
    print("DDD")


# test_02()


def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'


# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for x in range(9):
#   print(getAnswer(random.randint(1, 9)))


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('ȫ�ֱ����������������')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

eggs = 10


def test_03():
    print("Hello", end=' ')
    print("World", 'x', 'y', sep=' -*- ')
    #   print(eggs)
    global eggs


#    eggs = 3
#    print(eggs)

# test_03()
# print('~~~')
# print(eggs)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('try ... except ... �﷨ѧϰ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def spam4(divide_by):
    return 42 / divide_by


def spam5(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam5(2))
print(spam5(12))
print(spam5(0))
print(spam5(1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('�����ǳ���������Ƕ��Ƕ��ڿɱ����ݵĲ���������ȥ�����ã�ǳ����ȥ��ǳ�����ȥ����')


def eggs2(some_parameter):
    some_parameter.append('Hello')
    print(some_parameter)


string3 = [1, ['x', 'y', 'z'], 3]
# string3 ����Ϊ�������ݸ����� eggs2() ��ζ������ֵ�����Ƹ��� someParameter ������ע�⣬
# string3 �д洢�����б�����ã����ԣ�����ֱ���޸���������ָ���б�
# eggs2(string3)
cheese = copy.copy(string3)
cheese[0] = 100
print(cheese)
print(string3)
# eggs2(copy.deepcopy(string3))
# print(string3)
print('-------------------')
a = [1, 2, 3, 4, ['a', 'b']]  # ԭʼ����
b = a  # ��ֵ�������������
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('����ʵ�� 4.10.1 ���Ŵ���')


def xxx(input1):
    s = ''
    for i in range(len(input1)):
        if i == len(input1) - 1:
            s += 'and ' + input1[i]
        else:
            s += input1[i] + ", "
    print(s)


string2 = ['apples', 'bananas', 'tofu', 'cats', 'a', 'b', 'c', 'd']
xxx(string2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('����ʵ�� 4.10.2 �ַ�ͼ����')
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('|===================|')
row_num = len(grid)
array_num = len(grid[0])
for y in range(array_num):
    print('|', end=' ')
    for x in range(row_num):
        print(grid[x][y], end=' ')
    print('|')
print('|===================|')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('With ... As ... �﷨�о�')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

"""
with as �﷨��˵����

    with open(r'c:\test.txt', 'r') as f:
        data = f.read()

with ����ӵĶ��󷵻صĽ����ֵ�� f���� open �������ص��ļ�����ֵ���� f��with �����ѻ�ȡ�����ļ����쳣��Ϣ��
with ������������أ�
with ���淵�صĶ���Ҫ�������__enter__()/__exit__()���������������ļ�����f�պ����������������ģ���Ӧ�����硣

python�йٷ�����˵������(https://docs.python.org/2/reference/datamodel.html#context-managers)��

    object.__enter__(self)
    ������˶�����ص�����ʱ�����ġ�with��佫���˷����ķ���ֵ�󶨵�����AS�Ӿ���ָ����Ŀ�꣨��������õĻ���
 
    object.__exit__(self, exc_type, exc_value, traceback)
    �˳���˶�����ص�����ʱ�����ġ��������������������˳����쳣���������������ʱû���쳣��������ô��������������ΪNone��
    ������쳣���������Ҹ÷���ϣ�������쳣������ֹ����������������Ӧ�÷���True�������쳣�����˳��÷���ʱ��������
 
    ��ע��, __exit__()������Ӧ�������׳�������쳣�����ǵ����ߵ�ְ��
"""


class Test:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    @staticmethod
    def do_something():
        global x
        x = 1 / 0
        print('do something!')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__() is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_value}')
        print(f'trace:{traceback}')
        print('__exit()__ is call!')
        # ������쳣���������Ҹ÷���ϣ�������쳣�׳�������ֹ����������������Ӧ�÷���True��
        # �����쳣�����˳��÷���ʱ��������
        return True


with Test() as sample:
    sample.do_something()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('������ �ֵ�ͽṹ������')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def dictionary_test():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)
    pprint.pprint(count)
    # print(pprint.pformat(count))
    sss = {'aaaaaaaaaaaaaaaaaaaaaaaa': 1, 'bbbbbbbbbbbbbbbbbbbbbbbb': 2, 'cccccccccccccccccccccccc': 1}
    pprint.pprint(sss)


dictionary_test()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('�ֵ䣬����ʵ���罨ģ����������')
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def turn_board():
    turn = 'X'
    for i in range(9):
        print('----------------------------------')
        if i == 0:
            print('��ʼ���״̬')
        print_board(theBoard)
        print('----------------------------------')
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    print('----------------------------------')
    print('�������״̬')
    print_board(theBoard)
    print('----------------------------------')


# turn_board()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Ƕ�׵��ֵ���б�')


def use_get():
    # �ڷ���һ������ֵ֮ǰ�����ü��Ƿ�������ֵ��У�����鷳�����ڣ��ֵ���һ�� get()������
    # ��������������Ҫȡ����ֵ�ļ����Լ�����ü�������ʱ�����صı���ֵ��
    picnic_items = {'apples': 5, 'cups': 2}
    print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
    print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')


# �ֵ䣬�������˴����Ķ���
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    # �������п��˴�����ĳ��ʳ�������
    num_brought = 0
    for k, v in guests.items():  # �ַ�����Ķ��ظ�ֵ
        num_brought = num_brought + v.get(item, 0)
    return num_brought


def calculate_food():
    food = {}
    # ͳ��ʳ�������
    for guest_items in all_guests.items():
        for food_name in guest_items[1].keys():
            food.setdefault(food_name, 0)
    print(food)  # չʾ����ʳ������
    for food_name in food.keys():
        print(' ' + food_name + ' = ', end='')
        print(total_brought(all_guests, food_name), end='')
        print(', ', end='')
    print()


calculate_food()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('������Ϸ����Ʒ�嵥')

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inv, left_width, right_width):
    print(''.center(left_width + right_width, '~'))
    print('Inventory:'.center(left_width + right_width))
    print(''.center(left_width + right_width, '~'))
    total = 0
    for k, v in inv.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width, '.'))
        total += v
    print(''.center(left_width + right_width, '~'))
    print('total = '.ljust(left_width, '.') + str(total).rjust(right_width, '.'))


display_inventory(inventory, 10, 6)
print('=============================')


def add_to_inventory(inv, added_items):
    for item in added_items:
        print(item)
        inv.setdefault(item, 0)  # item ����ʱ��������ֵ��������������������ֵΪ0
        inv[item] += 1


add_to_inventory(inventory, dragon_loot)
display_inventory(inventory, 10, 10)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('������ �ַ�������')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

string1 = r'asd\'\
ss\
egg'

print(string1)


def multi_line_comment():
    """
    �˶���ע������˵��
    multi_line_comment()������;��
    """
    print('Hello!')


# multi_line_comment()


def string_cut():
    spam = 'Hello, World!'
    print(spam[0])
    print(spam[4])
    print(spam[-1])
    print(spam[0:5])
    print(spam[:2])
    print(spam[5:])
    print(spam[:])
    print(spam.lower())
    print(spam.upper())
    print(spam)


string_cut()


def input_age():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')


# input_age()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('����ӡ')
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def grid(data):
    print('������������������������������������������������')
    length_max = [0] * len(table_data)
    for i in range(table_data.__len__()):
        for j in range(table_data[0].__len__()):
            if table_data[i][j].__len__() > length_max[i]:
                length_max[i] = table_data[i][j].__len__()
        print(length_max[i])

    print('������������������������������������������������')
    for j in range(table_data[0].__len__()):
        for i in range(table_data.__len__()):
            if i == 0:
                print(data[i][j].rjust(length_max[i], ' '), end=' ')
            else:
                print(data[i][j].ljust(length_max[i], ' '), end=' ')
        print('')
    print('������������������������������������������������')


grid(table_data)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('������ ģʽƥ����������ʽ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def is_phone_number(text):  # ����������ʽ���ǳ�����
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def use_is_phone_number():
    print(is_phone_number('123-456-7890'))

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i + 12]
        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)
    print('Done')


# use_is_phone_number()

r"""
�Ƚ������Ĳο��ĵ���https://www.jianshu.com/p/bb7d5386507c��https://deerchao.cn/tutorials/regex/regex.htm
������ʽ�Ļ����÷���

1�������ŷ��飺r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
    ͨ�����ſ��Խ�ƥ�䵽���ı����飬��һ�������ǵ�1�飬�ڶ��������ǵ�2�顣��group()��������1����2���Ϳɻ�ȡƥ���ı��Ĳ�ͬ����

2���ùܵ�ƥ��������
    �ַ�|��Ϊ���ܵ��������С����ߡ��ĺ��塣������ʽ r'Batman|Tina Fey'��ƥ��'Batman'��'Tina Fey'��
    ��� Batman �� Tina Fey �������ڱ����ҵ��ַ����У���һ�γ��ֵ�ƥ���ı�������Ϊ Match ���󷵻ء�
    
3�����ʺű�ʾ��ǰ��ķ����ǿ�ѡ�ģ�ע�⣬����ı�ʾ������ʹ������
    �������Ϊ ? ����˵����ƥ������ʺ�֮ǰ�ķ�����λ�һ�Ρ���

4�����Ǻ� * ��ʾƥ����֮ǰ�ķ�����λ��Σ�ע�⣬����ı�ʾ������ʹ������

5���üӺ� + ��ʾƥ����֮ǰ�ķ���һ�λ��Σ�ע�⣬����һ��

6���û����� {} ƥ����ǰ��ķ��� �ض�������(Ha){3} == 'HaHaHa'
    ����һ�����֣�������ָ��һ����Χ�����ڻ�������д��һ����Сֵ��һ�����ź�һ�����ֵ��
    (Ha){3,5} ��ƥ�� 'HaHaHa'��'HaHaHaHa'��'HaHaHaHaHa'��
    (Ha){3,}  ��ƥ�� 3 �λ�����ʵ����
    (Ha){,5}  ��ƥ�� 0 �� 5 ��ʵ����
    ������һ�����⣬'HaHaHa'��'HaHaHaHa'Ҳ�ܹ���Ч��ƥ��������ʽ(Ha){3,5}����ʵ���Ϸ��ص���'HaHaHaHaHa'��
    Python ��������ʽĬ���ǡ�̰�ġ��ģ����ʾ���ж��������£����ǻᾡ����ƥ������ַ�����
    �����ŵġ���̰�ġ��汾ƥ�価������̵��ַ��������ڽ����Ļ����ź����һ���ʺţ�re.compile(r'(Ha){3,5}?')��
    ��ע�⣬�ʺ���������ʽ�п��������ֺ��壺������̰��ƥ����ʾ��ѡ�ķ��顣�����ֺ�������ȫ�޹صġ�
    
7����Ϊ findall() �����ķ��ؽ�����ܽᣬ���ס�������㣺
    1�����������һ�� û�� �����������ʽ�ϣ�����\d\d\d-\d\d\d-\d\d\d\d��
    ����findall()������һ��ƥ���ַ������б� ����['415-555-9999', '212-555-0000']��
    2�����������һ�� �� �����������ʽ�ϣ�����(\d\d\d)-(\d\d\d)-(\d\d\d\d)��
    ����findall()������һ���ַ�����Ԫ����б�(ÿ�������Ӧһ���ַ���)������[('415', '555', '1122'), ('212', '555', '0000')]��
    
8���ַ��������д���� https://blog.csdn.net/weixin_40693324/article/details/78785608

9����λ�� ^ �� $
    ������������ʽ�Ŀ�ʼ��ʹ�ò�����ţ�^��������ƥ����뷢���ڱ������ı���ʼ����
    ���Ƶأ�������������ʽ��ĩβ������Ԫ���ţ�$������ʾ���ַ������������������ʽ��ģʽ������
    ����ͬʱʹ��^��$�����������ַ�������ƥ���ģʽ��Ҳ����˵��ֻƥ����ַ�����ĳ���Ӽ��ǲ����ġ�

10��ͨ��� .
    ��ʾ���з� \n �������е��ַ�

11��ʹ�� sub() ���������滻�ַ���

12��ʹ�� re.VERBOSE ���� �� re.compile() ����������ʽ�еĿհ׺�ע�͡�
    ����ζ�ţ���ʱ����ͨ�����в����ע�ͣ���������⸴�ӵ�������ʽ��
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    �ַ�����    ʾ��
    ������������������������������������������������������������������������������������������������������������������������
    ת���      \
    һ���ַ�    \d, \D, \w, \W, \xn, \num, \n, \nm, \nml, \un, .
    �ַ�����    x|y, [xyz], [^xyz], [a-z], [^a-z]
    �Ǵ�ӡ�ַ�  \cx, \f, \n, \r, \s, \S, \t, \v
    ��λ��      ^, $, \b, \B
    �޶���      *, +, ?, ?(����), {n}, {n,}, {n,m}
    ƥ��        (pattern), (?:pattern)
    ������    (?=pattern), (?!pattern), (?<=pattern), (?<!pattern)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ��������     ����
    ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������
    \d          == [0-9] 0 �� 9 ���κ�����
    \D          == [^0-9] �� 0 �� 9 ������������κ��ַ�
    \w          == [A-Za-z0-9_] �κ���ĸ�����ֻ��»����ַ���������Ϊ��ƥ�䡰���ʡ��ַ���
    \W          == [^A-Za-z0-9_] ����ĸ�����ֺ��»���������κ��ַ�
    \s          == [ \f\n\r\t\v] �ո��Ʊ�����з���������Ϊ��ƥ�䡰�հס��ַ���
    \S          == [^ \f\n\r\t\v] ���ո��Ʊ���ͻ��з�������κ��ַ�
    
    ^           ����ƥ��
    ?           0 �� 1 �� 
    *           0 �� ��� 
    +           1 �� ���
    \           ����һ���ַ����Ϊһ�������ַ�����һ��ԭ���ַ�����һ��������á���һ���˽���ת���
    $           ƥ�������ַ����Ľ���λ�á����������RegExp ����� Multiline ���ԣ�$ Ҳƥ�� '\n' �� '\r' ֮ǰ��λ
    .           �� "\n" ֮����κε����ַ���Ҫƥ����� '\n' ���ڵ��κ��ַ�����ʹ���� '[.\n]' ��ģʽ

    ()          ��Ϊ����ȡƥ����ַ��������ʽ���м���()���м�����Ӧ��ƥ���ַ�����(\s*)��ʾ�����ո���ַ���
    []          �Ƕ���ƥ����ַ���Χ������ [a-zA-Z0-9] ��ʾ��Ӧλ�õ��ַ�Ҫƥ��Ӣ���ַ������֡�[\s*]��ʾ�ո����*��
    [^x]        x ����������ַ�
    [^aeiou]	����aeiou�⼸����ĸ����������ַ�
    {}          һ��������ʾƥ��ĳ��ȣ����� \s{3} ��ʾƥ�������ո�\s{1,3}��ʾƥ��һ�������ո�
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# 1�������ŷ���
print('��������������������������������\n1��ʹ�����ţ�\n��������������������������������')
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
area_code, main_number = mo.groups()
print(area_code, main_number)

# 2���ܵ����� | ��ʾ�����ߡ������ص�һ��ƥ�䵽���ı�
print('��������������������������������\n2��ʹ�ùܵ���\n��������������������������������')
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey, Batman.')  # �����ҵ��ĵ� 1 ��
print(mo1)
print(mo1.group())
print(mo1.group(0))
# print(mo1.group(1))     # ����
mo2 = hero_regex.findall('Batman and Tina Fey, Batman.')
print(mo2)
print('~~~~~~~~~~~~~~~~~~')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')  # �����ҵ��ĵ� 1 ����ע�����ŵ�ʹ��
mo3 = batRegex.search('xBatmobilex lost a wheel xBatbatx')
print(mo3)
print(mo3.group())
print(mo3.group(0))  # ��ȫƥ����ı�
print(mo3.group(1))  # ������ƥ����ı�

# 3�����ʺ� �� ��ʾ ����ѡ" ��ƥ��
print('��������������������������������\n3��ʹ���ʺţ�\n��������������������������������')
batRegex = re.compile(r'Bat(wo)?man')
mo4 = batRegex.search('The Adventures of Batman')
mo5 = batRegex.search('The Adventures of Batwoman')
print(mo4.group())
print(mo5.group())
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneRegex.search('My number is 415-555-4242')
mo7 = phoneRegex.search('My number is 555-4242')
print(mo6.group())
print(mo7.group())

# 4�����Ǻ� * ��ʾ ƥ����ǰ��ķ��� ��� �� ���
print('��������������������������������\n4��ʹ���Ǻţ�\n��������������������������������')
batRegex = re.compile(r'Bat(wo)*man')
mo8 = batRegex.search('The Adventures of Batman')
mo9 = batRegex.search('The Adventures of Batwoman')
mo10 = batRegex.search('The Adventures of Batwowowowoman')
print(mo8.group())
print(mo9.group())
print(mo10.group())

# 5�����Ǻ� + ��ʾ ƥ����ǰ��ķ��� һ�� �� ��Σ�����һ��
print('��������������������������������\n5��ʹ�üӺţ�\n��������������������������������')
batRegex = re.compile(r'Bat(wo)+man')
mo11 = batRegex.search('The Adventures of Batman')
mo12 = batRegex.search('The Adventures of Batwoman')
mo13 = batRegex.search('The Adventures of Batwowowowoman')
print(mo11)  # ���� None��print(mo11.group()) �����
print(mo12.group())
print(mo13.group())

# 6���û����� {} ƥ����ǰ��ķ��� �ض�����
print('��������������������������������\n6��ʹ�û����ţ�\n��������������������������������')
haRegex = re.compile(r'(Ha){3}')
mo14 = haRegex.search('HaHaHa')
mo15 = haRegex.search('Ha')
print(mo14.group())
print(mo15)
print('���������������� ̰�ģ���̰�� ����������������')
greedy_Ha_regex = re.compile(r'(Ha){3,5}')  # ̰����ʽ��Ĭ��
mo16 = greedy_Ha_regex.search('HaHaHaHaHa')
non_greedy_Ha_regex = re.compile(r'(Ha){3,5}?')  # ��̰����ʽ���� ?
mo17 = non_greedy_Ha_regex.search('HaHaHaHaHa')
print(mo16.group())
print(mo17.group())

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print('.findall() ����')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# ['415-555-9999', '212-555-0000']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# [('415', '555', '9999'), ('212', '555', '0000')]

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print('�ַ�����')
xmasRegex = re.compile(r'\d+\s\w+')
pprint.pprint(xmasRegex.findall('01 drummers, 02 pipers, 03 lords, 04 ladies, 05 maids, 06 swans, '
                                '07 geese, 08 rings, 09 birds, 10 hens, 11 doves, 12 partridge'))

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print('�Զ����ַ�����')
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print(r'��λ�� ^, $')
beginsWithHello = re.compile(r'^Hello')  # ��ʾ�� Hello ��ͷ���ı�
print(beginsWithHello.search('Hello world!'))  # <re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.'))  # None

endsWithNumber = re.compile(r'\d$')  # ��ʾ�����ֽ���
endsWith2Numbers = re.compile(r'\d{2}$')  # ��ʾ��2�����ֽ���
endsWith3Numbers = re.compile(r'\d{3}$')  # ��ʾ��3�����ֽ���
print(endsWithNumber.search('test23'))  # <re.Match object; span=(5, 6), match='3'>
print(endsWith2Numbers.search('test23'))  # <re.Match object; span=(4, 6), match='23'>
print(endsWith3Numbers.search('test23'))  # None

wholeStringIsNum = re.compile(r'^\d+$')  # ��ͷ��β������������ɣ�����Ҫ��1������
wholeStringIsNum2 = re.compile(r'^\d*$')  # ��ͷ��β������������ɣ�������0������
print(wholeStringIsNum.search('1234567890'))  # <re.Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890'))  # None
print(wholeStringIsNum.search('12 34567890'))  # None
print(wholeStringIsNum.search(''))  # None
print(wholeStringIsNum2.search(''))  # <re.Match object; span=(0, 0), match=''>

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print(r'ͨ��� .')
atRegex = re.compile(r'.at')  # ƥ�� �����ַ� + 'at'
print(atRegex.findall('The cat in the hat sat on the flat mat.'))  # ['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: .* Last Name: .*')  # ��Ȼ��.* ָ�����ַ�
mo18 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo18.group())  # ��ȡ�������ַ���
print('����������������ʹ�÷��顪��������������')
nameRegexGroup = re.compile(r'First Name: (.*) Last Name: (.*)')  # ͨ�����ţ������Եõ������ַ�
mo19 = nameRegexGroup.search('First Name: Al Last Name: Sweigart')
print(mo19.group())
print(mo19.group(0))  # == mo19.group()
print(mo19.group(1))
print(mo19.group(2))
print(mo19.groups())
print('����������������̰��/���衪��������������')
greedyRegex = re.compile(r'<.*>')  # ̰��ģʽ
print('̰��ģʽ��' + greedyRegex.search('<To serve man> for dinner.>').group())  # <To serve man> for dinner.>
nongreedyRegex = re.compile(r'<.*?>')  # ����ģʽ
print('����ģʽ��' + nongreedyRegex.search('<To serve man> for dinner.>').group())  # <To serve man>
print('������������������ƥ�任�С���������������')
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print('����������������ƥ�任�С���������������')
newlineRegex = re.compile('.*', re.DOTALL)  # ��2������ re.DOTALL ��ʵ���� DotAll ��ʾ . ƥ�������ַ�����������
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print('�������������������Դ�Сд����������������')
robocop = re.compile(r'robocop', re.I)  # �ڶ������� re.I ���� re.IGNORECASE ��ʾ���Դ�Сд
print(robocop.search('RoboCop is part man, part machine, all cop.').group())  # 'RoboCop'

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print('�� sub() �����滻�ַ���')
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent \w(\w)\w*')  # 'Agent (һ�������ַ�)�����ַ�'
print(agentNamesRegex.sub(r'*\1***',
                          'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

print('������������������������������������������������������������������������������������������������������������������������������������������������������������������������')
print('ʹ�� re.VERBOSE')
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')  # ���ö�ô��

phoneRegex2 = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # ���ţ�3�����֣������������3�����֣����߲�����
    (\s|-|\.)?                      # �ո񣬻���-������.�����߲�����
    (\d{3})                         # ǰ3������
    (\s|-|\.)                       # �ո񣬻���-������.
    (\d{4})                         # ��4������
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # (�л������ɿո� + �����ڵ�ext����x����ext. + �л������ɿո� + 2~5������)?
)''', re.VERBOSE)

for phoneNum in phoneRegex2.findall('as 425-589-4885, (110)258.6255, 358-4568 x 25531, '
                                    '234 0988, 110-258-1254 ext. 2586'):
    print(phoneNum[0])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('�ڰ��� ��д�ļ�')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(os.path.join('usr', 'bin', 'spam'))

print('������������������������·����������������������')
code_home = os.getcwd()  # �����ʼ����·�������������ڵ�·��
print(code_home)

print('���������������������л�����·����������������������')
download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')  # ��ȡ��ǰ�û�·��
print('�л���Ŀ��·����' + download_dir)  # C:\Users\bwang\Downloads
os.chdir(download_dir)  # ������·���л��������ļ���

print('������������������������·�������·����������������������')
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.relpath(r'C:\Windows', '.'))

print('���������������������л�Ĭ�Ϲ���·����������������������')
os.chdir(code_home)  # �л�Ĭ�Ϲ���·��
print(os.getcwd() + '\n')  # ȷ��

print('����������������������ȫ�����ļ��С�������������������')
# os.makedirs(os.path.join(download_dir, 'test1'))
Path(os.path.join(download_dir, 'test')).mkdir(parents=True, exist_ok=True)  # ��ȫ�Ĵ����ļ���

print('���������������������ֽ�path��������������������')
testpath = os.path.join(download_dir, 'test.txt')
print(os.path.basename(testpath))
print(os.path.dirname(testpath))
print(os.path.split(testpath))
print(testpath.split(os.path.sep))  # �������Ƿֽ��ַ�������������� os.path.sep == \ (windowsϵͳ)
print(os.path.sep)

print('���������������������鿴�ļ���С���ļ������ݡ�������������������')
print(os.path.getsize(os.path.join(download_dir, 'PBSetup70.exe')) / 1)  # ָ���ļ��Ĵ�С���ֽ�
print(os.listdir(download_dir))  # �ļ����е�����
print(os.path.getsize(os.path.join(download_dir, 'test')) / 1)  # ָ���ļ��Ĵ�С���ֽ�

totalSize = 0
for filename in os.listdir(download_dir):
    totalSize = totalSize + os.path.getsize(os.path.join(download_dir, filename))
print(str(round(totalSize / 1024 / 1024, 1)) + 'M')  # ֻ�����ļ���û���ļ���

print('�����������������������·����Ч�ԡ�������������������')
# print(os.path.exists(r'C:\Windows'))
# print(os.path.exists(r'C:\sometest'))

print('�������������������������ļ���д���ı�����ȡ�ı���������������������')
'''
open() �ĵڶ�����������ʹ�ã�
'r'  ֻ��ģʽ��Ĭ��ֵ
'w'  ��дģʽ��ֻ��д�����ܶ�����ͷ��ʼд������֮ǰ�Ѿ����ڵ�����
'a'  ���ģʽ���������ļ�ĩβ׷������
'r+' ��дģʽ���ɶ���д
����ļ������ڣ���ֻ����ʽ�򿪣��ᱨ���Ը�д/׷�ӵ�ģʽ�򿪣��ᰴ�����ִ���һ�����ļ���
��Ҫ����close()�����ر��ļ��󣬲����ٴδ򿪸��ļ���
'''
file = 'wb.txt'
with open(os.path.join('./data', file), 'w') as f:  # ֻ��д�����ܶ���'r+' �����½��ļ�
    f.write('xX=WB=Xx\n   \n_sss_!')
    print('f = ' + str(f))
    print('type(f) = ' + str(type(f)))

# with open(os.path.join(download_dir, file), 'r+') as f:
with open(os.path.join('./data', file), 'r+') as f:
    f.seek(0)  # ֮ǰд����α�ͣ���ļ�ĩβ����ҪŲ����ͷ
    print('��ȡ�����ı�����Ϊһ���ַ�����\n��������������������������������������������������������\n' + f.read())  # ����ƪ�����ص���һ���ַ���
    f.seek(0)  # ������α��ֻ�ͣ���ļ�ĩβ����ҪŲ����ͷ
    print('\n��ȡ�����ı������д����б�\n��������������������������������������������������������\n' + str(f.readlines()))  # �����У����д����б�
    f.seek(0)  # ���α����õ��ļ���ͷ
    print('\n�Ӵ��α�λ�ÿ�ʼ����һ���ı����������з���\n��������������������������������������������������������\n'
          'start -=| ' + f.readline(100) + ' |=- end')  # ����һ��

# open(os.path.join(download_dir, 'xxx'), 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\bwang\\Downloads\\xxx'

print('���������������������� shelve ģ�鱣�������������������������')
shelfFile = shelve.open('data/wb_data')  # �����ļ��������ص���һ�� shelfFile ������һ���ֵ䣬���������б����ֵ��
shelfFile['cats'] = ['Z', 'P', 'S']
shelfFile.close()

sf = shelve.open('data/wb_data')  # ���´��ļ�
print(list(sf.keys()))
print(list(sf.values()))
print(sf['cats'])  # ��֤�����Ƿ���ȷ����
shelfFile.close()  # �ر��ļ�

# ��������
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('myCats.py', 'w')  # ����һ���ļ�
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
# ��ʱ���ı��е������ǣ�"cats = [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
# pprint.pformat() �������ı��ĸ�ʽ���������Ķ���ͬʱҲ���﷨����ȷ�� python ���룬����ֱ�ӵ���ʹ�á�

# import myCats  # ����ִ��ͨ��

# print(myCats.cats)
# print(myCats.cats[0])
# print(myCats.cats[0]['name'])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('�ھ��� ��֯�ļ�')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('��ʮ���� JSON')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
print(json.loads(stringOfJsonData))

# ���д�ӡ�˷��ھ���
"""
print("\n".join(
    "\t".join(["{} * {} = {}".format(y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)
))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for x in range(1, 10):
    print('\t'.join(['{} * {} = {}'.format(y, x, x * y) for y in range(1, x + 1)]))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
"""


# ==========================================
# Python ��̴����ŵ�ʵ�� 2016.pdf
# ==========================================
# ���������
# ��
class Person:
    pass  # �մ����


p = Person()  # ʵ����һ����
print(p)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# ����̨����
# <__main__.Person object at 0x000002AAADF3F9C8>
# ����ζ�ţ�Person ��� __main__ ģ����ӵ����һ��ʵ��������ʾ�����ʵ�����ڴ��ַ

class Person2:
    def __init__(self, name):  # ���ڳ�ʼ����__init__ ����������Ķ���ʵ������Instantiated��ʱ��������
        self.name = name  # ʵ������/�������

    radius = 42  # �����

    def say_hi(self):  # Ĭ�ϣ�ʵ����������ʹ��ʵ��������
        print('~~~~~~~~~ Hi! %s!' % self.name)

    @staticmethod  # ��̬���������ַ�������ʹ���������ص��κζ�����û�� self ���� cls ����
    def my_add(xa, ya):
        return xa + ya

    @classmethod  # �෽�������ַ������ǰ󶨵����ʵ���ϵģ����ǰ󶨵����ϵģ����Բ��ܴ����ʵ���ϵ���
    def get_radius(cls):
        return cls.radius


wb = Person2('WangBo')
wb.say_hi()
wzy = Person2('WangZhiYuan')
wzy.say_hi()

print(Person2)  # �� <class '__main__.Person2'>
print(Person2.my_add(3, 6))  # ͨ���������þ�̬����

print(Person2('xxx'))  # ���ʵ�� <__main__.Person2 object at 0x000001EB0B9E7948>
print(Person2('xxx').my_add(3, 6))  # ͨ�����ʵ�������þ�̬������Ҳ�ǿ��Եģ�����û�б�Ҫ����Ϊ���˷���Դ

print(Person2.get_radius())  # ������� 42
xxx = Person2('xxx')  # ����һ�����ʵ����ע�⣬���� xxx = Person2
xxx.radius = 100  # �޸�ʵ��������Ϊ 100
print(xxx.radius)  # ��ȡʵ��������
print(xxx.get_radius())  # �෽����ȡ������Ȼ��������ԣ�������ʵ��������

Person2.radius = 1  # �޸������
print(xxx.radius)  # ʵ���ı���������ű�
yyy = Person2('yyy')  # ʵ����һ������
print(yyy.radius)  # ��������ָ��ƹ�����ʵ������

# ���ԣ��κ�����£�get_radius() ���ǰ󶨵� �� �ϵġ�
# ��ô������෽����������ʲô���أ�������ʲôʱ��Ż�ȥ������? ���������������ȥ���ĵġ�
"""
(1)�����������������ڴ������ʵ��������һЩԤ����
���ʹ��@staticmethod���棬�����ǲ��ò�Ӳ���� Pizza �����ں����У���ʹ���κμ̳� Pizza ���඼����ʹ����������������������Լ��á�

class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients
 
    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())

(2)�����þ�̬�ࣺ������һ����̬������ֳɶ����̬������������ʹ���෽���������㻹�ǵ�Ӳ����������
ʹ�����ַ�ʽ����������Pizza ��������Զ�������ڱ�ֱ�����ã��̳кͷ������Ƕ����������Ĺ�����

class Pizza(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
 
    @staticmethod
    def compute_area(radius):
         return math.pi * (radius ** 2)
 
    @classmethod
    def compute_volume(cls, height, radius):
         return height * cls.compute_area(radius)
 
    def get_volume(self):
        return self.compute_volume(self.height, self.radius)
"""


class Robot:
    """��ʾ��һ���������ֵĻ����ˡ�"""
    # һ����������������������˵�����
    population = 0

    def __init__(self, name):
        """��ʼ������"""
        self.name = name  # ������������� self ӵ��
        print("���ڳ�ʼ�� {} ...".format(self.name))

        # ���������� +1
        Robot.population += 1

    def die(self):
        """�ҹ���"""
        print("{} ���ڱ�����".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} �����һ���ˡ�".format(self.name))
        else:
            print("���� {:d} ���������ڹ�����".format(Robot.population))

    def say_hi(self):
        """���Ի����˵��ʺ�"""
        print("���ã��ҵ����ˣ������ {}".format(self.name))

    @classmethod
    def how_many(cls):
        """��ӡ��ǰ�����˵�����"""
        print("���������� {} ���������ڹ���".format(cls.population))

    @staticmethod
    def h_m():
        print("{}".format(Robot.population))

    @staticmethod
    def print_class_doc():
        print(Robot.__doc__)

    @staticmethod
    def print_say_hi_doc():
        print(Robot.say_hi.__doc__)


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('\n�����˹�����...\n')

print('�����Ѿ���ɣ��������ٻ�����')

droid1.die()
droid2.die()
Robot.how_many()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
Robot.h_m()
Robot.print_class_doc()
Robot.print_say_hi_doc()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class SchoolMember:
    """����ѧУ����κγ�Ա��"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """������ϸ�ڡ�"""
        print('Name:{} Age:{}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """����һλ��ʦ��"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{:d}'.format(self.salary))


class Student(SchoolMember):
    """����һλѧ����"""

    def __init__(self, name, age, marks):
        # SchoolMember.__init__(self, name, age)
        super().__init__(name, age)  # ������һ�е�������ͬ
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{:d}'.format(self.marks))


m = SchoolMember('Nobody', 0)
t = Teacher('WangBo', 42, 30000)
s = Student('WangZhiYuan', 7, 75)

# ��ӡһ�пհ�
print()

members = [m, t, s]
for member in members:
    member.tell()

t = 'a', 'b'
print(type(t))

print(dict(zip('abc', range(3))))
print(dict(zip(range(3), 'abc')))


def describe_pet(pet_name, animal_type='dog'):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet(pet_name='harry2', animal_type='hamster')
describe_pet('harry', 'hamster')
describe_pet('xxx')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('�� Python Cookbook ������������v3.0.0 2017')
# ==========================================
# Python Cookbook ����������v3.0.0 2017.pdf
# ==========================================
# �����£���������������
print(' �����£���������������')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def manual_iter():
    with open(r'c:\LibAntiPrtSc_INFORMATION.log') as fi:
        try:
            while True:
                line = next(fi)  # ���� next(iterator[, default]) ���ص���������һ��
                print(line, end='')
        except StopIteration:  # StopIteration��ʾ��������
            pass

        print('~~~~~ ��һ��д��~~~~~')
        fi.seek(0)  # �ص��ļ���ͷ
        while True:
            line = next(fi, None)  # ���� next(iterator[, default]) ���ص���������һ��
            if line:
                print(line, end='')
            else:
                print('-=WB=-')
                break


manual_iter()


# �������
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):  # �� print() ������������
        return 'Node value = {!r}'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):  # �� for in ���������б� self._children ��
        return iter(self._children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)


# ��������������
def my_range(start, stop, increment):
    my_x = start
    while my_x < stop:
        yield my_x  # ������
        my_x += increment


for n in my_range(0, 4, 0.5):
    print(n)

x = (my_range(0, 4, 0.5))
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(list(my_range(0, 4, 0.5)))

"""
========
������Э��
========
1��������Ҫ�ṩ __next__ ��������Ҫô������һ�Ҫô����һ�� StopIteration �쳣
2��pythonҪ�����������Ҳ�ǿɵ����ģ���������ҪΪ������ʵ�� __iter__ ������
   ��_iter_����Ҫ����һ������������������������һ����������
   ���Ե������� __iter__ ������������self���ɡ�

�� ython ��һ��ʵ���� _iter_ ������ _next_ ����������󣬾��ǵ�������

���������б���������ڣ�������������ʱ�򣬲���Ҫ���б�������������Ԫ��һ���Լ���
���ڴ棬������һ���ӳټ��㣨lazy evaluation���ķ�ʽ����Ԫ�أ������������ŵ㡣
���°����Ǽ���Ʋ��������еİ�����
"""


class Fib:
    def __init__(self, fibmax):
        self.a = 0
        self.b = 1
        self.fibmax = fibmax

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a  # ���ص�ֵ�� 0 ��ʼ
        if fib > self.fibmax:  # �������ֵ���׳��쳣
            raise StopIteration

        # ���� self.a, self.b ��ֵ
        # �� __iter__ ����
        self.a, self.b = self.b, self.a + self.b
        return fib  # ���ص�ֵ�� 0 ��ʼ


print(list(Fib(200)))

fx = Fib(200)
for idx in range(13):
    print('쳲��������еĵ� {} �����ǣ�{}'.format(idx+1, next(fx)))
