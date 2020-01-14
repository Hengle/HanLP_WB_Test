
import random
import pprint
import copy
import re


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('控制流')


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
print('字典 setdefault()')


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
    for k, v in guests.items():     # 手法清奇的多重赋值
        num_brought = num_brought + v.get(item, 0)
    return num_brought


def calculate_food():
    food = {}
    # 统计食物的种类
    for guest_items in all_guests.items():
        for food_name in guest_items[1].keys():
            food.setdefault(food_name, 0)
    print(food)     # 展示所有食物种类
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
        inv.setdefault(item, 0)     # item 存在时，返回其值，否则添加这个键，设其值为0
        inv[item] += 1


add_to_inventory(inventory, dragon_loot)
display_inventory(inventory, 10, 10)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('字符串处理')

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
print('正则表达式 regex')


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
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
# use_is_phone_number()


"""
正则表达式的基本用法：

1、用括号分组：(\d\d\d)-(\d\d\d-\d\d\d\d)
    通过括号可以将匹配到的文本分组，第一对括号是第1组，第二对括号是第2组。向group()传入整数1或者2，就可获取匹配文本的不同部分

2、用管道匹配多个分组
    字符|称为“管道”，它有“或者”的含义。正则表达式 r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
    如果 Batman 和 Tina Fey 都出现在被查找的字符串中，第一次出现的匹配文本，将作为 Match 对象返回。
    
3、用问号表示其前面的分组是可选的，注意，分组的表示方法是使用括号
    你可以认为 ? 是在说，“匹配这个问号之前的分组零次或一次”。

4、用星号‘*’表示匹配其之前的分组零次或多次，注意，分组的表示方法是使用括号

5、用加号‘+’表示匹配其之前的分组一次或多次，注意，至少一次

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
mo1 = hero_regex.search('Batman and Tina Fey, Batman.')     # 返回找到的第 1 个
print(mo1)
print(mo1.group())
print(mo1.group(0))
# print(mo1.group(1))     # 出错
mo2 = hero_regex.findall('Batman and Tina Fey, Batman.')
print(mo2)
print('~~~~~~~~~~~~~~~~~~')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')        # 返回找到的第 1 个，注意括号的使用
mo3 = batRegex.search('xBatmobilex lost a wheel xBatbatx')
print(mo3)
print(mo3.group())
print(mo3.group(0))     # 完全匹配的文本
print(mo3.group(1))     # 括号内匹配的文本

# 3、用问号 ？ 表示 “可选" 的匹配
print('————————————————\n2、使用问号：\n————————————————')
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
print('————————————————\n2、使用星号：\n————————————————')
batRegex = re.compile(r'Bat(wo)*man')
mo8 = batRegex.search('The Adventures of Batman')
mo9 = batRegex.search('The Adventures of Batwoman')
mo10 = batRegex.search('The Adventures of Batwowowowoman')
print(mo8.group())
print(mo9.group())
print(mo10.group())

# 5、用星号 + 表示 匹配其前面的分组 一次 或 多次，至少一次
print('————————————————\n2、使用加号：\n————————————————')
batRegex = re.compile(r'Bat(wo)+man')
mo11 = batRegex.search('The Adventures of Batman')
mo12 = batRegex.search('The Adventures of Batwoman')
mo13 = batRegex.search('The Adventures of Batwowowowoman')
print(mo11)     # 返回 None，print(mo11.group()) 会出错
print(mo12.group())
print(mo13.group())
