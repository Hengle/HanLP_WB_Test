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


# ��ɫ�ȼ�
suit_values = dict(xxx=4, spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value * len(suit_values) + suit_values[my_card.suit]


print('~~����~~~~~~~~~~~~~~~~~~~~~~~~~~')
deck = FrenchDeck()  # ����һ���� __init__
print('�Ƶ����� = %d' % len(deck))  # __len__
print('�����һ���ƣ�{}'.format(random.choice(deck)))  # __getitem__

print('~~�޸�~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__
deck[0] = Card('4', 'hearts')  # __setitem__
print('��ӡ�� 1��2 ���ƣ�{}'.format(deck[:2]))  # __getitem__

print('~~����~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('���ƵĴ�С���������У�ʹ�ö����ѭ�����ƴ�ӡ����Ϊ 3 ��')
for i, card in zip(range(4), sorted(deck, key=spades_high, reverse=False)):
    print(card)

print('~~ϴ��~~~~~~~~~~~~~~~~~~~~~~~~~~')
length = len(deck)
for i in range(0, length - 1):

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
