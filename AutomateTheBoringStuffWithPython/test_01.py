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
print('控制流')
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
print('全局变量与变量的作用域')
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
print('try ... except ... 语法学习')
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
print('深拷贝和浅拷贝，它们都是对于可变数据的操作，用于去除引用，浅拷贝去的浅，深拷贝去的深')


def eggs2(some_parameter):
    some_parameter.append('Hello')
    print(some_parameter)


string3 = [1, ['x', 'y', 'z'], 3]
# string3 被作为参数传递给函数 eggs2() 意味着它的值被复制给了 someParameter 但是请注意，
# string3 中存储的是列表的引用，所以，函数直接修改了引用所指的列表。
# eggs2(string3)
cheese = copy.copy(string3)
cheese[0] = 100
print(cheese)
print(string3)
# eggs2(copy.deepcopy(string3))
# print(string3)
print('-------------------')
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值，传对象的引用
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('代码实践 4.10.1 逗号代码')


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
print('代码实践 4.10.2 字符图网格')
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
print('With ... As ... 语法研究')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

"""
with as 语法的说明：

    with open(r'c:\test.txt', 'r') as f:
        data = f.read()

with 后面接的对象返回的结果赋值给 f，当 open 函数返回的文件对象赋值给了 f，with 会自已获取上下文件的异常信息。
with 是如何做到的呢？
with 后面返回的对象要求必须两__enter__()/__exit__()这两个方法，而文件对象f刚好是有这两个方法的，故应用自如。

python中官方定义说明如下(https://docs.python.org/2/reference/datamodel.html#context-managers)：

    object.__enter__(self)
    进入与此对象相关的运行时上下文。with语句将将此方法的返回值绑定到语句的AS子句中指定的目标（如果有设置的话）
 
    object.__exit__(self, exc_type, exc_value, traceback)
    退出与此对象相关的运行时上下文。参数描述导致上下文退出的异常。如果上下文运行时没有异常发生，那么三个参数都将置为None。
    如果有异常发生，并且该方法希望抑制异常（即阻止它被传播），则它应该返回True。否则，异常将在退出该方法时正常处理。
 
    请注意, __exit__()方法不应该重新抛出传入的异常，这是调用者的职责。
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
        # 如果有异常发生，并且该方法希望抑制异常抛出（即阻止它被传播），则它应该返回True。
        # 否则，异常将在退出该方法时正常处理。
        return True


with Test() as sample:
    sample.do_something()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第五章 字典和结构化数据')
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
print('字典，对真实世界建模：井字棋盘')
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
            print('初始棋局状态')
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
    print('最终棋局状态')
    print_board(theBoard)
    print('----------------------------------')


# turn_board()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('嵌套的字典和列表')


def use_get():
    # 在访问一个键的值之前，检查该键是否存在于字典中，这很麻烦。好在，字典有一个 get()方法，
    # 它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
    picnic_items = {'apples': 5, 'cups': 2}
    print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
    print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')


# 字典，包含客人带来的东西
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    # 计算所有客人带来的某种食物的数量
    num_brought = 0
    for k, v in guests.items():  # 手法清奇的多重赋值
        num_brought = num_brought + v.get(item, 0)
    return num_brought


def calculate_food():
    food = {}
    # 统计食物的种类
    for guest_items in all_guests.items():
        for food_name in guest_items[1].keys():
            food.setdefault(food_name, 0)
    print(food)  # 展示所有食物种类
    for food_name in food.keys():
        print(' ' + food_name + ' = ', end='')
        print(total_brought(all_guests, food_name), end='')
        print(', ', end='')
    print()


calculate_food()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('好玩游戏的物品清单')

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
        inv.setdefault(item, 0)  # item 存在时，返回其值，否则添加这个键，设其值为0
        inv[item] += 1


add_to_inventory(inventory, dragon_loot)
display_inventory(inventory, 10, 10)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第六章 字符串操作')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

string1 = r'asd\'\
ss\
egg'

print(string1)


def multi_line_comment():
    """
    此多行注释用于说明
    multi_line_comment()函数用途。
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
print('表格打印')
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def grid(data):
    print('————————————————————————')
    length_max = [0] * len(table_data)
    for i in range(table_data.__len__()):
        for j in range(table_data[0].__len__()):
            if table_data[i][j].__len__() > length_max[i]:
                length_max[i] = table_data[i][j].__len__()
        print(length_max[i])

    print('————————————————————————')
    for j in range(table_data[0].__len__()):
        for i in range(table_data.__len__()):
            if i == 0:
                print(data[i][j].rjust(length_max[i], ' '), end=' ')
            else:
                print(data[i][j].ljust(length_max[i], ' '), end=' ')
        print('')
    print('————————————————————————')


