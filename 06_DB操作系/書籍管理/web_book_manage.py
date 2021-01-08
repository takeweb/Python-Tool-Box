#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_table import Table, Col, LinkCol
import datetime, os, pathlib
from util.dateUtil import conv_str_datetime
from util.dateUtil import get_one_month_before
from util.loggingUtil import get_logger
from lib import util_com
from lib import util_db
from lib import util_book

app = Flask(__name__)
book = None

@app.route('/', methods=['GET'])
def get_index():
    return get_list()

@app.route('/list', methods=['GET'])
def get_list():
    """
    一覧表示
    """
    util_db.Book.db_init(db_file)
    list = util_db.Book.select_all(db_file)
    return render_template('web_book_list.html', list=list)

@app.route('/search', methods=['POST'])
def search():
    """
    キーワード検索
    """
    list = util_db.Book.select_by_keyword(db_file, request.form['seach_keyword'])
    return render_template('web_book_list.html', list=list, seach_keyword=request.form['seach_keyword'])

@app.route('/detail/<int:id>', methods=['GET'])
def get_detail(id):
    """
    詳細表示
    """
    book = util_db.Book(db_file, 'view', id)
    return render_template('web_book_detail.html', book=book)

@app.route('/new', methods=['GET'])
def new():
    """
    新規登録画面へ遷移
    """
    return render_template('web_book_new.html', book=book)

@app.route('/save', methods=['POST'])
def save():
    """
    新規登録
    """
    if request.method == 'POST':
        book = new_book(request, 'new')
        # 登録
        book.save()
        return render_template('web_book_new.html', book=book)

def new_book(request, mode):
    """
    Bookクラスをrequestの内容で初期化して返却
    """
    data_id        = request.form['data_id']        if 'data_id'        in request.form else 0
    isbn           = request.form['isbn']           if 'isbn'           in request.form else ''
    name           = request.form['name']           if 'name'           in request.form else ''
    author         = request.form['author']         if 'author'         in request.form else ''
    translator     = request.form['translator']     if 'translator'     in request.form else ''
    publisher      = request.form['publisher']      if 'publisher'      in request.form else ''
    selling_agency = request.form['selling_agency'] if 'selling_agency' in request.form else 0
    original_price = request.form['original_price'] if 'original_price' in request.form else 0
    bid_price      = request.form['bid_price']      if 'bid_price'      in request.form else 0
    selling_price  = request.form['selling_price']  if 'selling_price'  in request.form else 0
    owned_flg      = request.form['owned_flg']      if 'owned_flg'      in request.form else 1
    remarks        = request.form['remarks']        if 'remarks'        in request.form else ''
    tag            = request.form['tag']            if 'tag'            in request.form else ''

    book = util_db.Book(db_file, mode, data_id, isbn, name, author, translator
                        , publisher, selling_agency, original_price, bid_price, selling_price
                        , owned_flg, remarks, tag)
    return book

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    """
    編集表示
    """
    book = util_db.Book(db_file, 'view', id)
    return render_template('web_book_edit.html', book=book)

@app.route('/update', methods=['POST'])
def update():
    """
    更新
    """
    if request.method == 'POST':
        book = new_book(request, 'update')
        # 更新
        book.update_by_key()
        return render_template('web_book_detail.html', book=book, done_flg=1)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    """
    削除
    """
    book.delete_by_key(id)
    return get_list()

if __name__ == '__main__':
    dt_today = datetime.datetime.today()
    current_dir = pathlib.Path(__file__).resolve().parent

    # 設定ファイル読み込み
    settings = util_com.get_settings(current_dir)

    # DBファイル準備
    db_file = os.path.join(current_dir, settings["db_file"])

    # ロガー準備
    log_filename = settings["log_filename"] + '_' + dt_today.strftime('%Y%m%d') + '.log'
    logger = get_logger(__name__, log_filename)
    logger.info('start:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    app.run(port=5001, debug=True)