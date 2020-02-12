#! python3
# coding=gbk

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card_value):
        self._cards[position] = card_value


# ��ɫ�ȼ�
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value * len(suit_values) + suit_values[my_card.suit]


deck = FrenchDeck()  # ����һ���� __init__
print('�Ƶ����� = %d' % len(deck))  # __len__
print('�����һ���ƣ�{}'.format(random.choice(deck)))  # __getitem__
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__
deck[0] = Card('4', 'hearts')  # __setitem__
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('���ƵĴ�С���������У�ʹ�ö����ѭ�����ƴ�ӡ����Ϊ 3 ��')
for i, card in zip(range(3), sorted(deck, key=spades_high, reverse=True)):
    print(card)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



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
print(Card)  # ��������һ����
beer_card = Card('7', 'diamonds')
print(beer_card)
print(beer_card())
print(type(beer_card))
'''
