#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar, os, sys, shutil, argparse

def out_analize(input_file, output_file):
    with open(input_file, 'r', encoding = 'utf_8') as in_f:
        with open(output_file, 'w', encoding = 'utf_8', newline='\n') as out_f:
            for str in in_f:
                # 改行コードをLFに統一しつつ、ANALYZE文を生成
                str = "ANALYZE VERBOSE " + str.rstrip() + ";\n"
                out_f.write(str)

def out_count_list(input_file, output_file):
    with open(input_file, 'r', encoding = 'utf_8') as in_f:
        with open(output_file, 'w', encoding = 'utf_8', newline='\n') as out_f:
            for str in in_f:
                # テーブル名とカウントを分割してタブ区切りにする
                list = str.split("|")
                list = [i.strip() for i in list]
                out_f.write("\t".join(list) + "\n")

if __name__ == '__main__':
    # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode')
    parser.add_argument('-i', '--in_file')
    parser.add_argument('-o', '--out_file')

    # コマンドライン引数受け取り
    args = parser.parse_args()
    mode = args.mode
    in_file = args.in_file
    out_file = args.out_file

    # 対象ファイルの存在チェック
    if not os.path.exists(in_file):
        print("対象ファイルが存在しません")
        sys.exit()

    if os.path.isfile(in_file):
        if mode == "analize":
            # ANALYZE文を生成・出力
            out_analize(in_file, out_file)
        else:
            # カウントリスト作成
            out_count_list(in_file, out_file)
    print("Done!!")