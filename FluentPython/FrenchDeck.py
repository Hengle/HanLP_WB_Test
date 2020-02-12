#! python3
# coding=gbk

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


# print(Card)
# field_names = 'rank, suit'
# if isinstance(field_names, str):
#     field_names = field_names.replace(',', ' ').split()
#     print(field_names)
#     x = map(str, field_names)
#     print(list(x))


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'apades diamonds clubs hearts'.split()

    # print(ranks)
    # print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        # print(self._cards[0])

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()  # 构建一副牌
print('牌的数量 = %d' % len(deck))
print('随机抽一张牌：{}'.format(random.choice(deck)))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# for card in deck:  # doctest: +ELLIPSIS
#     print(card)
'''
print(A.__len__())
print(A.__getitem__(2))
print('~~~~~~~~~~~~~~~')
print(A[0])
print(A[1])
print(A[2])
print('~~~~~~~~~~~~~~~')
print(FrenchDeck)
print(A)
print(Card)  # 创建的是一个类
beer_card = Card('7', 'diamonds')
print(beer_card)
print(beer_card())
print(type(beer_card))
'''
