#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse

def conv_lat_lng(infile, outfile):
    list_result = []
    with open(infile, "r", encoding = 'utf_8') as in_f:
        for row in in_f:
            if row != "":
                row = row.rstrip()
                list_tmp = row.split(' ')
                print(list_tmp)
                list_result.append(list_tmp[1] + ' ' + list_tmp[0] +  '\n')
    
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
    conv_lat_lng(input_file, output_file)

    print("Done!")