#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import datetime, os, pathlib, calendar
import com_db
import com
import datetime

class TestComDb(unittest.TestCase):
    db_file = ''
    def setUp(self):
        # current_dir = pathlib.Path(__file__).resolve().parent
        current_dir = '../'

        # 設定ファイル読み込み
        # settings = util_com.get_settings(current_dir)
        settings = com.get_settings(current_dir)

        # DBファイル準備
        self.db_file = os.path.join(current_dir, settings["db_file"])

        # DB管理クラスインスタンス化
        self.db_util = com_db.DbUtil(self.db_file)

    # def tearDown(self):
    #     # テストの後片付け
    #     print("test finished!!")

    def test_get_to_date_for_search(self):
        self.assertEqual('2020-01-01 23:59', self.db_util.get_to_date_for_search('2020-01-01'))

    def test_select_ave_weight(self):
        self.assertEqual(74.0, self.db_util.select_ave_weight_term('2020-12-09', '2021-01-08'))
        self.assertEqual(75.0, self.db_util.select_ave_weight_term('2020-11-21', '2020-12-20'))

    def test_select_max_weight_term(self):
        self.assertEqual(75.4, self.db_util.select_max_weight_term('2020-12-09', '2021-01-08'))

    def test_select_min_weight_term(self):
        self.assertEqual(72.5, self.db_util.select_min_weight_term('2020-12-09', '2021-01-08'))

    def test_select_min_weight_term(self):
        self.assertEqual(72.5, self.db_util.select_min_weight_term('2020-12-09', '2021-01-08'))