grid(table_data)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第七章 模式匹配与正则表达式')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def is_phone_number(text):  # 不用正则表达式，非常繁琐
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
比较完整的参考文档：https://www.jianshu.com/p/bb7d5386507c，https://deerchao.cn/tutorials/regex/regex.htm
正则表达式的基本用法：

1、用括号分组：r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
    通过括号可以将匹配到的文本分组，第一对括号是第1组，第二对括号是第2组。向group()传入整数1或者2，就可获取匹配文本的不同部分

2、用管道匹配多个分组
    字符|称为“管道”，它有“或者”的含义。正则表达式 r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
    如果 Batman 和 Tina Fey 都出现在被查找的字符串中，第一次出现的匹配文本，将作为 Match 对象返回。
    
3、用问号表示其前面的分组是可选的，注意，分组的表示方法是使用括号
    你可以认为 ? 是在说，“匹配这个问号之前的分组零次或一次”。

4、用星号 * 表示匹配其之前的分组零次或多次，注意，分组的表示方法是使用括号

5、用加号 + 表示匹配其之前的分组一次或多次，注意，至少一次

6、用花括号 {} 匹配其前面的分组 特定次数，(Ha){3} == 'HaHaHa'
    除了一个数字，还可以指定一个范围，即在花括号中写下一个最小值、一个逗号和一个最大值。
    (Ha){3,5} 将匹配 'HaHaHa'、'HaHaHaHa'和'HaHaHaHaHa'。
    (Ha){3,}  将匹配 3 次或更多次实例，
    (Ha){,5}  将匹配 0 到 5 次实例。
    这里有一个问题，'HaHaHa'和'HaHaHaHa'也能够有效地匹配正则表达式(Ha){3,5}，但实际上返回的是'HaHaHaHaHa'。
    Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。
    花括号的“非贪心”版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号：re.compile(r'(Ha){3,5}?')。
    请注意，问号在正则表达式中可能有两种含义：声明非贪心匹配或表示可选的分组。这两种含义是完全无关的。
    
7、作为 findall() 方法的返回结果的总结，请记住下面两点：
    1．如果调用在一个 没有 分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，
    方法findall()将返回一个匹配字符串的列表， 例如['415-555-9999', '212-555-0000']。
    2．如果调用在一个 有 分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，
    方法findall()将返回一个字符串的元组的列表(每个分组对应一个字符串)，例如[('415', '555', '1122'), ('212', '555', '0000')]。
    
8、字符分类的缩写代码 https://blog.csdn.net/weixin_40693324/article/details/78785608

9、定位符 ^ 和 $
    可以在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。
    类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束。
    可以同时使用^和$，表明整个字符串必须匹配该模式，也就是说，只匹配该字符串的某个子集是不够的。

10、通配符 .
    表示换行符 \n 以外所有的字符

11、使用 sub() 方法可以替换字符串

