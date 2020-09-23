#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# じゃんけん
def getJanken():
    janken = ["グー", "チョキ", "パー"]
    return janken[random.randrange(len(janken))]

if __name__ == '__main__':
    try:
        print(getJanken())
    except Exception as e:
        print(e)
