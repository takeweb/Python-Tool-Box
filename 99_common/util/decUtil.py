#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse

def convert_dec_to_any(target, target_div):
    # 10進数をm進数へ変換する
    amari = []
    target = int(target)

    while target != 0:
        amari.append(target % target_div)
        target = target // target_div

    if target_div == 16:
        for i in range(len(amari)):
            amari[i] = conv_dec_to_hex(amari[i])

    # 要素を反転
    amari.reverse()

    # 要素全部を数値から文字列へ変換
    str_result = [str(n) for n in amari]

    # 文字列にして返却
    return "".join(str_result)

def convert_any_to_dec(target, m):
    # m進数を10進数へ変換する

    target = str(target)

    n = len(target) - 1
    sum = 0

    for i in range(len(target)):
        num = conv_hex_to_dec(target[i])
        sum += (m ** n) * num
        n -= 1

    return sum

def conv_dec_to_hex(target):
    if target == 10:
        rtn_value = 'A'
    elif target == 11:
        rtn_value = 'B'
    elif target == 12:
        rtn_value = 'C'
    elif target == 13:
        rtn_value = 'D'
    elif target == 14:
        rtn_value = 'E'
    elif target == 15:
        rtn_value = 'F'
    else:
        rtn_value = target
    
    return rtn_value

def conv_hex_to_dec(target):
    if target == 'A':
        rtn_value = 10
    elif target == 'B':
        rtn_value = 11
    elif target == 'C':
        rtn_value = 12
    elif target == 'D':
        rtn_value = 13
    elif target == 'E':
        rtn_value = 14
    elif target == 'F':
        rtn_value = 15
    else:
        rtn_value = int(target)
    
    return rtn_value

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mode', default='d2a')
        parser.add_argument('-n', '--num')
        parser.add_argument('-d', '--div', default=2)

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        num = args.num
        div = int(args.div)

        if div not in (2, 8, 16):
            print("Error")
            sys.exit()

        if mode == "d2a":
            # 10進数をn進数へ変換する
            result= convert_dec_to_any(num, div)
        else:
            # m進数を10進数へ変換する
            result= convert_any_to_dec(num, div)
    
        print(result)

    except Exception as e:
        print(e)