12、使用 re.VERBOSE 参数 让 re.compile() 忽略正则表达式中的空白和注释。
    这意味着，此时可以通过换行并添加注释，来帮助理解复杂的正则表达式。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    字符类型    示例
    ————————————————————————————————————————————————————————————
    转义符      \
    一般字符    \d, \D, \w, \W, \xn, \num, \n, \nm, \nml, \un, .
    字符集合    x|y, [xyz], [^xyz], [a-z], [^a-z]
    非打印字符  \cx, \f, \n, \r, \s, \S, \t, \v
    定位符      ^, $, \b, \B
    限定符      *, +, ?, ?(懒惰), {n}, {n,}, {n,m}
    匹配        (pattern), (?:pattern)
    零宽断言    (?=pattern), (?!pattern), (?<=pattern), (?<!pattern)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见分类     含义
    ————————————————————————————————————————————————————————————————————————————————————————————————————————
    \d          == [0-9] 0 到 9 的任何数字
    \D          == [^0-9] 除 0 到 9 的数字以外的任何字符
    \w          == [A-Za-z0-9_] 任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
    \W          == [^A-Za-z0-9_] 除字母、数字和下划线以外的任何字符
    \s          == [ \f\n\r\t\v] 空格、制表符或换行符（可以认为是匹配“空白”字符）
    \S          == [^ \f\n\r\t\v] 除空格、制表符和换行符以外的任何字符
    
    ^           行首匹配
    ?           0 或 1 个 
    *           0 或 多个 
    +           1 或 多个
    \           将下一个字符标记为一个特殊字符、或一个原义字符、或一个向后引用、或一个八进制转义符
    $           匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位
    .           除 "\n" 之外的任何单个字符，要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式

    ()          是为了提取匹配的字符串。表达式中有几个()就有几个相应的匹配字符串，(\s*)表示连续空格的字符串
    []          是定义匹配的字符范围。比如 [a-zA-Z0-9] 表示相应位置的字符要匹配英文字符和数字。[\s*]表示空格或者*号
    [^x]        x 以外的任意字符
    [^aeiou]	除了aeiou这几个字母以外的任意字符
    {}          一般用来表示匹配的长度，比如 \s{3} 表示匹配三个空格，\s{1,3}表示匹配一到三个空格
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# 1、用括号分组
print('————————————————\n1、使用括号：\n————————————————')
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
area_code, main_number = mo.groups()
print(area_code, main_number)

# 2、管道符号 | 表示“或者”，返回第一个匹配到的文本
print('————————————————\n2、使用管道：\n————————————————')
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey, Batman.')  # 返回找到的第 1 个
print(mo1)
print(mo1.group())
print(mo1.group(0))
# print(mo1.group(1))     # 出错
mo2 = hero_regex.findall('Batman and Tina Fey, Batman.')
print(mo2)
print('~~~~~~~~~~~~~~~~~~')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')  # 返回找到的第 1 个，注意括号的使用
mo3 = batRegex.search('xBatmobilex lost a wheel xBatbatx')
print(mo3)
print(mo3.group())
print(mo3.group(0))  # 完全匹配的文本
print(mo3.group(1))  # 括号内匹配的文本

# 3、用问号 ？ 表示 “可选" 的匹配
print('————————————————\n3、使用问号：\n————————————————')
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

# 4、用星号 * 表示 匹配其前面的分组 零次 或 多次
print('————————————————\n4、使用星号：\n————————————————')
batRegex = re.compile(r'Bat(wo)*man')
mo8 = batRegex.search('The Adventures of Batman')
mo9 = batRegex.search('The Adventures of Batwoman')
mo10 = batRegex.search('The Adventures of Batwowowowoman')
print(mo8.group())
print(mo9.group())
print(mo10.group())

# 5、用星号 + 表示 匹配其前面的分组 一次 或 多次，至少一次
print('————————————————\n5、使用加号：\n————————————————')
batRegex = re.compile(r'Bat(wo)+man')
mo11 = batRegex.search('The Adventures of Batman')
mo12 = batRegex.search('The Adventures of Batwoman')
mo13 = batRegex.search('The Adventures of Batwowowowoman')
print(mo11)  # 返回 None，print(mo11.group()) 会出错
print(mo12.group())
print(mo13.group())

# 6、用花括号 {} 匹配其前面的分组 特定次数
print('————————————————\n6、使用花括号：\n————————————————')
haRegex = re.compile(r'(Ha){3}')
mo14 = haRegex.search('HaHaHa')
mo15 = haRegex.search('Ha')
print(mo14.group())
print(mo15)
print('———————— 贪心，非贪心 ————————')
greedy_Ha_regex = re.compile(r'(Ha){3,5}')  # 贪心形式，默认
mo16 = greedy_Ha_regex.search('HaHaHaHaHa')
non_greedy_Ha_regex = re.compile(r'(Ha){3,5}?')  # 非贪心形式，加 ?
mo17 = non_greedy_Ha_regex.search('HaHaHaHaHa')
print(mo16.group())
print(mo17.group())

