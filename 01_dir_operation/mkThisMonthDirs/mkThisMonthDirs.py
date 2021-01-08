#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, pathlib, argparse, re, calendar
from util.dateUtil import isBizDay

def mk_this_month_dirs(arg_date):
    # 作成ディレクトリ設定ファイルの存在チェック
    current_dir = pathlib.Path(__file__).resolve().parent
    conf_file = os.path.join(current_dir, "mkdir_list.txt")
    if not os.path.isfile(conf_file):
        print("設定ファイルが存在しません")
        sys.exit(1)

    year = arg_date[0:4]
    month = arg_date[4:6]
    max_day = calendar.monthrange(int(year), int(month))[1]

    # 作成ディレクトリ設定ファイルの読み込み
    with open(conf_file, mode='r', encoding='utf-8') as cfile:
        for row in cfile:
            target_dir = row.rstrip()
            for day in range(1, max_day + 1):
                if isBizDay(datetime.date(int(year), int(month), day)):
                    day = str(day).zfill(2)
                    mkdir_list = [year, year + month, year + month + day]
                    mk_dir = os.path.join(target_dir, *mkdir_list)
                    os.makedirs(mk_dir)
    print("Done!")

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--date', default=datetime.date.today())

        # コマンドライン引数受け取り
        args = parser.parse_args()

        # その月のディレクトリ郡を作成
        mk_this_month_dirs(str(args.date).replace("-", ""))
    
    except Exception as e:
        print(e)

