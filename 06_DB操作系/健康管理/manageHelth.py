#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, os, pathlib, calendar
from util.dateUtil import conv_str_datetime
from util.loggingUtil import get_logger
from lib import lib_com
from lib import lib_db
from lib import lib_health

if __name__ == '__main__':
    try:
        dt_today = datetime.datetime.today()
        current_dir = pathlib.Path(__file__).resolve().parent

        # 設定ファイル読み込み
        settings = lib_com.get_settings(current_dir)
        height = float(settings["height"])
        target_weight = float(settings["target_weight"])

        # DBファイル準備
        db_file = os.path.join(current_dir, settings["db_file"])

        # ロガー準備
        log_filename = settings["log_filename"] + '_' + dt_today.strftime('%Y%m%d') + '.log'
        logger = get_logger(__name__, log_filename)
        logger.info('start:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

        # コマンドライン引数設定
        parser = lib_com.init_argument_parser(height, dt_today)

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
            # 前回最新データ取得
            before_data = lib_db.select_by_key(db_file, lib_db.select_max_seq(db_file, "health"))
            before = before_data[3]

            # 登録
            lib_db.save(db_file, dt_regist, height, weight, lib_health.show_bmi(height, weight, target_weight, before))

        elif mode == 'select_all':
            # 全件取得
            datas = lib_db.select_all(db_file)
            for data in datas:
                print(data)

        elif mode == 'read_key':
            # キーで検索
            data = lib_db.select_by_key(db_file, data_id)
            print(data)

        elif mode == 'del_key':
            # キーで削除
            lib_db.delete_by_key(db_file, data_id)

        elif mode == 'upd_key':
            bmi = lib_health.calc_bmi(height, weight)
            # キーで更新
            lib_db.update_by_key(db_file, data_id, dt_regist, height, weight, bmi)

        elif mode == 'show_bmi':
            # BMIを計算・表示
            lib_health.show_bmi(height, weight, target_weight)

        elif mode == 'show_monthly_graph':
            # 年月指定でグラフ表示
            target_year_month = str(target_year_month)
            from_date = datetime.date(int(target_year_month[0:4]), int(target_year_month[4:6]), 1)
            print(from_date)
            to_date = from_date.replace(day=calendar.monthrange(from_date.year, from_date.month)[1])
            print(to_date)
            data = lib_db.select_all_for_graph(db_file, str(from_date), str(to_date))            
            print(data)
            disp_year_month = target_year_month[0:4] + '/' + target_year_month[4:6]
            lib_health.disp_graph(data, str(disp_year_month))

        elif mode == 'show_past_month_graph':
            # 直近１ヶ月をグラフ表示
            if to_date == "None":
                dt_to_date = datetime.datetime.today()
                to_date = str(dt_to_date.strftime('%Y-%m-%d'))
            else:
                dt_to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')

            dt_from_date = datetime.datetime(dt_to_date.year, dt_to_date.month - 1, dt_to_date.day + 1)
            from_date = str(dt_from_date.strftime('%Y-%m-%d'))
            print(to_date)
            print(from_date)

            data = lib_db.select_all_for_graph(db_file, str(from_date), str(to_date))            
            print(data)
            lib_health.disp_graph(data, str(from_date) + '~' + str(to_date))

        elif mode == 'max_weight':
            # 最大体重だった日のデータを表示
            max_weight = lib_db.select_max_weight(db_file)
            print(max_weight)

        elif mode == 'min_weight':
            # 最小体重だった日のデータを表示
            min_weight = lib_db.select_min_weight(db_file)
            print(min_weight)

        else:
            # 期間指定でグラフ表示
            data = lib_db.select_all_for_graph(db_file, from_date, to_date)
            print(data)
            lib_health.disp_graph(data, from_date + '~' + to_date)

        logger.info('end:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    except Exception as e:
        logger.exception('Exception occered: %s', e)
        print('Exception occered: %s', e)