print('————————————————————————————————————————————————————————————————————————————————————')
print('.findall() 方法')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# ['415-555-9999', '212-555-0000']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# [('415', '555', '9999'), ('212', '555', '0000')]

print('————————————————————————————————————————————————————————————————————————————————————')
print('字符分类')
xmasRegex = re.compile(r'\d+\s\w+')
pprint.pprint(xmasRegex.findall('01 drummers, 02 pipers, 03 lords, 04 ladies, 05 maids, 06 swans, '
                                '07 geese, 08 rings, 09 birds, 10 hens, 11 doves, 12 partridge'))

print('————————————————————————————————————————————————————————————————————————————————————')
print('自定义字符分类')
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

print('————————————————————————————————————————————————————————————————————————————————————')
print(r'定位符 ^, $')
beginsWithHello = re.compile(r'^Hello')  # 表示以 Hello 开头的文本
print(beginsWithHello.search('Hello world!'))  # <re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.'))  # None

endsWithNumber = re.compile(r'\d$')  # 表示以数字结束
endsWith2Numbers = re.compile(r'\d{2}$')  # 表示以2个数字结束
endsWith3Numbers = re.compile(r'\d{3}$')  # 表示以3个数字结束
print(endsWithNumber.search('test23'))  # <re.Match object; span=(5, 6), match='3'>
print(endsWith2Numbers.search('test23'))  # <re.Match object; span=(4, 6), match='23'>
print(endsWith3Numbers.search('test23'))  # None

wholeStringIsNum = re.compile(r'^\d+$')  # 从头到尾都是有数字组成，至少要有1个数字
wholeStringIsNum2 = re.compile(r'^\d*$')  # 从头到尾都是有数字组成，可以是0个数字
print(wholeStringIsNum.search('1234567890'))  # <re.Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890'))  # None
print(wholeStringIsNum.search('12 34567890'))  # None
print(wholeStringIsNum.search(''))  # None
print(wholeStringIsNum2.search(''))  # <re.Match object; span=(0, 0), match=''>

print('————————————————————————————————————————————————————————————————————————————————————')
print(r'通配符 .')
atRegex = re.compile(r'.at')  # 匹配 任意字符 + 'at'
print(atRegex.findall('The cat in the hat sat on the flat mat.'))  # ['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: .* Last Name: .*')  # 显然，.* 指任意字符
mo18 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo18.group())  # 获取到整个字符串
print('————————使用分组————————')
nameRegexGroup = re.compile(r'First Name: (.*) Last Name: (.*)')  # 通过括号，还可以得到分组字符
mo19 = nameRegexGroup.search('First Name: Al Last Name: Sweigart')
print(mo19.group())
print(mo19.group(0))  # == mo19.group()
print(mo19.group(1))
print(mo19.group(2))
print(mo19.groups())
print('————————贪心/懒惰————————')
greedyRegex = re.compile(r'<.*>')  # 贪心模式
print('贪心模式：' + greedyRegex.search('<To serve man> for dinner.>').group())  # <To serve man> for dinner.>
nongreedyRegex = re.compile(r'<.*?>')  # 懒惰模式
print('懒惰模式：' + nongreedyRegex.search('<To serve man> for dinner.>').group())  # <To serve man>
print('————————不匹配换行————————')
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print('————————匹配换行————————')
newlineRegex = re.compile('.*', re.DOTALL)  # 第2个参数 re.DOTALL 其实就是 DotAll 表示 . 匹配所有字符，包括换行
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print('————————忽略大小写————————')
robocop = re.compile(r'robocop', re.I)  # 第二个参数 re.I 或者 re.IGNORECASE 表示忽略大小写
print(robocop.search('RoboCop is part man, part machine, all cop.').group())  # 'RoboCop'

