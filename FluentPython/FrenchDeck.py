#! python3
# coding=gbk

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'apades diamonds clubs hearts'.split()
