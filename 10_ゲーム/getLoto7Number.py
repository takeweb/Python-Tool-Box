#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# 1〜37までの整数7個をランダムに出力
def getLotoNumber():
    result = []
    for i in range(1, 8):
        result.append(random.randrange(1, 37))
    result.sort()
    return result

if __name__ == '__main__':
    try:
        list = getLotoNumber()
        # リスト内に重複が無くなるまで繰り返す
        while len(list) != len(set(list)):
            list = getLotoNumber()
        print(list)
    except Exception as e:
        print(e)
