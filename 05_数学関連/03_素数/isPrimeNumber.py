#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, argparse

# 素数判定
def isPrimeNumber(targer_num):
    if targer_num == 1:
        return False

    for n in range(2, targer_num):
        if targer_num % n == 0:
            return False
    return True

# 素数判定
def isPrimeNumberFast(targer_num):
    if targer_num == 1:
        return False

    for n in range(2, int(math.sqrt(targer_num)) + 1):
        if targer_num % n == 0:
            return False
    return True

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--num')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        num = int(args.num)
    
        #print(isPrimeNumber(num))
        print(isPrimeNumberFast(num))
    except Exception as e:
        print(e)

