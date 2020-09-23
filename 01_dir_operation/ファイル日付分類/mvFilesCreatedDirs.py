#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime, platform, shutil, argparse

def get_create_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            return stat.st_mtime

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--dir')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        target_dir = args.dir

        file_list = os.listdir(target_dir)

        # .始まりのファイル名のファイルを除外(.DS_Store等)
        file_list = [f for f in file_list if not f.startswith(".")]

        for filename in file_list:
            full_path = os.path.join(target_dir, filename)
            if os.path.isfile(full_path):
                create_date = get_create_date(full_path)
                dt_create_date = datetime.datetime.fromtimestamp(create_date)
                print(filename + " created:" + dt_create_date.strftime('%Y/%m/%d'))

                # targetdir/yyyy/yyyymm/yyyymmdd
                to_dir_list = [target_dir, 
                            str(dt_create_date.year), 
                            str(dt_create_date.year) + str(dt_create_date.month).zfill(2), 
                            str(dt_create_date.year) + str(dt_create_date.month).zfill(2) + str(dt_create_date.day).zfill(2)]
                to_dir = os.path.join(target_dir, *to_dir_list)
                if not os.path.isdir(to_dir):
                    os.makedirs(to_dir)
                to_path = shutil.move(full_path, to_dir)
                print(to_path)

        print("Done!")

    except Exception as e:
        print(e)


