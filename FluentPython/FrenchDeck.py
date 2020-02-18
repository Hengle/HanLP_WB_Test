#! python3
# coding=gbk

import collections
import random
import bisect
import array
import numpy

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
        return '-= XXX û�� __str__ ��ʱ��ŵ��� =-'

    def __str__(self):
        return '-= ��ӡ��ʱ������ʹ��������� =-'


# ��ɫ�ȼ�
suit_values = dict(xxx=4, spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value * len(suit_values) + suit_values[my_card.suit]


print('~~����~~~~~~~~~~~~~~~~~~~~~~~~~~')
deck = FrenchDeck()  # ����һ���� __init__
print(FrenchDeck)
print(FrenchDeck())
print(deck)  # __repr__ ע���� self ��������һ��ʵ������
print('�Ƶ����� = %d' % len(deck))  # __len__
print('�����һ���ƣ�{}'.format(random.choice(deck)))  # __getitem__

print('~~�޸�~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__
deck[1] = Card('Q', 'hearts')  # __setitem__
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__

print('~~����~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('���ƵĴ�С���������У�ʹ�ö����ѭ�����ƴ�ӡ����Ϊ 3 ��')
for i, card in zip(range(4), sorted(deck, key=spades_high, reverse=False)):
    print(card)

print('~~ϴ��~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(0, len(deck) - 1):

    print('i = {}'.format(i))
    for card in deck:
        print(card)

    # ����
    list_temp = deck[:len(deck) - i]  # ��ǰ�����Ƶ��б�
    random_card = random.choice(list_temp)  # �����һ��
    random_card_idx = list_temp.index(random_card)  # �õ�����
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('����鵽�����ǵ� {} �ţ�{}'.format(random_card_idx, random_card))

    # ���鵽������� len(deck) - i �Ž������������� len(deck) - i - 1
    deck[random_card_idx] = deck[len(deck) - i - 1]
    deck[len(deck) - i - 1] = random_card
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('ϴ����ɣ����յĽ���ǣ�')
for card in deck:
    print(card)

symbols = '����?'
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

# ����Ԫ�飬��
City = collections.namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

LatLong = collections.namedtuple('LatLong', 'lat long')  # ����Ԫ��
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))  # Ԫ��
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
print(City._asdict(tokyo))  # ʵ������
print(tokyo._asdict())  # ʵ������
print(City._fields)  # �෽��
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
# ���������������ֵ�Ķ�����һ����Ƭ����ô��ֵ�����Ҳ�����Ǹ��ɵ�������
# ����ֻ�е���һ��ֵ��ҲҪ����ת���ɿɵ��������С�
# temp_l[2:5] = 100
print(temp_l)
temp_l[2:5] = [100, 100, 100, 100]
print(temp_l)

board1 = ('-',) * 3  # ����Ԫ��
board2 = ['-', ] * 3  # �����б�
board3 = [['-'] * 3 for i in range(3)]  # 3 ���б��ɵ��б�
board4 = [['-'] * 3] * 3  # ����ģ��� 3 ���б��Ƕ�ͬһ���б������
print(board1)
print(board2)
print(board3)
print(board4)
board3[1][2] = 'X'
board4[1][2] = 'X'
print(board3)
print(board4)

tl1 = [1, 2, 3]
print(tl1, id(tl1))
tl1 += [2]
print(tl1, id(tl1))  # tl ��Ȼָ��ԭ���ĵ�ַ

tl2 = 1, 2, 3
print(tl2, id(tl2))
tl2 += (2,)
print(tl2, id(tl2), 'sss', tl2)  # tl2 ָ���µĵ�ַ

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ----------0--------1---------2--0
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle, lo=4, hi=8)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


fn = bisect.bisect
# fn = bisect.bisect_left
print('DEMO:', fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(fn)

breakpoints = [60, 70, 80, 90]


def grade(score, bps=breakpoints, grades='EDCBA'):
    idx = bisect.bisect(bps, score)
    return grades[idx]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

for score in [33, 99, 77, 70, 89, 90, 100]:
    bisect.insort(breakpoints, score)
    print('%3d ->' % score, breakpoints)

# һ���ܴ�ĸ�������
# floats = array.array('d', [random.random() for i in range(10**8)])  # ����4G�ڴ�
floats = array.array('d', (random.random() for i in range(10 ** 6)))  # ����1G�ڴ�
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
print(len(floats))
print(floats[-1])
print('------------------')
floats2 = array.array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 6)
fp.close()
print(floats2[-1])
print(floats2.typecode)

# �ڴ���ͼ
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print('len =', len(memv), '\n', 'memv[0] =', memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[4] = 78  # ���ֽ� 1*78 + 256*0 = 78
memv_oct[7] = 1  # ���ֽ� 1*1 + 256*1 = 257
print(numbers)

# NmuPy ��ά����
