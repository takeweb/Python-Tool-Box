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
        arg_dt_regist = str(arg_dt_regist)
#       if re.compile("^\d{4}/|-\d{2}/|-\d{2} \d{2}:\d{2}:\d{2}$").search(arg_dt_regist):
        if re.compile("^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$").search(arg_dt_regist):
#       if re.compile("^\d{4}\D\d{2}\D\d{2}\D \d{2}:\d{2}:\d{2}$").search(arg_dt_regist):
            dt_regist = datetime.datetime(int(arg_dt_regist[0:4])
                                        , int(arg_dt_regist[5:7])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[11:13])
                                        , int(arg_dt_regist[14:16])
                                        , int(arg_dt_regist[17:19]))
#       elif re.compile("^\d{4}/|-\d{2}/|-\d{2} \d{2}:\d{2}$").search(arg_dt_regist):
        elif re.compile("^\d{4}/\d{2}/\d{2} \d{2}:\d{2}$").search(arg_dt_regist):
#       elif re.compile("^\d{4}\D\d{2}\D\d{2}\D \d{2}:\d{2}$").search(arg_dt_regist):
            dt_regist = datetime.datetime(int(arg_dt_regist[0:4])
                                        , int(arg_dt_regist[5:7])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[8:10])
                                        , int(arg_dt_regist[11:13])
                                        , int(arg_dt_regist[14:16]))
#       elif re.compile("^\d{4}/|-\d{2}/|-\d{2}$").search(arg_dt_regist):
        elif re.compile("^\d{4}/\d{2}/\d{2}$").search(arg_dt_regist):
#       elif re.compile("^\d{4}\D\d{2}\D\d{2}\D$").search(arg_dt_regist):
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

# 判定
def hantei(bmi):
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi >= 18.5 and bmi < 25:
        result = "標準体型"
    elif bmi >= 25 and bmi < 30:
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
    return result

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
    plt.ylabel("weight(kg)")
    plt.show()

# データベースからグラフ用データ取得
def readAllForGraph(from_date, to_date):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    strftime('%m/%d', date(regist_datetime))
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
    conn.execute('''CREATE TABLE IF NOT EXISTS health(
                          data_id INTEGER PRIMARY KEY AUTOINCREMENT
                        , regist_datetime TEXT
                        , height FLOAT
                        , weight FLOAT
                        , bmi FLOAT)''')
    ins = ('INSERT INTO health(regist_datetime, height, weight, bmi) VALUES(?, ?, ?, ?)')
    conn.execute(ins, (regist_datetime, height, weight, bmi))
    conn.commit()
    conn.close()

# データベースから全件取得
def readAllDb():
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT 
                    data_id
                    , regist_datetime
                    , height
                    , weight
                    , bmi
                FROM
                    health
                ORDER BY
                    regist_datetime'''
    curs.execute(select)
    rows = curs.fetchall()
    print(rows)
    curs.close()
    conn.close()

# 最大シーケンス取得
def readMaxSeq(table_name):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT seq FROM sqlite_sequence WHERE name = ?'
    curs.execute(select, (table_name,))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row[0]

# キーで１件取得
def readByKeyDb(data_id):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    data_id
                    , regist_datetime
                    , height
                    , weight
                    , bmi
                FROM
                    health
                WHERE
                    data_id = ?'''
    curs.execute(select, (data_id,))
    row = curs.fetchone()
    print(row)
    curs.close()
    conn.close()

# キーで更新
def updateByKeyDb(data_id, regist_datetime, height, weight, bmi):
    conn = sqlite3.connect(db_file)
    upd = ('''UPDATE health 
                SET
                    regist_datetime = ?
                    , height = ? 
                    , weight = ? 
                    , bmi = ?
                WHERE data_id = ?''')
    conn.execute(upd, (regist_datetime, height, weight, bmi, data_id))
    conn.commit()
    conn.close()

# キーで削除
def deleteByKeyDb(data_id):
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM health WHERE data_id = ?')
    conn.execute(delete, (data_id, ))
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
        parser.add_argument('-i', '--data_id')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        height = float(args.height)
        weight = float(args.weight)
        dt_regist = getRegistDatetime(args.dt_regist)
        from_date = str(args.from_date)
        to_date = str(args.to_date)
        data_id = str(args.data_id)

        # BMIと適正体重を計算
        bmi = calcBmi(height, weight)
        suitableWeight = calcSuitableWeight(height)

        if mode == 'save':
            result = hantei(bmi)
            print("BMI(Body Mass Index): " + str(bmi) + " / 判定: " + result)
            print("適正体重:" + str(suitableWeight))
            saveDb(dt_regist, height, weight, bmi)
            data_id = readMaxSeq("health")
            readByKeyDb(data_id)
        elif mode == 'read_all':
            readAllDb()
        elif mode == 'read_key':
            readByKeyDb(data_id)
        elif mode == 'del_key':
            deleteByKeyDb(data_id)
        elif mode == 'upd_key':
            updateByKeyDb(data_id, dt_regist, height, weight, bmi)
        else:
            data = readAllForGraph(from_date, to_date)
            print(data)
            dispGraph(data)
    except Exception as e:
        print(e)
