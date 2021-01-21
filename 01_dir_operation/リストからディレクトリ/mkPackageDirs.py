#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, argparse

if __name__ == '__main__':
    # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default="./list.txt")

    # コマンドライン引数受け取り
    args = parser.parse_args()
    list_file = str(args.file)

    with open(list_file, "r", encoding = 'utf_8') as in_f:
        for target_dir in in_f:
            os.makedirs(target_dir.rstrip())

    print("Done!")
