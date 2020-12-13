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

def saveDb(passwd, current_flg):
    """
    データベースに保存
    """

    conn = sqlite3.connect(db_file)
    conn.execute('''CREATE TABLE IF NOT EXISTS passwd(
                          data_id INTEGER PRIMARY KEY AUTOINCREMENT
                        , passwd TEXT
                        , current_flg INTEGER
                        , regist_datetime TEXT
                        , update_datetime TEXT)''')
    ins = ('''INSERT INTO passwd(passwd, current_flg, regist_datetime, update_datetime)
                VALUES(?, ?, datetime('now', 'localtime'), datetime('now', 'localtime'))''')
    conn.execute(ins, (passwd, current_flg))
    conn.commit()
    conn.close()

def readAllDb():
    """
    データベースから全件取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT 
                    data_id
                    , passwd
                    , current_flg
                    , regist_datetime
                    , update_datetime
                FROM
                    passwd
                ORDER BY
                    data_id'''
    curs.execute(select)
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def readMaxSeq(table_name):
    """
    最大シーケンス取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT seq FROM sqlite_sequence WHERE name = ?'
    curs.execute(select, (table_name,))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row[0]

def readByKeyDb(data_id):
    """
    キーで１件取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT 
                    data_id
                    , passwd
                    , current_flg
                    , regist_datetime
                    , update_datetime
                FROM
                    passwd
                WHERE
                    data_id = ?'''
    curs.execute(select, (data_id,))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row

def getCurrentPw():
    """
    カレントパスワード取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    passwd
                FROM
                    passwd
                WHERE
                    current_flg = 1'''
    curs.execute(select)
    row = curs.fetchone()
    pw = row[0]
    curs.close()
    conn.close()
    return pw

def getNextPws():
    """
    次のパスワード候補を取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    data_id
                    , passwd
                    , regist_datetime
                    , update_datetime
                FROM
                    passwd
                WHERE
                    current_flg = 0
                ORDER BY
                    update_datetime
                    '''
    curs.execute(select)
    rows = curs.fetchall()
    pws = rows
    curs.close()
    conn.close()
    return pws

def changeCurrentPw(data_id, current_flg):
    """
    カレントパスワードを変更
    """
    conn = sqlite3.connect(db_file)
    upd = ('''UPDATE passwd 
            SET
                current_flg = 0
            , update_datetime = datetime('now', 'localtime')
            WHERE current_flg = 1''')
    conn.execute(upd)

    upd = ('''UPDATE passwd 
                SET
                      current_flg = ? 
                    , update_datetime = datetime('now', 'localtime')
                WHERE data_id = ?''')
    conn.execute(upd, (current_flg, data_id))
    conn.commit()
    conn.close()

def updateByKeyDb(data_id, passwd, current_flg):
    """
    キーで更新
    """
    conn = sqlite3.connect(db_file)
    upd = ('''UPDATE passwd 
                SET
                      passwd = ?
                    , current_flg = ? 
                    , update_datetime = datetime('now', 'localtime')
                WHERE data_id = ?''')
    conn.execute(upd, (passwd, current_flg, data_id))
    conn.commit()
    conn.close()

def deleteByKeyDb(data_id):
    """
    キーで削除
    """
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM passwd WHERE data_id = ?')
    conn.execute(delete, (data_id, ))
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
        parser.add_argument('-m', '--mode', default='read_all')
        parser.add_argument('-i', '--data_id')
        parser.add_argument('-p', '--passwd')
        parser.add_argument('-c', '--current_flg', default=0)

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        
        if mode != 'read_all':
            if mode not in ('save', 'get_current_pw', 'get_next_pws'):
                data_id = int(args.data_id)
            passwd = str(args.passwd)
            current_flg = int(args.current_flg)

        # モード切り替え
        if mode == 'save':
            # 登録
            saveDb(passwd, current_flg)
            data_id = readMaxSeq("passwd")
            readByKeyDb(data_id)

        elif mode == 'read_all':
            # 全件取得
            datas = readAllDb()
            for data in datas:
                print(data)

        elif mode == 'get_current_pw':
            # カレントパスワードを取得
            pw = getCurrentPw()
            print(pw)

        elif mode == 'change_current_pw':
            # カレントパスワードを変更
            changeCurrentPw(data_id, current_flg)
            data = readByKeyDb(data_id)
            print(data)

        elif mode == 'get_next_pws':
            # 次のパスワードを取得
            pws = getNextPws()
            for pw in pws:
                print(pw)

        elif mode == 'read_key':
            # キーで検索
            data = readByKeyDb(data_id)
            print(data)

        elif mode == 'upd_key':
            if current_flg == 1:
                # カレントパスワードを変更
                changeCurrentPw(data_id, current_flg)
            # キーで更新
            updateByKeyDb(data_id, passwd, current_flg)
            data = readByKeyDb(data_id)
            print(data)

        elif mode == 'del_key':
            # キーで削除
            deleteByKeyDb(data_id)

        logger.info('end')

    except Exception as e:
        logger.exception('Exception occered: %s', e)
