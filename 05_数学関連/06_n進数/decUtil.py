#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def convert_dec_to_any(target, target_div):
    # 10進数をm進数へ変換する
    amari = []
    target = int(target)

    while target != 0:
        amari.append(target % target_div)
        target = target // target_div

    if target_div == 16:
        for i in range(len(amari)):
            if amari[i] == 10:
                amari[i] = 'A'
            elif amari[i] == 11:
                amari[i] = 'B'
            elif amari[i] == 12:
                amari[i] = 'C'
            elif amari[i] == 13:
                amari[i] = 'D'
            elif amari[i] == 14:
                amari[i] = 'E'
            elif amari[i] == 15:
                amari[i] = 'F'

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
        if target[i] == 'A':
            num = 10
        elif target[i] == 'B':
            num = 11
        elif target[i] == 'C':
            num = 12
        elif target[i] == 'D':
            num = 13
        elif target[i] == 'E':
            num = 14
        elif target[i] == 'F':
            num = 15
        else:
            num = int(target[i])
        sum += (m ** n) * num
        n -= 1

    return sum

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
            # 10進数をm進数へ変換する
            result= convert_dec_to_any(num, div)
        else:
            # m進数を10進数へ変換する
            result= convert_any_to_dec(num, div)
    
        print(result)

    except Exception as e:
        print(e)