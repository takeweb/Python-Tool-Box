#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, os, pathlib, calendar
from util.dateUtil import conv_str_datetime
from util.dateUtil import get_one_month_before
from util.loggingUtil import get_logger
from lib import com
from lib import com_db
from lib import com_health

db_util = None
health = None

if __name__ == '__main__':
    try:
        dt_today = datetime.datetime.today()
        current_dir = pathlib.Path(__file__).resolve().parent

        # 設定ファイル読み込み
        settings = com.get_settings(current_dir)
        height = float(settings["height"])
        target_weight = float(settings["target_weight"])
        png_file_name = settings["png_file_name"]

        # DBファイル準備
        db_file = os.path.join(current_dir, settings["db_file"])

        # DB管理クラスインスタンス化
        db_util = com_db.DbUtil(db_file)

        # ロガー準備
        log_filename = settings["log_filename"] + '_' + dt_today.strftime('%Y%m%d') + '.log'
        logger = get_logger(__name__, log_filename)
        logger.info('start:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

        # コマンドライン引数設定
        parser = com.init_argument_parser(height, dt_today)

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
            before_data = db_util.select_by_key(db_util.select_max_id())
            before = before_data.weight

            # BMIを計算
            bmi = com_health.calc_bmi(float(height), float(weight))

            # 登録
            # db_util.save(dt_regist, height, weight, com_health.show_bmi(height, weight, target_weight, before))
            db_util.save(com_db.Health(data_id, dt_regist, height, weight, bmi))

            # 結果を取得
            result_list = com_health.get_result_list(health.height, health.weight, target_weight, before)
            for result in result_list:
                print(result_list)

        elif mode == 'select_all':
            # 全件取得
            datas = db_util.select_all()
            for data in datas:
                print(data)

        elif mode == 'read_key':
            # キーで検索
            data = db_util.select_by_key(data_id)
            print(data)

        elif mode == 'del_key':
            # キーで削除
            db_util.delete_by_key(data_id)

        elif mode == 'upd_key':
            bmi = com_health.calc_bmi(height, weight)
            # キーで更新
            # db_util.update_by_key(data_id, dt_regist, height, weight, bmi)
            db_util.update(com_db.Health(data_id, dt_regist, height, weight, bmi))

        elif mode == 'show_bmi':
            # BMIを計算・表示
            # com_health.show_bmi(height, weight, target_weight)
            result_list = com_health.get_result_list(height, weight, target_weight)
            for result in result_list:
                print(result)

        elif mode == 'show_monthly_graph':
            # 年月指定でグラフ表示
            target_year_month = str(target_year_month)
            from_date = datetime.date(int(target_year_month[0:4]), int(target_year_month[4:6]), 1)
            print(from_date)
            to_date = from_date.replace(day=calendar.monthrange(from_date.year, from_date.month)[1])
            print(to_date)
            data = db_util.select_for_graph(str(from_date), str(to_date))            
            print(data)
            disp_year_month = target_year_month[0:4] + '-' + target_year_month[4:6]
            title = disp_year_month + '\n' + db_util.get_disp_min_max_avg( str(from_date), str(to_date))
            com_health.disp_graph(data, title)

        elif mode == 'show_term_graph':
            # 期間指定でグラフ表示
            data = db_util.select_for_graph(from_date, to_date)
            print(data)
            title = str(from_date) + '~' + str(to_date) + '\n' + db_util.get_disp_min_max_avg(str(from_date), str(to_date))
            com_health.disp_graph(data, title)

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

            data = db_util.select_for_graph(str(from_date), str(to_date))            
            print(data)
            title = str(from_date) + '~' + str(to_date) + '\n' + db_util.get_disp_min_max_avg(str(from_date), str(to_date))
            com_health.disp_graph(data, title)
            com_health.save_graph(data, title, png_file_name)

        elif mode == 'max_weight':
            # 今までで最大体重だった日のデータを表示
            max_weight = db_util.select_max_weight()
            print(max_weight)

        elif mode == 'min_weight':
            # 今までで最小体重だった日のデータを表示
            min_weight = db_util.select_min_weight()
            print(min_weight)

        else:
            print("modeが指定されていませんので、処理を終了します。")

        logger.info('end:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    except Exception as e:
        logger.exception('Exception occered: %s', e)
        print('Exception occered: %s', e)
