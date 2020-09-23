#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, argparse

def getListPrimeNumber(max_num):
    # 指定された最大値までの素数のリストを返却
    sosuu_list = []
    zyogai_list = []
    for min_num in range(2, max_num + 1):
        if min_num not in zyogai_list:
            sosuu_list.append(min_num)
            for target in range(min_num + 1, max_num + 1):
                if target % min_num == 0:
                    zyogai_list.append(target)
    return sosuu_list

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--max', default=50)

        # コマンドライン引数受け取り
        args = parser.parse_args()
        max_num = int(args.max)

        result_list = getListPrimeNumber(max_num)
    
        print(result_list)
    except Exception as e:
        print(e)

