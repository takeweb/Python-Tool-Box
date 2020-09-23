#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jpholiday
import pathlib, os, sys, re

MEIJI = datetime.date(1868, 10, 23)
TAISHO = datetime.date(1912, 7, 30)
SHOWA = datetime.date(1926, 12, 25)
HEISEI = datetime.date(1989, 1, 8)
REIWA = datetime.date(2019, 5, 1)

def conv_str_datetime(arg_dt_regist):
    """
    文字列からdatetime型へ変換して返却する。
    """
    
    if isinstance(arg_dt_regist, datetime.datetime):
        dt_regist = arg_dt_regist
    else:
        re1 = re.compile("^(\d{4})\D(\d{2})\D(\d{2})\D* (\d{2}):(\d{2}):(\d{2})$")
        re2 = re.compile("^(\d{4})\D(\d{2})\D(\d{2})\D* (\d{2}):(\d{2})$")
        re3 = re.compile("^(\d{4})\D(\d{2})\D(\d{2})\D*$")
        arg_dt_regist = str(arg_dt_regist)

        if re.search(re1, arg_dt_regist):
            m = re.search(re1, arg_dt_regist)
            gs = m.groups()
            dt_regist = datetime.datetime(int(gs[0]), int(gs[1]), int(gs[2])
                                        , int(gs[3]), int(gs[4]), int(gs[5]))
        elif re.search(re2, arg_dt_regist):
            m = re.search(re2, arg_dt_regist)
            gs = m.groups()
            dt_regist = datetime.datetime(int(gs[0]), int(gs[1]), int(gs[2])
                                        , int(gs[3]), int(gs[4]))
        elif re.search(re3, arg_dt_regist):
            m = re.search(re3, arg_dt_regist)
            gs = m.groups()
            dt_regist = datetime.datetime(int(gs[0]), int(gs[1]), int(gs[2]))
        else:
            sys.exit()

    return dt_regist

def convSeirekiToWareki(arg_date, week_flg=False):
    """
    西暦の年月日(yyyymmdd)を和暦(元号＋年)に変換
    """

    w_list = ['月', '火', '水', '木', '金', '土', '日']
    input_date = datetime.date(int(arg_date[0:4])
                                , int(arg_date[4:6])
                                , int(arg_date[6:8]))

    if input_date >= MEIJI and input_date < TAISHO:
        gengo = "明治"
        wareki_year = input_date.year - (MEIJI.year - 1)
    elif input_date >= TAISHO and input_date < SHOWA:
        gengo = "大正"
        wareki_year = input_date.year - (TAISHO.year - 1)
    elif input_date >= SHOWA and input_date < HEISEI:
        gengo = "昭和"
        wareki_year = input_date.year - (SHOWA.year - 1)
    elif input_date >= HEISEI and input_date < REIWA:
        gengo = "平成"
        wareki_year = input_date.year - (HEISEI.year - 1)
    elif input_date >= REIWA:
        gengo = "令和"
        wareki_year = input_date.year - (REIWA.year - 1)
    else:
        wareki = "変換不可"

    if wareki_year == 1:
        wareki_year = "元"

    if week_flg:
        rtn_str = "{0}年{1}月{2}日({3})".format(gengo + str(wareki_year)
                                    , str(input_date.month), str(input_date.day)
                                    , w_list[input_date.weekday()])
    else:
        rtn_str = "{0}年{1}月{2}日".format(gengo + str(wareki_year)
                                    , str(input_date.month), str(input_date.day)) 

    return rtn_str

def convWarekiToSeireki(input_ymd):
    """
    西暦の年月日(datetime.date)を和暦(元号＋年)に変換
    """

    gengo = input_ymd[0:2]
    wareki_year = input_ymd[2:input_ymd.find("年")]
    if wareki_year == "元":
        wareki_year = "1"
    month = input_ymd[input_ymd.find("年")+1:input_ymd.find("月")]
    day = input_ymd[input_ymd.find("月")+1:input_ymd.find("日")]

    if gengo == "明治":
        seireki_year = int(wareki_year) + (MEIJI.year - 1)
    elif gengo == "大正":
        seireki_year = int(wareki_year) + (TAISHO.year - 1)
    elif gengo == "昭和":
        seireki_year = int(wareki_year) + (SHOWA.year - 1)
    elif gengo == "平成":
        seireki_year = int(wareki_year) + (HEISEI.year - 1)
    elif gengo == "令和":
        seireki_year = int(wareki_year) + (REIWA.year - 1)
    else:
        seireki_year = "変換不可"

    return str(seireki_year) + month.zfill(2) + day.zfill(2)

def isBizDay(dt_date):
    """
    営業日判定
    """

    conf = 'my_holiday.txt'
    current_dir = pathlib.Path(__file__).resolve().parent
    conf_file = os.path.join(current_dir, conf)

    with open(conf_file) as f:
        list_my_holiday = f.readlines()
    
    list_my_holiday2 = [datetime.date(int(i.split('-')[0]), int(i.split('-')[1]), int(i.split('-')[2])) for i in list_my_holiday]

    if dt_date.weekday() >= 5 or jpholiday.is_holiday(dt_date) or dt_date in list_my_holiday2:
        return False
    else:
        return True