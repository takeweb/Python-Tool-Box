#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse, datetime

def convSeirekiToWareki(inputDate):
    MEIJI = datetime.date(1868, 10, 23)
    TAISHO = datetime.date(1912, 7, 30)
    SHOWA = datetime.date(1926, 12, 25)
    HEISEI = datetime.date(1989, 1, 8)
    REIWA = datetime.date(2019, 5, 1)

    if inputDate >= MEIJI and inputDate < TAISHO:
        wareki = "明治"
        wareki_year = inputDate.year - (MEIJI.year - 1)
    elif inputDate >= TAISHO and inputDate < SHOWA:
        wareki = "大正"
        wareki_year = inputDate.year - (TAISHO.year - 1)
    elif inputDate >= SHOWA and inputDate < HEISEI:
        wareki = "昭和"
        wareki_year = inputDate.year - (SHOWA.year - 1)
    elif inputDate >= HEISEI and inputDate < REIWA:
        wareki = "平成"
        wareki_year = inputDate.year - (HEISEI.year - 1)
    elif inputDate >= REIWA:
        wareki = "令和"
        wareki_year = inputDate.year - (REIWA.year - 1)
    else:
        wareki = "変換不可"

    if wareki_year == 1:
        wareki_year = "元"

    return wareki + str(wareki_year) + "年"

if __name__ == '__main__':
    w_list = ['月', '火', '水', '木', '金', '土', '日']
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--date')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        arg_date = str(args.date)
        input_date = datetime.date(int(arg_date[0:4]), int(arg_date[4:6]), int(arg_date[6:8]))

        # 変換実行
        after = convSeirekiToWareki(input_date)
        print("{0}年{1}月{2}日({3})".format(after
                                            , str(input_date.month)
                                            , str(input_date.day)
                                            , w_list[input_date.weekday()]))
    except Exception as e:
        print(e)

 