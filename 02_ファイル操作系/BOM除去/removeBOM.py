#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, shutil, argparse

def removeBom(fileFrom):
    # BOM(Byte Order Mark)を除去
    with open(fileFrom, "r", encoding = 'utf_8_sig') as in_f:
        with open("tmp_file", "w", encoding = 'UTF-8') as out_f:
            for str in in_f:
                out_f.write(str)

    # 元ファイルを変換後の内容で上書き
    shutil.move("tmp_file", fileFrom)

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        arg_input = str(args.input)

        # ファイル単品の場合
        in_file = arg_input
        if os.path.isfile(in_file):
            # BOM除去実行
            removeBom(in_file)
            sys.exit()
        else:
            # 変換対象ディレクトリの存在チェック
            in_dir = arg_input
            if not os.path.exists(in_dir):
                print("変換元が存在しません")
                sys.exit()

        for dirpath, dirnames, filenames in os.walk(in_dir):
            for filename in filenames:
                print(os.path.join(dirpath, filename))
                in_file = os.path.join(dirpath, filename)

                if os.path.isfile(in_file):
                    # BOM除去実行
                    removeBom(in_file)
    except Exception as e:
        print(e)
