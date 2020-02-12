#! python3
# coding=gbk

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # suits = 'spades diamonds clubs hearts'.split()
    suits = 'xxx'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card_value):
        self._cards[position] = card_value


# 花色等级
suit_values = dict(xxx=4, spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value * len(suit_values) + suit_values[my_card.suit]


print('~~构建~~~~~~~~~~~~~~~~~~~~~~~~~~')
deck = FrenchDeck()  # 构建一副牌 __init__
print('牌的数量 = %d' % len(deck))  # __len__
print('随机抽一张牌：{}'.format(random.choice(deck)))  # __getitem__

print('~~修改~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('打印第 1，2 张牌：{}'.format(deck[:2]))  # __getitem__
deck[0] = Card('4', 'hearts')  # __setitem__
print('打印第 1，2 张牌：{}'.format(deck[:2]))  # __getitem__

print('~~排序~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('按牌的大小，降序排列，使用多变量循环限制打印数量为 3 张')
for i, card in zip(range(4), sorted(deck, key=spades_high, reverse=False)):
    print(card)

print('~~洗牌~~~~~~~~~~~~~~~~~~~~~~~~~~')
length = len(deck)
for i in range(0, length - 1):

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
