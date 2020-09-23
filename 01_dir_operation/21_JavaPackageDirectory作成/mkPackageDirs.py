#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, argparse

if __name__ == '__main__':
    # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default="./temp")
    parser.add_argument('-p', '--package')

    # コマンドライン引数受け取り
    args = parser.parse_args()
    base_dir = str(args.dir)
    package_name = str(args.package)

    # ベースディレクトリが存在しない場合は作成
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir)

    # パッケージを「.」で分解
    dir_llist = package_name.split('.')

    # パッケージディレクトリ作成
    target_dir = os.path.join(base_dir, *dir_llist)
    os.makedirs(target_dir)

    print("Done!")
