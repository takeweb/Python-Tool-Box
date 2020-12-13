#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse

def conv_snake_2_Camel(infile, outfile):
    # camelCaseをsnake_caseへ変換
    list_result = []
    with open(infile, "r", encoding = 'utf_8') as in_f:
        for row in in_f:
            if row != "":
                list_tmp = row.split('_')
                for i, row in enumerate(list_tmp):
                    if i > 0:
                        list_tmp[i] = list_tmp[i].capitalize()
                list_result.append("".join(list_tmp))

    with open(outfile, "w", encoding = 'utf_8', newline='\n') as out_f:
        out_f.writelines(list_result)

if __name__ == '__main__':
     # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default="./input.txt")
    parser.add_argument('-o', '--output', default="./output.txt")

    # コマンドライン引数受け取り
    args = parser.parse_args()
    input_file = str(args.input)
    output_file = str(args.output)

    # 元ファイルの存在チェック
    if not os.path.exists(input_file):
        print("ファイルが存在しません")
        sys.exit()

    # 変換実行
    conv_snake_2_Camel(input_file, output_file)

    print("Done!")