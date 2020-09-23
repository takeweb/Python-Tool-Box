#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse, datetime, pathlib

# モジュールのあるパスを追加
sys.path.append('/Users/oishi/develop/python3/Python-Tool-Box/99_common/util')

import dateUtil

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--date')
        parser.add_argument('-w', '--week_flg', default=0)

        # コマンドライン引数受け取り
        args = parser.parse_args()
        arg_date = str(args.date)
        arg_week_flg = bool(int(args.week_flg))

        # 西暦→和暦変換実行
        print(dateUtil.convSeirekiToWareki(arg_date, arg_week_flg)) 

    except Exception as e:
        print(e)

 