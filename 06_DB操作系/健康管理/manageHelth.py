#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, os, pathlib, calendar
from util.dateUtil import conv_str_datetime
from util.dateUtil import get_one_month_before
from util.loggingUtil import get_logger
from lib import util_com
from lib import util_db
from lib import util_health

if __name__ == '__main__':
    try:
        dt_today = datetime.datetime.today()
        current_dir = pathlib.Path(__file__).resolve().parent

        # 設定ファイル読み込み
        settings = util_com.get_settings(current_dir)
        height = float(settings["height"])
        target_weight = float(settings["target_weight"])

        # DBファイル準備
        db_file = os.path.join(current_dir, settings["db_file"])

        # ロガー準備
        log_filename = settings["log_filename"] + '_' + dt_today.strftime('%Y%m%d') + '.log'
        logger = get_logger(__name__, log_filename)
        logger.info('start:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

        # コマンドライン引数設定
        parser = util_com.init_argument_parser(height, dt_today)

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
            before_data = util_db.select_by_key(db_file, util_db.select_max_seq(db_file, "health"))
            before = before_data[3]

            # 登録
            util_db.save(db_file, dt_regist, height, weight, util_health.show_bmi(height, weight, target_weight, before))

        elif mode == 'select_all':
            # 全件取得
            datas = util_db.select_all(db_file)
            for data in datas:
                print(data)

        elif mode == 'read_key':
            # キーで検索
            data = util_db.select_by_key(db_file, data_id)
            print(data)

        elif mode == 'del_key':
            # キーで削除
            util_db.delete_by_key(db_file, data_id)

        elif mode == 'upd_key':
            bmi = util_health.calc_bmi(height, weight)
            # キーで更新
            util_db.update_by_key(db_file, data_id, dt_regist, height, weight, bmi)

        elif mode == 'show_bmi':
            # BMIを計算・表示
            util_health.show_bmi(height, weight, target_weight)

        elif mode == 'show_monthly_graph':
            # 年月指定でグラフ表示
            target_year_month = str(target_year_month)
            from_date = datetime.date(int(target_year_month[0:4]), int(target_year_month[4:6]), 1)
            print(from_date)
            to_date = from_date.replace(day=calendar.monthrange(from_date.year, from_date.month)[1])
            print(to_date)
            data = util_db.select_all_for_graph(db_file, str(from_date), str(to_date))            
            print(data)
            disp_year_month = target_year_month[0:4] + '-' + target_year_month[4:6]
            # avg_weight = util_db.select_ave_weight_term(db_file, str(from_date), str(to_date))
            # min_weight = util_db.select_min_weight_term(db_file, str(from_date), str(to_date))
            # max_weight = util_db.select_max_weight_term(db_file, str(from_date), str(to_date))
            # title = disp_year_month + ' / AVG:' + str(avg_weight) + 'kg / MIN:' + str(min_weight) + 'kg / MAX:' + str(max_weight) + 'kg'
            title = disp_year_month + util_db.get_disp_min_max_avg(db_file, str(from_date), str(to_date))
            util_health.disp_graph(data, title)

        elif mode == 'show_term_graph':
            # 期間指定でグラフ表示
            data = util_db.select_all_for_graph(db_file, from_date, to_date)
            print(data)
            # avg_weight = util_db.select_ave_weight_term(db_file, str(from_date), str(to_date))
            # min_weight = util_db.select_min_weight_term(db_file, str(from_date), str(to_date))
            # max_weight = util_db.select_max_weight_term(db_file, str(from_date), str(to_date))
            # title = 'TERM:' + str(from_date) + '~' + str(to_date) + ' / AVG:' + str(avg_weight) + 'kg / MIN:' + str(min_weight) + 'kg / MAX:' + str(max_weight) + 'kg'
            title = 'TERM:' + str(from_date) + '~' + str(to_date) + util_db.get_disp_min_max_avg(db_file, str(from_date), str(to_date))
            util_health.disp_graph(data, title)

        elif mode == 'show_past_month_graph':
            # 直近１ヶ月をグラフ表示
            if to_date == "None":
                dt_to_date = datetime.datetime.today()
                to_date = str(dt_to_date.strftime('%Y-%m-%d'))
            else:
                dt_to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')

            dt_from_date = get_one_month_before(dt_to_date)
            from_date = str(dt_from_date.strftime('%Y-%m-%d'))
            print(from_date)
            print(to_date)

            data = util_db.select_all_for_graph(db_file, str(from_date), str(to_date))            
            print(data)
            # avg_weight = util_db.select_ave_weight_term(db_file, str(from_date), str(to_date))
            # min_weight = util_db.select_min_weight_term(db_file, str(from_date), str(to_date))
            # max_weight = util_db.select_max_weight_term(db_file, str(from_date), str(to_date))
            # title = 'TERM:' + str(from_date) + '~' + str(to_date) + ' / AVG:' + str(avg_weight) + 'kg / MIN:' + str(min_weight) + 'kg / MAX:' + str(max_weight) + 'kg'
            title = 'TERM:' + str(from_date) + '~' + str(to_date) + util_db.get_disp_min_max_avg(db_file, str(from_date), str(to_date))
            util_health.disp_graph(data, title)

        elif mode == 'max_weight':
            # 今までで最大体重だった日のデータを表示
            max_weight = util_db.select_max_weight(db_file)
            print(max_weight)

        elif mode == 'min_weight':
            # 今までで最小体重だった日のデータを表示
            min_weight = util_db.select_min_weight(db_file)
            print(min_weight)

        else:
            print("modeが指定されていませんので、処理を終了します。")

        logger.info('end:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    except Exception as e:
        logger.exception('Exception occered: %s', e)
        print('Exception occered: %s', e)
