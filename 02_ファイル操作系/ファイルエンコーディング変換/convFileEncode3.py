#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar, os, sys, shutil

def getEuc(replaceString):
    print("変換" + replaceString + "ファイルの文字エンコーディングを指定してください")
    enc_num = input("1:Shift_JIS 2:EUC-JP 3 JIS 4:UTF-8：")
    if enc_num == "1":
        enc = "cp932"
    elif enc_num == "2":
        enc = "euc_jp"
    elif enc_num == "3":
        enc = "iso2022_jp"
    elif enc_num == "4":
        enc = "utf_8"
    else:
        print("エンコーディング指定が正しくありません")
        sys.exit()
    return enc

def fileEncode(fileFrom, encFrom, encTo):
    with open(fileFrom, "r", encoding = encFrom) as in_f:
        with open("tmp_file", "w", encoding = encTo, newline='\n') as out_f:
            for str in in_f:
                # 改行コードをLFに統一
#               str = str.replace('\r\n', '\n')
                out_f.write(str)

    # 元ファイルを変換後の内容で上書き
    shutil.move("tmp_file", fileFrom)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("使い方：" + sys.argv[0] + " dir")
        sys.exit();

    # 変換対象ディレクトリの存在チェック
    in_dir = str(sys.argv[1])
    if not os.path.exists(in_dir):
        print("ディレクトリが存在しません")
        sys.exit()

    # エンコーディング取得
    #enc_from = getEuc("元")
    #enc_to =   getEuc("先")
    enc_from = "utf_8"
    enc_to =   "utf_8"

    for dirpath, dirnames, filenames in os.walk(in_dir):
        for filename in filenames:
            print(os.path.join(dirpath, filename))
            in_file = os.path.join(dirpath, filename)

            if os.path.isfile(in_file):
                # ファイルエンコード実行
                fileEncode(in_file, enc_from, enc_to)
