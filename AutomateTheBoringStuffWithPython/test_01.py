#! python3
# coding=gbk

import pprint
import copy
import re
import os
from pathlib import Path
import shelve

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

file = 'xx.txt'

print(os.path.join(r'C:\Users\bwang\Downloads', file))  # 创建路径

print('——————————切换当前路径——————————')
print(os.getcwd())  # 当前路径，本代码所在路径
print(os.path.join(os.getcwd(), file))
os.chdir(r'C:\Users\bwang\Downloads')  # 切换当前路径到指定路径
print(os.getcwd())  # 查看切换后的当前路径
print(os.path.join(os.getcwd(), file))

print('——————————绝对路径与相对路径——————————')
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.join(os.path.abspath('..'), file))  # 工作目录的父目录
print(os.path.relpath(r'C:\Windows', '.'))

print('——————————当前用户路径——————————')
download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')  # 获取当前用户路径
print(download_dir)  # C:\Users\bwang\Downloads

print('——————————安全创建文件夹——————————')
# os.makedirs(os.path.join(download_dir, 'test1'))
Path(os.path.join(download_dir, 'test1')).mkdir(parents=True, exist_ok=True)  # 安全的创建文件夹

print('——————————分解path——————————')
testpath = os.path.join(download_dir, 'test1', file)
print(os.path.basename(testpath))
print(os.path.dirname(testpath))
print(os.path.split(testpath))
print(testpath.split(os.path.sep))  # 本质上是分解字符串，间隔参数是 os.path.sep == \ (windows系统)
print(os.path.sep)

print('——————————查看文件大小和文件夹内容——————————')
print(os.path.getsize(os.path.join(download_dir, 'mls-mpm88.zip'))/1)  # 指定文件的大小，字节
print(os.listdir(download_dir))  # 文件夹中的内容
print(os.path.getsize(os.path.join(download_dir, 'test1'))/1)  # 指定文件的大小，字节

totalSize = 0
for filename in os.listdir(download_dir):
    totalSize = totalSize + os.path.getsize(os.path.join(download_dir, filename))
print(str(round(totalSize/1024/1024, 1)) + 'M')  # 只算了文件，没算文件夹

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
with open(os.path.join(download_dir, file), 'r+') as f:
    f.write('xX=WB=Xx\n   \n_sss_!')
    print('f = ' + str(f))
    print('type(f) = ' + str(type(f)))
    f.seek(0)  # 之前写完后，游标停在文件末尾，需要挪到开头
    print('读取整个文本，作为一个字符串：\n————————————————————————————\n' + f.read())  # 读整篇，返回的是一个字符串
    f.seek(0)  # 读完后，游标又会停在文件末尾，需要挪到开头
    print('\n读取多行文本，按行存入列表：\n————————————————————————————\n' + str(f.readlines()))  # 读多行，按行存入列表(list)
    f.seek(0)  # 将游标重置到文件开头
    print('\n从从游标位置开始，读一行文本，包含换行符。\n————————————————————————————\n'
          'start -=| ' + f.readline(100) + ' |=- end')  # 最多读一行

# open(os.path.join(download_dir, 'xxx'), 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\bwang\\Downloads\\xxx'

print('——————————用 shelve 模块保存变量——————————')
shelfFile = shelve.open('wb_data')  # 传入文件名，返回的是一个 shelfFile 它类似一个字典，可以在其中保存键值对
shelfFile['cats'] = ['Z', 'P', 'S']
shelfFile.close()

sf = shelve.open('wb_data')  # 重新打开文件
print(sf['cats'])  # 验证数据是否正确保存
shelfFile.close()  # 关闭文件
