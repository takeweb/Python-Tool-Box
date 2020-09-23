#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def separateCamma(fileFrom, outKind):
    # ファイルの内容をカンマ区切りにして返却
    rtn_strs = []
    with open(fileFrom, "r", encoding = 'utf_8') as in_f:
        for row in in_f:
            str = row.rstrip()
            if str != "":
                if outKind == "s":
                    rtn_strs.append("\'" + str + "\'")
                else:
                    rtn_strs.append(str)

    # カンマで区切った文字列を取得して返却
    return ", ".join(rtn_strs)

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file')
        parser.add_argument('-m', '--mode', default="i")

        # コマンドライン引数受け取り
        args = parser.parse_args()
        input_file = str(args.file)
        out_kind = str(args.mode)
    
        # 元ファイルの存在チェック        
        if not os.path.exists(input_file):
            print("ファイルが存在しません")
            sys.exit()
        
        # 関数呼び出し
        result = separateCamma(input_file, out_kind)
        print(result)

    except Exception as e:
        print(e)