print('————————————————————————————————————————————————————————————————————————————————————')
print('用 sub() 方法替换字符串')
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent \w(\w)\w*')  # 'Agent (一个分组字符)若干字符'
print(agentNamesRegex.sub(r'*\1***',
                          'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

print('————————————————————————————————————————————————————————————————————————————————————')
print('使用 re.VERBOSE')
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')  # 看得懂么？

phoneRegex2 = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # 区号，3个数字，或者括号里的3个数字，或者不存在
    (\s|-|\.)?                      # 空格，或者-，或者.，或者不存在
    (\d{3})                         # 前3个数字
    (\s|-|\.)                       # 空格，或者-，或者.
    (\d{4})                         # 后4个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # (有或无若干空格 + 括号内的ext或者x或者ext. + 有或无若干空格 + 2~5个数字)?
)''', re.VERBOSE)

for phoneNum in phoneRegex2.findall('as 425-589-4885, (110)258.6255, 358-4568 x 25531, '
                                    '234 0988, 110-258-1254 ext. 2586'):
    print(phoneNum[0])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第八章 读写文件')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(os.path.join('usr', 'bin', 'spam'))

print('——————————工作路径——————————')
code_home = os.getcwd()  # 保存初始工作路径，即代码所在的路径
print(code_home)

print('——————————切换工作路径——————————')
download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')  # 获取当前用户路径
print('切换的目标路径：' + download_dir)  # C:\Users\bwang\Downloads
os.chdir(download_dir)  # 将工作路径切换到下载文件夹

print('——————————绝对路径与相对路径——————————')
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.relpath(r'C:\Windows', '.'))

print('——————————切回默认工作路径——————————')
os.chdir(code_home)  # 切回默认工作路径
print(os.getcwd() + '\n')  # 确认

print('——————————安全创建文件夹——————————')
# os.makedirs(os.path.join(download_dir, 'test1'))
Path(os.path.join(download_dir, 'test')).mkdir(parents=True, exist_ok=True)  # 安全的创建文件夹

print('——————————分解path——————————')
testpath = os.path.join(download_dir, 'test.txt')
print(os.path.basename(testpath))
print(os.path.dirname(testpath))
print(os.path.split(testpath))
print(testpath.split(os.path.sep))  # 本质上是分解字符串，间隔参数是 os.path.sep == \ (windows系统)
print(os.path.sep)

print('——————————查看文件大小和文件夹内容——————————')
print(os.path.getsize(os.path.join(download_dir, 'PBSetup70.exe')) / 1)  # 指定文件的大小，字节
print(os.listdir(download_dir))  # 文件夹中的内容
print(os.path.getsize(os.path.join(download_dir, 'test')) / 1)  # 指定文件的大小，字节

totalSize = 0
for filename in os.listdir(download_dir):
    totalSize = totalSize + os.path.getsize(os.path.join(download_dir, filename))
print(str(round(totalSize / 1024 / 1024, 1)) + 'M')  # 只算了文件，没算文件夹

print('——————————检查路径有效性——————————')
# print(os.path.exists(r'C:\Windows'))
# print(os.path.exists(r'C:\sometest'))

print('——————————创建文件，写入文本，读取文本——————————')
'''
open() 的第二个参数可以使用：
'r'  只读模式，默认值
'w'  覆写模式，只能写，不能读，从头开始写，无视之前已经存在的内容
'a'  添加模式，在已有文件末尾追加内容
'r+' 读写模式，可读可写
如果文件不存在，以只读方式打开，会报错，以覆写/追加的模式打开，会按此名字创建一个空文件。
需要调用close()方法关闭文件后，才能再次打开该文件。
'''
file = 'wb.txt'
with open(os.path.join('./data', file), 'w') as f:  # 只能写，不能读，'r+' 不能新建文件
    f.write('xX=WB=Xx\n   \n_sss_!')
    print('f = ' + str(f))
    print('type(f) = ' + str(type(f)))

# with open(os.path.join(download_dir, file), 'r+') as f:
with open(os.path.join('./data', file), 'r+') as f:
    f.seek(0)  # 之前写完后，游标停在文件末尾，需要挪到开头
    print('读取整个文本，作为一个字符串：\n————————————————————————————\n' + f.read())  # 读整篇，返回的是一个字符串
    f.seek(0)  # 读完后，游标又会停在文件末尾，需要挪到开头
    print('\n读取多行文本，按行存入列表：\n————————————————————————————\n' + str(f.readlines()))  # 读多行，按行存入列表
    f.seek(0)  # 将游标重置到文件开头
    print('\n从从游标位置开始，读一行文本，包含换行符。\n————————————————————————————\n'
          'start -=| ' + f.readline(100) + ' |=- end')  # 最多读一行

# open(os.path.join(download_dir, 'xxx'), 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\bwang\\Downloads\\xxx'

print('——————————用 shelve 模块保存变量——————————')
shelfFile = shelve.open('data/wb_data')  # 传入文件名，返回的是一个 shelfFile 它类似一个字典，可以在其中保存键值对
shelfFile['cats'] = ['Z', 'P', 'S']
shelfFile.close()

sf = shelve.open('data/wb_data')  # 重新打开文件
print(list(sf.keys()))
print(list(sf.values()))
print(sf['cats'])  # 验证数据是否正确保存
shelfFile.close()  # 关闭文件

# 已有数据
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('myCats.py', 'w')  # 创建一个文件
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
# 此时，文本中的内容是："cats = [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
# pprint.pformat() 产生的文本的格式不仅易于阅读，同时也是语法上正确的 python 代码，可以直接导入使用。

# import myCats  # 可以执行通过

# print(myCats.cats)
# print(myCats.cats[0])
# print(myCats.cats[0]['name'])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第九章 组织文件')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('第十四章 JSON')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
print(json.loads(stringOfJsonData))

# 单行打印乘法口诀表
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
# Python 编程从入门到实践 2016.pdf
# ==========================================
# 面向对象编程
# 类
class Person:
    pass  # 空代码块


p = Person()  # 实例化一个类
print(p)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 控制台返回
# <__main__.Person object at 0x000002AAADF3F9C8>
# 这意味着，Person 类的 __main__ 模块中拥有了一个实例，并显示了这个实例的内存地址

class Person2:
    def __init__(self, name):  # 用于初始化，__init__ 方法会在类的对象被实例化（Instantiated）时立即运行
        self.name = name  # 实例变量/对象变量

    radius = 42  # 类变量

    def say_hi(self):  # 默认，实例方法，会使用实例的属性
        print('~~~~~~~~~ Hi! %s!' % self.name)

    @staticmethod  # 静态方法，这种方法不会使用这个类相关的任何东西，没有 self 或者 cls 参数
    def my_add(xa, ya):
        return xa + ya

    @classmethod  # 类方法，这种方法不是绑定到类的实例上的，而是绑定到类上的，所以不能从类的实例上调用
    def get_radius(cls):
        return cls.radius


wb = Person2('WangBo')
wb.say_hi()
wzy = Person2('WangZhiYuan')
wzy.say_hi()

print(Person2)  # 类 <class '__main__.Person2'>
print(Person2.my_add(3, 6))  # 通过类来调用静态方法

print(Person2('xxx'))  # 类的实例 <__main__.Person2 object at 0x000001EB0B9E7948>
print(Person2('xxx').my_add(3, 6))  # 通过类的实例来调用静态方法，也是可以的，但是没有必要，因为会浪费资源

print(Person2.get_radius())  # 类的属性 42
xxx = Person2('xxx')  # 创建一个类的实例，注意，不是 xxx = Person2
xxx.radius = 100  # 修改实例的属性为 100
print(xxx.radius)  # 获取实例的属性
print(xxx.get_radius())  # 类方法获取到的仍然是类的属性，而不是实例的属性

Person2.radius = 1  # 修改类变量
print(xxx.radius)  # 实例的变量不会跟着变
yyy = Person2('yyy')  # 实例化一个对象
print(yyy.radius)  # 从类变量种复制过来的实例变量

# 所以，任何情况下，get_radius() 都是绑定到 类 上的。
# 那么，这个类方法，到底有什么用呢？我们在什么时候才会去用它呢? 我想这才是我们想去关心的。
"""
(1)、工厂方法：它用于创建类的实例，例如一些预处理。
如果使用@staticmethod代替，那我们不得不硬编码 Pizza 类名在函数中，这使得任何继承 Pizza 的类都不能使用我们这个工厂方法给它自己用。

class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients
 
    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())

(2)、调用静态类：如果你把一个静态方法拆分成多个静态方法，除非你使用类方法，否则你还是得硬编码类名。
使用这种方式声明方法，Pizza 类名明永远都不会在被直接引用，继承和方法覆盖都可以完美的工作。

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
    """表示有一个带有名字的机器人。"""
    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name  # 对象变量，属于 self 拥有
        print("正在初始化 {} ...".format(self.name))

        # 机器人数量 +1
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} 正在被销毁".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} 是最后一个了。".format(self.name))
        else:
            print("还有 {:d} 个机器人在工作。".format(Robot.population))

    def say_hi(self):
        """来自机器人的问候"""
        print("您好，我的主人，请叫我 {}".format(self.name))

    @classmethod
    def how_many(cls):
        """打印当前机器人的数量"""
        print("我们现在有 {} 个机器人在工作".format(cls.population))

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

print('\n机器人工作中...\n')

print('工作已经完成，可以销毁机器人')

droid1.die()
droid2.die()
Robot.how_many()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
Robot.h_m()
Robot.print_class_doc()
Robot.print_say_hi_doc()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class SchoolMember:
    """代表学校里的任何成员。"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """告诉我细节。"""
        print('Name:{} Age:{}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """代表一位老师。"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{:d}'.format(self.salary))


class Student(SchoolMember):
    """代表一位学生。"""

    def __init__(self, name, age, marks):
        # SchoolMember.__init__(self, name, age)
        super().__init__(name, age)  # 跟上面一行的作用相同
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{:d}'.format(self.marks))


m = SchoolMember('Nobody', 0)
t = Teacher('WangBo', 42, 30000)
s = Student('WangZhiYuan', 7, 75)

# 打印一行空白
print()

members = [m, t, s]
for member in members:
    member.tell()

t = 'a', 'b'
print(type(t))

print(dict(zip('abc', range(3))))
print(dict(zip(range(3), 'abc')))


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet(pet_name='harry2', animal_type='hamster')
describe_pet('harry', 'hamster')
describe_pet('xxx')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('《 Python Cookbook 》第三版中文v3.0.0 2017')
# ==========================================
# Python Cookbook 第三版中文v3.0.0 2017.pdf
# ==========================================
# 第四章：迭代器与生成器
print(' 第四章：迭代器与生成器')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def manual_iter():
    with open(r'c:\LibAntiPrtSc_INFORMATION.log') as fi:
        try:
            while True:
                line = next(fi)  # 函数 next(iterator[, default]) 返回迭代器的下一项
                print(line, end='')
        except StopIteration:  # StopIteration表示迭代结束
            pass

        print('~~~~~ 另一种写法~~~~~')
        fi.seek(0)  # 回到文件开头
        while True:
            line = next(fi, None)  # 函数 next(iterator[, default]) 返回迭代器的下一项
            if line:
                print(line, end='')
            else:
                print('-=WB=-')
                break


manual_iter()


# 代理迭代
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):  # 将 print() 操作代理到这里
        return 'Node value = {!r}'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):  # 将 for in 操作代理到列表 self._children 上
        return iter(self._children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)


# 生成器产生迭代
def my_range(start, stop, increment):
    my_x = start
    while my_x < stop:
        yield my_x  # 生成器
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
迭代器协议
========
1、对象需要提供 __next__ 方法，它要么返回下一项，要么引起一个 StopIteration 异常
2、python要求迭代器本身也是可迭代的，所以我们要为迭代器实现 __iter__ 方法，
   而_iter_方法要返回一个迭代器，迭代器自身正是一个迭代器，
   所以迭代器的 __iter__ 方法返回自身self即可。

在 ython 中一个实现了 _iter_ 方法和 _next_ 方法的类对象，就是迭代器。

迭代器与列表的区别在于，构建迭代器的时候，不需要像列表那样，把所有元素一次性加载
到内存，而是以一种延迟计算（lazy evaluation）的方式返回元素，这正是它的优点。
如下案例是计算菲波那切数列的案例。
"""


class Fib:
    def __init__(self, fibmax):
        self.a = 0
        self.b = 1
        self.fibmax = fibmax

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a  # 返回的值从 0 开始
        if fib > self.fibmax:  # 超过最大值，抛出异常
            raise StopIteration

        # 更新 self.a, self.b 的值
        # 备 __iter__ 调用
        self.a, self.b = self.b, self.a + self.b
        return fib  # 返回的值从 0 开始


print(list(Fib(200)))

fx = Fib(200)
for idx in range(13):
    print('斐波那契数列的第 {} 个数是：{}'.format(idx+1, next(fx)))
