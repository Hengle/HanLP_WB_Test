# -*- coding: utf-8 -*-
import random
import pprint
import copy


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


def spam1(divide_by):
    return 42 / divide_by


def spam2(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam2(2))
print(spam2(12))
print(spam2(0))
print(spam2(1))


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('深拷贝和浅拷贝，它们都是对于可变数据的操作，用于去除引用，浅拷贝去的浅，深拷贝去的深')


def eggs2(some_parameter):
    some_parameter.append('Hello')
    print(some_parameter)


spam = [1, ['x', 'y', 'z'], 3]
# spam 被作为参数传递给函数 eggs2() 意味着它的值被复制给了 someParameter 但是请注意，
# spam 中存储的是列表的引用，所以，函数直接修改了引用所指的列表。
# eggs2(spam)
cheese = copy.copy(spam)
cheese[0] = 100
print(cheese)
print(spam)
# eggs2(copy.deepcopy(spam))
# print(spam)
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


spam = ['apples', 'bananas', 'tofu', 'cats', 'a', 'b', 'c', 'd']
xxx(spam)

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
    # pprint.pprint(count)
    # print(pprint.pformat(count))


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


def total_brought(guests, item):    # 没有声明数据类型
    # 计算所有客人带来的某种食物的数量
    num_brought = 0
    for k, v in guests.items():
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


calculate_food()
