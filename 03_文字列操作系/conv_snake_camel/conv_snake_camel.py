#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse, re

def conv_snake_to_camel(in_string):
    # snake_caseをcamelCaseへ変換
    if in_string == "":
        return ""

    list_tmp = in_string.split('_')
    for i, row in enumerate(list_tmp):
        if i > 0:
            list_tmp[i] = list_tmp[i].capitalize()
    result = "".join(list_tmp)
    
    return result

def conv_camel_to_snake(in_string, upper=False):
    # camelCaseをsnake_caseへ変換
    if in_string == "":
        return ""

    result = re.sub("(.[A-Z])",
                      lambda x: x.group(1)[0] + "_" + x.group(1)[1],
                      in_string)
    if upper:
            result = result.lower().upper()
    else:
        result = result.lower()
    
    return result

if __name__ == '__main__':
     # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default="./input.txt")
    parser.add_argument('-o', '--output', default="./output.txt")
    parser.add_argument('-m', '--mode', default="cs")
    parser.add_argument('-u', '--upper', default=0)

    # コマンドライン引数受け取り
    args = parser.parse_args()
    input_file = str(args.input)
    output_file = str(args.output)
    mode = str(args.mode)
    upper = bool(args.upper)

    # 元ファイルの存在チェック
    if not os.path.exists(input_file):
        print("ファイルが存在しません")
        sys.exit()

    list_result = []

    # 入力ファイル読み込み
    with open(input_file, "r", encoding = 'utf_8') as in_f:
        for row in in_f:
            # 変換実行
            if mode == 'sc':
                result = conv_snake_to_camel(row)
            else:
                result = conv_camel_to_snake(row, upper)
            list_result.append(result)

    # 出力ファイル読み込み
    with open(output_file, "w", encoding = 'utf_8', newline='\n') as out_f:
        out_f.writelines(list_result)

    print("Done!")