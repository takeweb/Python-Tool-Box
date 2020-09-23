#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar, os, sys, shutil

def fileEncode(fileFrom, encFrom, encTo):
    with open(fileFrom, "r", encoding = encFrom) as in_f:
        with open("tmp_file", "w", encoding = encTo, newline='\n') as out_f:
            for str in in_f:
                out_f.write(str)

    # 元ファイルを変換後の内容で上書き
    shutil.move("tmp_file", fileFrom)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("使い方：" + sys.argv[0] + " file/dir")
        sys.exit();

    enc_from = "cp932"
    enc_to =   "utf_8"

    # ファイル単品の場合
    in_file = str(sys.argv[1])
    if os.path.isfile(in_file):
        # ファイルエンコード実行
        fileEncode(in_file, enc_from, enc_to)
        sys.exit()
    else:
        # 変換対象ディレクトリの存在チェック
        in_dir = str(sys.argv[1])
        if not os.path.exists(in_dir):
            print("変換元が存在しません")
            sys.exit()

    for dirpath, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            print(os.path.join(dirpath, filename))
            in_file = os.path.join(dirpath, filename)

            if os.path.isfile(in_file):
                # ファイルエンコード実行
                fileEncode(in_file, enc_from, enc_to)
