#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, argparse

def getGreatestCommonDivisor(num1, num2):
    # 最大公約数を算出
    if num2 < num1:
        num1, num2 = num2, num1
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1

def getLeastCommonMultiple(num1, num2):
    # 最小公倍数を算出
    multi = num1 * num2
    gcd = getGreatestCommonDivisor(num1, num2)
    lcd = multi / gcd
    
    return round(lcd)

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-n1', '--num1')
        parser.add_argument('-n2', '--num2')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        num1 = int(args.num1)
        num2 = int(args.num2)
    
        gcd = getGreatestCommonDivisor(num1, num2)
        print("最大公約数：" + str(gcd))

        lcd = getLeastCommonMultiple(num1, num2)
        print("最小公倍数：" + str(lcd))
    except Exception as e:
        print(e)
