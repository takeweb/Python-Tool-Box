#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, make_response, send_file
from flask_table import Table, Col, LinkCol
import datetime, os, pathlib
from util.dateUtil import conv_str_datetime
from util.dateUtil import get_one_month_before
from util.loggingUtil import get_logger
from lib import com
from lib import com_db
from lib import com_health

app = Flask(__name__)
db_util = None
health = None
height = 0.0
target_weight = 0

@app.route('/', methods=['GET'])
def get_index():
    return get_list()

@app.route('/list', methods=['GET'])
def get_list():
    """
    一覧表示
    """
    list = db_util.select_all()
    return render_template('web_health_list.html', list=list)

@app.route('/detail/<int:id>', methods=['GET'])
def get_detail(id):
    """
    詳細表示
    """
    health = db_util.select_by_key(id)
    return render_template('web_health_detail.html', health=health)

@app.route('/new', methods=['GET'])
def new():
    """
    新規登録画面へ遷移
    """
    return render_template('web_health_new.html', health=health, height=height)

@app.route('/save', methods=['POST'])
def save():
    """
    新規登録
    """
    if request.method == 'POST':
        # 前回最新データ取得
        before_data = db_util.select_by_key(db_util.select_max_id())
        before = before_data.weight

        # 登録
        health = new_health(request)
        db_util.save(health)
        new_data = db_util.select_by_key(db_util.select_max_seq("health"))
        health = db_util.select_by_key(new_data.data_id)

        # 結果を取得
        result_list = com_health.get_result_list(health.height, health.weight, target_weight, before)

        return render_template('web_health_new.html', health=health, result_list=result_list)

def new_health(request):
    data_id = 0
    dt_regist = datetime.datetime.today()
    weight = request.form['weight'] if 'weight' in request.form else 0.0

    # BMIを計算
    bmi = com_health.calc_bmi(float(height), float(weight))

    # インスタンス生成
    return com_db.Health(data_id, dt_regist, height, weight, bmi)

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    """
    編集表示
    """
    health = db_util.select_by_key(id)
    return render_template('web_health_edit.html', health=health)

@app.route('/update', methods=['POST'])
def update():
    """
    更新
    """
    if request.method == 'POST':
        # 更新
        data_id = request.form['data_id']
        dt_regist = request.form['regist_datetime']
        height = request.form['height']
        weight = request.form['weight']
        # BMIを再度計算
        bmi = com_health.calc_bmi(float(height), float(weight))

        health = com_db.Health(data_id, dt_regist, height, weight, bmi)
        db_util.update(health)
        health = db_util.select_by_key(data_id)
        return render_template('web_health_detail.html', health=health, done_flg=1)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    """
    削除
    """
    db_util.delete_by_key(id)
    return get_list()

@app.route('/graph', methods=['GET'])
def graph():
    """
    グラフ画面へ遷移
    """
    dt_to_date = datetime.datetime.today()
    to_date = str(dt_to_date.strftime('%Y-%m-%d'))

    dt_from_date = get_one_month_before(dt_to_date)
    from_date = str(dt_from_date.strftime('%Y-%m-%d'))

    return render_template('web_health_graph.html', from_date=from_date, to_date=to_date)

@app.route('/search_graph', methods=['POST'])
def search_graph():
    """
    指定期間でグラフ検索
    """
    from_date = request.form['from_date']
    to_date = request.form['to_date']
    data = db_util.select_for_graph(from_date, to_date)
    print(data)
    title = str(from_date) + '~' + str(to_date) + '\n' + db_util.get_disp_min_max_avg(str(from_date), str(to_date))
    graph_date = com_health.save_graph(data, title, png_file_name)
    return render_template('web_health_graph.html', graph_date=graph_date, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
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

    app.run(port=5002, debug=True)
