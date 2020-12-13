#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# おみくじ
def getOmikuji():
    omikuji = ["大吉","吉","中吉","小吉","半吉","末吉","平","凶","小凶","半凶","末凶","大凶"]
    return omikuji[random.randrange(len(omikuji))]

if __name__ == '__main__':
    try:
        print(getOmikuji())
    except Exception as e:
        print(e)
