# -*- coding: utf-8 -*-
from random import randrange

def roll_the_dice():
    dice1 = randrange(6)
    dice2 = randrange(6)
    return 2+dice1+dice2, u'⚀⚁⚂⚃⚄⚅'[dice1] + ' ' + u'⚀⚁⚂⚃⚄⚅'[dice2]
