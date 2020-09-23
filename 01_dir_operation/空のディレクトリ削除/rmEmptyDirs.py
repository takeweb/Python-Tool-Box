#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, re

def is_empty(directory):
    files = os.listdir(directory)
#    files = [f for f in files 
#                if not f.startswith(".")]
    if not files:
        return True
    else:
        return False

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 1:
        print("使い方：" + sys.argv[0])
        sys.exit()

    # 作成ディレクトリ設定ファイルの存在チェック
    conf_file = "./dir_list.txt"
    if not os.path.isfile(conf_file):
        print("設定ファイルが存在しません")
        sys.exit()

    # 当日日付取得・dateへ変換
    dt_now = datetime.datetime.now()
    date_now = datetime.date(dt_now.year, dt_now.month, dt_now.day)

    # ディレクトリ設定ファイルの読み込み
    with open(conf_file, mode='r', encoding='utf-8') as cfile:
        for row in cfile:
            target_dir = row.rstrip()
            for dirpath, dirnames, filenames in os.walk(target_dir):
                for dir in dirnames:
                    if re.compile("^\d{8}$").search(dir):
                        tdate = datetime.date(int(dir[0:4]), int(dir[4:6]), int(dir[6:8]))
                        full_path = os.path.join(dirpath, dir)
                        dir_size = os.path.getsize(full_path)
                        # 空のディレクトリを削除
                        if tdate < date_now and is_empty(full_path):
                            print(full_path + ":" + str(dir_size))
                            os.rmdir(full_path)
    print("Done!")


