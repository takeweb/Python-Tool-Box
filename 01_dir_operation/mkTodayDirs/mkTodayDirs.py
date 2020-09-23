#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, pathlib, argparse, re

def mkTodayDirs(arg_date):
    # 作成ディレクトリ設定ファイルの存在チェック
    current_dir = pathlib.Path(__file__).resolve().parent
    conf_file = os.path.join(current_dir, "mkdir_list.txt")
    if not os.path.isfile(conf_file):
        print("設定ファイルが存在しません")
        sys.exit()

    # 引数チェック
    if re.compile("^\d{8}$").search(arg_date):
        d_target = datetime.date(int(arg_date[0:4])
                                , int(arg_date[4:6])
                                , int(arg_date[6:8]))
    else:
        sys.exit()

    # 日付取得・分解
    year = str(d_target.year)
    month = str(d_target.month).zfill(2)
    day = str(d_target.day).zfill(2)

    # 作成ディレクトリ設定ファイルの読み込み
    with open(conf_file, mode='r', encoding='utf-8') as cfile:
        for row in cfile:
            target_dir = row.rstrip()
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

        # 本日ディレクトリ郡を作成
        mkTodayDirs(str(args.date).replace("-", ""))
    
    except Exception as e:
        print(e)

