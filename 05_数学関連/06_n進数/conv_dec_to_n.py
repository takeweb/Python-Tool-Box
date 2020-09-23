#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse

def convert(target, target_div):
    if target_div == 2:
        result = bin(int(target))
    elif target_div == 8:
        result = oct(int(target))
    elif target_div == 16:
        result = hex(int(target))
    else:
        result = target

    return result

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

        if div not in (2, 8, 16, 10):
            print("Error")
            sys.exit()

        if mode == "d2a":
            # 10進数をm進数へ変換する
            result = convert(num, div)
        else:
            # m進数を10進数へ変換する
            result = int(num, div)

        print(result)

    except Exception as e:
        print(e)