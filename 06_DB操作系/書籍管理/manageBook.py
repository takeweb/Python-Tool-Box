#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, os, pathlib
from util.dateUtil import conv_str_datetime
from util.dateUtil import get_one_month_before
from util.loggingUtil import get_logger
from lib import util_com
from lib import util_db
from lib import util_book

if __name__ == '__main__':
    book = None
    try:
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

        # コマンドライン引数設定
        parser = util_com.init_argument_parser()

        # コマンドライン引数受け取り
        args = parser.parse_args()
        mode = str(args.mode)
        isbn = str(args.isbn)
        ccode = str(args.ccode)
        data_id = 0 if args.data_id is None else int(args.data_id)
        isbn = '' if args.isbn is None else str(args.isbn)
        name = '' if args.name is None else str(args.name)
        author = '' if args.author is None else str(args.author)
        translator = '' if args.translator is None else str(args.translator)
        publisher = '' if args.publisher is None else str(args.publisher)
        selling_agency = '' if args.selling_agency is None else str(args.selling_agency)
        original_price = 0 if args.original_price is None else int(args.original_price)
        bid_price = 0 if args.bid_price is None else int(args.bid_price)
        selling_price = 0 if args.selling_price is None else int(args.selling_price)
        owned_flg = 1 if args.owned_flg is None else int(args.owned_flg)
        remarks = '' if args.remarks is None else str(args.remarks)
        tag = '' if args.tag is None else str(args.tag)
        book = util_db.Book(db_file, data_id, isbn, name, author, translator, publisher, selling_agency
                            , original_price, bid_price, selling_price, owned_flg, remarks, tag)
        #print(book)

        # モード切り替え
        if mode == 'save':
            # 登録
            book.save()
        elif mode == 'select_all':
            # 全件取得
            datas = book.select_all()
            for data in datas:
                print(data)
        elif mode == 'read_key':
            # キーで検索
            data = book.select_by_key(data_id)
            print(data)
        elif mode == 'del_key':
            # キーで削除
            book.delete_by_key(data_id)
        elif mode == 'upd_key':
            # キーで更新
            book.update_by_key(data_id)
        elif mode == "13":
            print(util_book.calcCheckDegit13(isbn))
        elif mode == "10":
            print(util_book.calcCheckDegit10(isbn))
        else:
            print(util_book.decipherCcode(ccode))

        logger.info('end:' + dt_today.strftime('%Y/%m/%d %H:%M:%S'))

    except Exception as e:
        print(e)
    finally:
        book.db_close()
