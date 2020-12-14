#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, datetime, os, pathlib, re, sqlite3, sys, json
import matplotlib.pyplot as plt
from util.dateUtil import conv_str_datetime
from util.loggingUtil import get_logger

def get_settings():
    json_file = open('settings.json', 'r')
    json_data = json.load(json_file)

    return json_data

def saveDb(passwd):
    """
    データベースに保存
    """
    conn = sqlite3.connect(db_file)
    conn.execute('''CREATE TABLE IF NOT EXISTS ng_passwd(
                        passwd TEXT PRIMARY KEY)''')
    ins = ('''INSERT INTO ng_passwd(passwd)
                VALUES(?)''')
    conn.execute(ins, (passwd, ))
    conn.commit()
    conn.close()

def getNgPw(passwd):
    """
    キーで１件取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    passwd
                FROM
                    ng_passwd
                WHERE
                    passwd = ?'''
    curs.execute(select, (passwd,))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row

def readAllDb():
    """
    データベースから全件取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT 
                    passwd
                FROM
                    ng_passwd
                ORDER BY
                    passwd'''
    curs.execute(select)
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def getNextPw():
    """
    次のパスワード候補を取得
    """
    for i1 in range(0, 10):
        for i2 in range(0, 10):
            for i3 in range(0, 10):
                pw = str(i1) + str(i2) + str(i3)
                if getNgPw(pw):
                    next
                else:
                    return pw

def deleteByPwDb(passwd):
    """
    キーで削除
    """
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM ng_passwd WHERE passwd = ?')
    conn.execute(delete, (passwd, ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 設定ファイル読み込み
    settings = get_settings()

    current_dir = pathlib.Path(__file__).resolve().parent
    db_file = os.path.join(current_dir, settings["db_file"])

    log_filename = settings["log_filename"]
    logger = get_logger(__name__, log_filename)

    logger.info('start')

    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mode', default='get_all')
        parser.add_argument('-p', '--passwd')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        passwd = str(args.passwd)

        # モード切り替え
        if mode == 'save':
            # 登録
            pw = getNgPw(passwd)
            if pw is None or pw[0] != passwd:
                saveDb(passwd)
                pw = getNgPw(passwd)
                print(pw[0])
            else:
                print(passwd + "は既に登録されています。")

        elif mode == 'series_save':
            # 連続登録
            for i in range(0,10):
                tmp_passwd = passwd + str(i)
                pw = getNgPw(tmp_passwd)
                if pw is None or pw[0] != tmp_passwd:
                    saveDb(tmp_passwd)
                    pw = getNgPw(tmp_passwd)
                    print(pw[0])
                else:
                    print(tmp_passwd + "は既に登録されています。")
                    next

        elif mode == 'get_all':
            # 全件取得
            datas = readAllDb()
            for data in datas:
                print(data[0])

        elif mode == 'get_next_pw':
            # 次のパスワードを取得
            pw = getNextPw()
            print(pw)

        elif mode == 'del_pw':
            # パスワード削除
            deleteByPwDb(passwd)

        logger.info('end')

    except Exception as e:
        logger.exception('Exception occered: %s', e)
