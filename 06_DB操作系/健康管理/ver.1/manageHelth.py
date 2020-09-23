#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, re, sqlite3, datetime, sys, pathlib, os
import matplotlib.pyplot as plt

DATABASE_FILE = 'healthcare.db'
current_dir = pathlib.Path(__file__).resolve().parent
db_file = os.path.join(current_dir, DATABASE_FILE)

# 登録日時取得
def getRegistDatetime(arg_dt_regist):
    if isinstance(arg_dt_regist, datetime.datetime):
        dt_regist = arg_dt_regist
    else:
        if re.compile("^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$").search(arg_dt_regist):
            dt_regist = datetime.datetime(int(arg_dt_regist[0:4])
                                        , int(arg_dt_regist[5:7])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[11:13])
                                        , int(arg_dt_regist[14:16])
                                        , int(arg_dt_regist[17:19]))
        elif re.compile("^\d{4}/\d{2}/\d{2} \d{2}:\d{2}$").search(arg_dt_regist):
            dt_regist = datetime.datetime(int(arg_dt_regist[0:4])
                                        , int(arg_dt_regist[5:7])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[11:13])
                                        , int(arg_dt_regist[14:16]))
        elif re.compile("^\d{4}/\d{2}/\d{2}$").search(arg_dt_regist):
            dt_regist = datetime.datetime(int(arg_dt_regist[0:4])
                                        , int(arg_dt_regist[5:7])
                                        , int(arg_dt_regist[8:10]))
        else:
            sys.exit()
    return dt_regist

# BMIを算出
def calcBmi(cm_height, weight):
    m_height = cm_height / 100
    bmi = round(weight / m_height ** 2, 2)
    return bmi

# 適正体重を算出
def calcSuitableWeight(cm_height):
    m_height = cm_height / 100
    suitableWeight = round(m_height ** 2 * 22, 2)
    return suitableWeight

# グラフ表示
def dispGraph(rows):
    dt_list = []
    weight_list = []
    for row in rows:
        dt_list.append(row[0])
        weight_list.append(row[1])
    plt.plot(dt_list, weight_list)
    plt.grid(color='0.8')
    plt.title("Weight Transition")
    plt.xlabel("days")
    plt.ylabel("weight")
    plt.show()

# データベースからグラフ用データ取得
def readAllForGraph(from_date, to_date):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    strftime('%Y/%m/%d', date(regist_datetime))
                    , weight 
                FROM health 
                WHERE regist_datetime BETWEEN  ? AND ?
                ORDER BY regist_datetime'''
    curs.execute(select, (from_date, to_date))
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

# データベースに保存
def saveDb(regist_datetime, height, weight, bmi):
    conn = sqlite3.connect(db_file)
    conn.execute('CREATE TABLE IF NOT EXISTS health(regist_datetime TEXT PRIMARY KEY, height FLOAT, weight FLOAT, bmi FLOAT)')
    ins = ('INSERT INTO health VALUES(?, ?, ?, ?)')
    conn.execute(ins, (regist_datetime, height, weight, bmi))
    conn.commit()
    conn.close()

# データベースから全件取得
def readAllDb():
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT regist_datetime, height, weight, bmi FROM health ORDER BY regist_datetime'
    curs.execute(select)
    rows = curs.fetchall()
    print(rows)
    curs.close()
    conn.close()

# キーで１件取得
def readByKeyDb(regist_datetime):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT regist_datetime, height, weight, bmi FROM health WHERE regist_datetime = ?'
    curs.execute(select, (regist_datetime,))
    row = curs.fetchone()
    print(row)
    curs.close()
    conn.close()

# データベースから１件取得
def readByKeyDb(regist_datetime):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT regist_datetime, height, weight, bmi FROM health WHERE regist_datetime = ?'
    curs.execute(select, (regist_datetime,))
    row = curs.fetchone()
    print(row)
    curs.close()
    conn.close()

# キーで更新
def updateByKeyDb(regist_datetime, height, weight, bmi, upd_date):
    if upd_date == "":
        upd_date = regist_datetime
    else:
        upd_date = getRegistDatetime(regist_datetime)

    conn = sqlite3.connect(db_file)
    upd = ('''UPDATE health 
                SET
                    regist_datetime = ?
                    , height = ? 
                    , weight = ? 
                    , bmi = ?
                WHERE regist_datetime = ?''')
    conn.execute(upd, (upd_date, height, weight, bmi, regist_datetime))
    conn.commit()
    conn.close()

# キーで削除
def deleteByKeyDb(regist_datetime):
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM health WHERE regist_datetime = ?')
    conn.execute(delete, (regist_datetime, ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mode', default='read_all')
        parser.add_argument('-t', '--height', default=176)
        parser.add_argument('-w', '--weight', default=80)
        parser.add_argument('-d', '--dt_regist', default=datetime.datetime.today())
        parser.add_argument('-f', '--from_date')
        parser.add_argument('-to', '--to_date')
        parser.add_argument('-u', '--upd_date')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        height = float(args.height)
        weight = float(args.weight)
        dt_regist = getRegistDatetime(args.dt_regist)
        from_date = str(args.from_date)
        to_date = str(args.to_date)
        upd_date = str(args.upd_date)
        if upd_date == "":
            upd_date = getRegistDatetime(args.upd_date)

        # BMIと適正体重を計算
        bmi = calcBmi(height, weight)
        suitableWeight = calcSuitableWeight(height)

        if mode == 'save':
            if bmi < 18.5:
                result = "痩せ型"
            elif bmi >= 18.5 and bmi < 25:
                result = "標準体型"
            elif bmi >= 25 and bmi < 30:
                result = "肥満(軽)"
            else:
                result = "肥満(重)"
            print("BMI(Body Mass Index): " + str(bmi) + " / 判定: " + result)
            print("適正体重:" + str(suitableWeight))
            saveDb(dt_regist, height, weight, bmi)
            readByKeyDb(dt_regist)
        elif mode == 'read_all':
            readAllDb()
        elif mode == 'read_key':
            readByKeyDb(dt_regist)
        elif mode == 'del_key':
            deleteByKeyDb(dt_regist)
        elif mode == 'upd_key':
            updateByKeyDb(dt_regist, height, weight, bmi, upd_date)
        else:
            data = readAllForGraph(from_date, to_date)
            dispGraph(data)
    except Exception as e:
        print(e)
