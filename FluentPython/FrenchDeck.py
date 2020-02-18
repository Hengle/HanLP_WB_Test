#! python3
# coding=gbk

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(9, 11)] + list('JQKA')
    # suits = 'spades diamonds clubs hearts'.split()
    suits = 'xxx'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card_value):
        self._cards[position] = card_value

    def __repr__(self):
        return '-= XXX 没有 __str__ 的时候才调用 =-'

    def __str__(self):
        return '-= 打印的时候优先使用这个函数 =-'


# 花色等级
suit_values = dict(xxx=4, spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value * len(suit_values) + suit_values[my_card.suit]


print('~~构建~~~~~~~~~~~~~~~~~~~~~~~~~~')
deck = FrenchDeck()  # 构建一副牌 __init__
print(FrenchDeck)
print(FrenchDeck())
print(deck)  # __repr__ 注意其 self 参数，是一个实例函数
print('牌的数量 = %d' % len(deck))  # __len__
print('随机抽一张牌：{}'.format(random.choice(deck)))  # __getitem__

print('~~修改~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('打印第 1，2 张牌：{}'.format(deck[:2]))  # __getitem__
deck[1] = Card('Q', 'hearts')  # __setitem__
print('打印第 1，2 张牌：{}'.format(deck[:2]))  # __getitem__

print('~~排序~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('按牌的大小，降序排列，使用多变量循环限制打印数量为 3 张')
for i, card in zip(range(4), sorted(deck, key=spades_high, reverse=False)):
    print(card)

print('~~洗牌~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(0, len(deck) - 1):

    print('i = {}'.format(i))
    for card in deck:
        print(card)

    # 抽牌
    list_temp = deck[:len(deck) - i]  # 当前待抽牌的列表
    random_card = random.choice(list_temp)  # 随机抽一张
    random_card_idx = list_temp.index(random_card)  # 得到索引
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('随机抽到的牌是第 {} 张：{}'.format(random_card_idx, random_card))

    # 将抽到的牌与第 len(deck) - i 张交换，其索引是 len(deck) - i - 1
    deck[random_card_idx] = deck[len(deck) - i - 1]
    deck[len(deck) - i - 1] = random_card
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('洗牌完成，最终的结果是：')
for card in deck:
    print(card)

symbols = '我们?'
print([ord(s) for s in symbols if ord(s) > 0])

a = [5, 7, 6, 3, 4, 1, 2]
print(sorted(a, reverse=True))
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda s: s[2]))
t = 20, 8
divmod(*t)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9} |'.format('', 'lat.', 'long.'))
str_fmt = '{:15} | {:9.4f} | {:9.4f} |'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(str_fmt.format(name, latitude, longitude))

# 具名元组，类
City = collections.namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

LatLong = collections.namedtuple('LatLong', 'lat long')  # 具名元组
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))  # 元组
delhi_data2 = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
delhi_data3 = ['Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889)]
delhi_data4 = ['Delhi NCR', 'IN', 21.935, [28.613889, 77.208889]]
delhi = City._make(delhi_data)
delhi2 = City._make(delhi_data2)
delhi3 = City._make(delhi_data3)
delhi4 = City._make(delhi_data4)
print(type(delhi))
print(type(delhi2))
print(type(delhi3))
print(type(delhi4))
print(delhi)
print(delhi2)
print(delhi3)
print(delhi4)

for key, value in delhi._asdict().items():
    print(key + ':', value)

"""
print(tokyo)
print(City.coordinates)
print(tokyo[0])
print(City._asdict(tokyo))  # 实例方法
print(tokyo._asdict())  # 实例方法
print(City._fields)  # 类方法
# print(tokyo._field_types)
print(type(delhi_data))
print(type(tokyo))
"""

invoice = """
0.....6................................40........52...55........
1909  Pimoroni PiBrella                    $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95    2     $9.90
1510  Panavise Jr. - PV-201                $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[DESCRIPTION], item[UNIT_PRICE])

temp_l = list(range(10))
# 以下语句错误，如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。
# 即便只有单独一个值，也要把它转换成可迭代的序列。
# temp_l[2:5] = 100
print(temp_l)
temp_l[2:5] = [100, 100, 100, 100]
print(temp_l)

board1 = ('-',) * 3  # 构成元组
board2 = ['-', ] * 3  # 构成列表
board3 = [['-'] * 3 for i in range(3)]  # 3 个列表构成的列表
board4 = [['-'] * 3] * 3  # 错误的，这 3 个列表是对同一个列表的引用
print(board1)
print(board2)
print(board3)
print(board4)
board3[1][2] = 'X'
board4[1][2] = 'X'
print(board3)
print(board4)

tl = [1, 2, 3]
print(tl, id(tl))
tl += [2]
print(tl, id(tl))  # tl 仍然指向原来的地址

tl2 = 1, 2, 3
print(tl2, id(tl2))
tl2 += (2,)
print(tl2, id(tl2))  # tl2 指向新的地址
