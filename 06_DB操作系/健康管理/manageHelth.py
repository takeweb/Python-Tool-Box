#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, datetime, os, pathlib, re, sqlite3, sys, json
import matplotlib.pyplot as plt
from util.dateUtil import conv_str_datetime
from util.loggingUtil import get_logger
import calendar

db_file = ""

def get_settings():
    json_file = open('settings.json', 'r')
    json_data = json.load(json_file)

    return json_data

def calc_bmi(cm_height, weight):
    """
    BMIを算出

    Parameters
    ----------
    cm_height : fload
        身長(cm)
    weight : float
        体重(kg)

    Returns
    -------
    bmi : float
        BMI値
    """
    m_height = cm_height / 100
    bmi = round(weight / m_height ** 2, 2)
    return bmi

def calc_suitable_weight(cm_height):
    """
    適正体重を算出
    """
    m_height = cm_height / 100
    suitableWeight = round(m_height ** 2 * 22, 1)
    return suitableWeight

def hantei_bmi(bmi):
    """
    BMI判定
    """
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi >= 18.5 and bmi < 25:
        result = "標準体型"
    elif bmi >= 25 and bmi < 30:
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
    return result

def disp_graph(rows, title_add):
    """
    グラフ表示
    """
    dt_list = []
    weight_list = []
    for row in rows:
        dt_list.append(row[0])
        weight_list.append(row[1])
    plt.plot(dt_list, weight_list)
    plt.grid(color='0.8')
    plt.title("Weight Transition:" + title_add)
    plt.xlabel("days")
    plt.ylabel("weight(kg)")
    plt.show()

def select_all_for_graph(from_date, to_date):
    """
    データベースからグラフ用データ取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    strftime('%d', date(regist_datetime))
                    , weight 
                FROM health 
                WHERE regist_datetime BETWEEN ? AND ?
                ORDER BY regist_datetime'''
    # 日付で検索する場合、時刻部分がが「00:00:00」で検索されることになるので、
    # TO日時は23:59:59を加算してSQLへバインドする
    dt_to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    dt_to_date = dt_to_date + datetime.timedelta(hours=23, minutes=59)
    to_date = dt_to_date.strftime('%Y-%m-%d %H:%M')
    curs.execute(select, (from_date, to_date))
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def save(regist_datetime, height, weight, bmi):
    """
    データベースに保存
    """
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

def select_all():
    """
    データベースから全件取得
    """
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
    curs.close()
    conn.close()
    return rows

def select_max_seq(table_name):
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

def select_by_key(data_id):
    """
    キーで１件取得
    """
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
    curs.close()
    conn.close()
    return row

def update_by_key(data_id, regist_datetime, height, weight, bmi):
    """
    キーで更新
    """
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

def delete_by_key(data_id):
    """
    キーで削除
    """
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM health WHERE data_id = ?')
    conn.execute(delete, (data_id, ))
    conn.commit()
    conn.close()

def show_bmi():
    # BMIと適正体重を計算
    bmi = calc_bmi(height, weight)
    suitable_weight = calc_suitable_weight(height)

    result_bmi = hantei_bmi(bmi)
    result_suitable_weight = round((suitable_weight - weight) * -1, 2)
    hantei_suitable_weight = 'あと' if result_suitable_weight > 0 else '達成'
    result_target_weight = round((target_weight - weight) * -1, 2)
    hantei_target_weight = 'あと' if result_target_weight > 0 else '達成'

    print("BMI(Body Mass Index): " + str(bmi) + " / 判定: " + result_bmi)
    print("適正体重:" + str(suitable_weight) + "kg" + " / " + hantei_suitable_weight + ": " + str(result_suitable_weight) + "kg！")
    print("目標体重:" + str(target_weight)   + "kg" + " / " + hantei_target_weight   + ": " + str(result_target_weight)   + "kg！")
    return bmi

if __name__ == '__main__':
    dt_today = datetime.datetime.today()

    # 設定ファイル読み込み
    settings = get_settings()
    height = float(settings["height"])
    target_weight = float(settings["target_weight"])

    # DBファイル準備
    current_dir = pathlib.Path(__file__).resolve().parent
    db_file = os.path.join(current_dir, settings["db_file"])

    # ロガー準備
    log_filename = settings["log_filename"] + '_' + dt_today.strftime('%Y%m%d') + '.log'
    logger = get_logger(__name__, log_filename)
    logger.info('start:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mode', default='select_all')
        parser.add_argument('-t', '--height', default=height)
        parser.add_argument('-w', '--weight')
        parser.add_argument('-d', '--dt_regist', default=dt_today)
        parser.add_argument('-from', '--from_date')
        parser.add_argument('-to', '--to_date')
        parser.add_argument('-i', '--data_id')
        parser.add_argument('-tym', '--target_year_month')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        if mode in ('save', 'upd_key', 'show_bmi'):
            height = float(args.height)
            weight = float(args.weight)
        dt_regist = conv_str_datetime(args.dt_regist)
        from_date = str(args.from_date)
        to_date = str(args.to_date)
        data_id = str(args.data_id)
        target_year_month = str(args.target_year_month)

        logger.info('mode=' + mode)
        
        # モード切り替え
        if mode == 'save':
            bmi = show_bmi()

            # 登録
            save(dt_regist, height, weight, bmi)
            data_id = select_max_seq("health")
            select_by_key(data_id)

        elif mode == 'select_all':
            # 全件取得
            datas = select_all()
            for data in datas:
                print(data)

        elif mode == 'read_key':
            # キーで検索
            data = select_by_key(data_id)
            print(data)

        elif mode == 'del_key':
            # キーで削除
            delete_by_key(data_id)

        elif mode == 'upd_key':
            bmi = calc_bmi(height, weight)
            # キーで更新
            update_by_key(data_id, dt_regist, height, weight, bmi)

        elif mode == 'show_bmi':
            # BMIを計算・表示
            show_bmi()

        elif mode == 'show_monthly_graph':
            # 年月指定でグラフ表示
            target_year_month = str(target_year_month)
            from_date = datetime.date(int(target_year_month[0:4]), int(target_year_month[4:6]), 1)
            print(from_date)
            to_date = from_date.replace(day=calendar.monthrange(from_date.year, from_date.month)[1])
            print(to_date)
            data = select_all_for_graph(str(from_date), str(to_date))            
            print(data)
            disp_graph(data, str(target_year_month))

        else:
            # 期間指定でグラフ表示
            data = select_all_for_graph(from_date, to_date)
            print(data)
            disp_graph(data)

        logger.info('end:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    except Exception as e:
        logger.exception('Exception occered: %s', e)
        print('Exception occered: %s', e)
