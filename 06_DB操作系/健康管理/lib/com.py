import argparse, json, os

def get_settings(current_dir):
    # 設定ファイル取得
    conf_file = os.path.join(current_dir, 'settings.json')
    json_file = open(conf_file, 'r')
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def init_argument_parser(height, dt_today):
    # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    # parser.add_argument('-m', '--mode', default='select_all')
    parser.add_argument('-m', '--mode')
    parser.add_argument('-t', '--height', default=height)
    parser.add_argument('-w', '--weight')
    parser.add_argument('-d', '--dt_regist', default=dt_today)
    parser.add_argument('-from', '--from_date')
    parser.add_argument('-to', '--to_date')
    parser.add_argument('-i', '--data_id')
    parser.add_argument('-tym', '--target_year_month')
    return parser
