#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, re, sqlite3, datetime, sys

DATABASE_FILE = './book.db'

# チェックデジット(ISBN-13)算出
# 引数の形式：978-4-10-109205
# 978-4-10-109205-?
def calcCheckDegit13(input):
    result = 0
    mw_flg = True
    input = input.replace('-', '')
    int_list = []

    for i in range(0, 12):
        int_list.append(int(input[i:i+1]))

    for target in int_list:
        if mw_flg:
            result += target * 1
            mw_flg = False
        else:
            result += target * 3
            mw_flg = True

    if result % 10 == 0:
        result = 0
    else:
        result = 10 - result % 10

    return result

# チェックデジット(ISBN-10)
# 引数の形式：4-10-109205
# 4-10-109205-?
def calcCheckDegit10(input):
    result = 0
    mw_flg = True
    input = input.replace('-', '')
    int_list = []
    for i in range(0, 9):
        int_list.append(int(input[i:i+1]))

    x = 10
    for target in int_list:
        result += target * x
        x -= 1

    result1 = result % 11
    result2 = 11 - result1
    return result2

def decipherCcode(input):
    keta1 = ("一般","教養","実用","専門","","婦人","学参Ⅰ(小中)","学参Ⅱ(高校)","児童","雑誌扱い")
    keta2 = ("単行本","文庫","新書","全集・双書","ムック・その他","事・辞典","図鑑","絵本","磁性媒体など","コミック")
    keta3 = {'00': "総記", '01': "百科事典", '04': "情報科学", '10': "哲学", \
                '11': "心理(学)", '12': "倫理(学)", '14': "宗教", '15': "仏教", '16': "キリスト教", \
                '20': "歴史", '21': "日本歴史", '23': "海外歴史", '25': "地理", '26': "旅行", \
                '30': "社会科学総記", '31': "政治・含む国防軍事", '32': "法律", '33': "経済・財政・統計", '34': "経営", '36': "社会", '37': "教育", '39': "民族・風習", \
                '40': "自然科学総記", '41': "数学", '42': "物理学", '43': "化学", '44': "天文・地学", '45': "生物学", '47': "医学・歯学・薬学", \
                '50': "工学・工学総記", '51': "土木", '52': "建築", '53': "機械", '54': "電気", '55': "電子通信", '56': "海事", '57': "採鉱・冶金", '58': "その他の工業", \
                '60': "産業総記", '61': "農林業", '62': "水産業", '63': "商業", '65': "交通・通信", \
                '70': "芸術総記", '71': "絵画・彫刻", '72': "写真・工芸", '73': "音楽・舞踊", '74': "演劇・映画", '75': "体育・スポーツ", '75': "諸芸・娯楽", '77': "家事", '79': "コミックス・劇画", \
                '80': "語学総記", '81': "日本語", '82': "英米語", '84': "ドイツ語", '85': "フランス語", '87': "各国語",  \
                '90': "文学総記", '91': "日本文学総記", '92': "日本文学詩歌", '93': "日本文学、小説、物語", '95': "日本文学、評論、随筆、その他", '97': "外国文学小説", '98': "外国文学、その他"}
    tmp1 = input[0:1]
    tmp2 = input[1:2]
    tmp3 = input[2:4]
    result1 = keta1[int(tmp1)]
    result2 = keta2[int(tmp2)]
    result3 = keta3[tmp3]
    return result1 + "・" + result2 + "・" + result3

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

# データベースに保存
def saveDb(regist_datetime, height, weight):
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute('CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, height FLOAT, weight FLOAT, bmi FLOAT)')
    ins = ('INSERT INTO health VALUES(?, ?, ?, ?)')
    conn.execute(ins, (regist_datetime, height, weight, calcBmi(height, weight)))
    conn.commit()
    conn.close()

# データベースから全件取得
def readAllDb():
    conn = sqlite3.connect(DATABASE_FILE)
    curs = conn.cursor()
    select = 'SELECT regist_datetime, height, weight, bmi FROM health ORDER BY regist_datetime'
    curs.execute(select)
    rows = curs.fetchall()
    print(rows)
    curs.close()
    conn.close()

# データベースから１件取得
def readByKeyDb(regist_datetime):
    conn = sqlite3.connect(DATABASE_FILE)
    curs = conn.cursor()
    select = 'SELECT regist_datetime, height, weight, bmi FROM health WHERE regist_datetime = ?'
    curs.execute(select, (regist_datetime,))
    row = curs.fetchone()
    print(row)
    curs.close()
    conn.close()

# キーで更新
def updateByKeyDb(regist_datetime, height, weight):
    conn = sqlite3.connect(DATABASE_FILE)
    upd = ('UPDATE health SET height = ?, weight = ?, bmi = ? WHERE regist_datetime = ?')
    conn.execute(upd, (height, weight, calcBmi(height, weight), regist_datetime))
    conn.commit()
    conn.close()

# キーで削除
def deleteByKeyDb(regist_datetime):
    conn = sqlite3.connect(DATABASE_FILE)
    delete = ('DELETE FROM health WHERE regist_datetime = ?')
    conn.execute(delete, (regist_datetime, ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mode')
        parser.add_argument('-i', '--isbn')
        parser.add_argument('-c', '--ccode')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        isbn = str(args.isbn)
        ccode = str(args.ccode)

        if mode == "13":
            print(calcCheckDegit13(isbn))
        elif mode == "10":
            print(calcCheckDegit10(isbn))
        else:
            print(decipherCcode(ccode))
    except Exception as e:
        print(e)
