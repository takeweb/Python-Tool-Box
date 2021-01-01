import argparse, json, os

def get_settings(current_dir):
    # 設定ファイル取得
    conf_file = os.path.join(current_dir, 'settings.json')
    json_file = open(conf_file, 'r')
    json_data = json.load(json_file)
    return json_data

def init_argument_parser():
    # コマンドライン引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='select_all')
    parser.add_argument('-c', '--ccode')
    parser.add_argument('-i', '--data_id')
    parser.add_argument('-ib', '--isbn')
    parser.add_argument('-n', '--name')
    parser.add_argument('-a', '--author')
    parser.add_argument('-t', '--translator')
    parser.add_argument('-p', '--publisher')
    parser.add_argument('-sa', '--selling_agency')
    parser.add_argument('-o', '--original_price')
    parser.add_argument('-b', '--bid_price')
    parser.add_argument('-s', '--selling_price')
    parser.add_argument('-w', '--owned_flg')
    parser.add_argument('-r', '--remarks')
    parser.add_argument('-tg', '--tag')
    return parser
