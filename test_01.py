# -*- coding: utf-8 -*-
import random
import copy


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


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for x in range(9):
#   print(getAnswer(random.randint(1, 9)))


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


def spam1(divideBy):
    return 42 / divideBy


def spam2(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam2(2))
print(spam2(12))
print(spam2(0))
print(spam2(1))


def eggs2(someParameter):
    someParameter.append('Hello')
    print(someParameter)


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
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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


def xxx(input1):
    s = ''
    for i in range(len(input1)):
        if i == len(input1) - 1:
            s += 'and ' + input1[i]
        else:
            s += input1[i] + ", "
    print(s)


spam = ['apples', 'bananas', 'tofu', 'cats', 'a', 'b', 'c']
xxx(spam)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
