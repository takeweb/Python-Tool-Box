#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import datetime, sys
import util.dateUtil as dateUtil

class TestDateUtil(unittest.TestCase):
    def test_convSeirekiToWareki(self):
        # 曜日無・デフォルト引数
        self.assertEqual("明治元年10月23日", dateUtil.convSeirekiToWareki("18681023"))
        self.assertEqual("明治45年7月29日", dateUtil.convSeirekiToWareki("19120729"))
        self.assertEqual("大正元年7月30日", dateUtil.convSeirekiToWareki("19120730"))
        self.assertEqual("大正15年12月24日", dateUtil.convSeirekiToWareki("19261224"))
        self.assertEqual("昭和元年12月25日", dateUtil.convSeirekiToWareki("19261225"))
        self.assertEqual("昭和64年1月7日", dateUtil.convSeirekiToWareki("19890107"))
        self.assertEqual("平成元年1月8日", dateUtil.convSeirekiToWareki("19890108"))
        self.assertEqual("平成31年4月30日", dateUtil.convSeirekiToWareki("20190430"))
        self.assertEqual("令和元年5月1日", dateUtil.convSeirekiToWareki("20190501"))
        self.assertEqual("令和2年9月8日", dateUtil.convSeirekiToWareki("20200908"))
        # 曜日無・引数でfalse指定
        self.assertEqual("明治元年10月23日", dateUtil.convSeirekiToWareki("18681023", False))
        self.assertEqual("明治45年7月29日", dateUtil.convSeirekiToWareki("19120729", False))
        self.assertEqual("大正元年7月30日", dateUtil.convSeirekiToWareki("19120730", False))
        self.assertEqual("大正15年12月24日", dateUtil.convSeirekiToWareki("19261224", False))
        self.assertEqual("昭和元年12月25日", dateUtil.convSeirekiToWareki("19261225", False))
        self.assertEqual("昭和64年1月7日", dateUtil.convSeirekiToWareki("19890107", False))
        self.assertEqual("平成元年1月8日", dateUtil.convSeirekiToWareki("19890108", False))
        self.assertEqual("平成31年4月30日", dateUtil.convSeirekiToWareki("20190430", False))
        self.assertEqual("令和元年5月1日", dateUtil.convSeirekiToWareki("20190501", False))
        self.assertEqual("令和2年9月8日", dateUtil.convSeirekiToWareki("20200908", False))
        # 曜日付き・引数でtrue指定
        self.assertEqual("明治元年10月23日(金)", dateUtil.convSeirekiToWareki("18681023", True))
        self.assertEqual("明治45年7月29日(月)", dateUtil.convSeirekiToWareki("19120729", True))
        self.assertEqual("大正元年7月30日(火)", dateUtil.convSeirekiToWareki("19120730", True))
        self.assertEqual("大正15年12月24日(金)", dateUtil.convSeirekiToWareki("19261224", True))
        self.assertEqual("昭和元年12月25日(土)", dateUtil.convSeirekiToWareki("19261225", True))
        self.assertEqual("昭和64年1月7日(土)", dateUtil.convSeirekiToWareki("19890107", True))
        self.assertEqual("平成元年1月8日(日)", dateUtil.convSeirekiToWareki("19890108", True))
        self.assertEqual("平成31年4月30日(火)", dateUtil.convSeirekiToWareki("20190430", True))
        self.assertEqual("令和元年5月1日(水)", dateUtil.convSeirekiToWareki("20190501", True))
        self.assertEqual("令和2年9月8日(火)", dateUtil.convSeirekiToWareki("20200908", True))

    def test_convWarekiToSeireki(self):
        self.assertEqual("18681223", dateUtil.convWarekiToSeireki("明治元年12月23日"))
        self.assertEqual("19120729", dateUtil.convWarekiToSeireki("明治45年7月29日"))
        self.assertEqual("19120730", dateUtil.convWarekiToSeireki("大正元年7月30日"))
        self.assertEqual("19261224", dateUtil.convWarekiToSeireki("大正15年12月24日"))
        self.assertEqual("19261225", dateUtil.convWarekiToSeireki("昭和元年12月25日"))
        self.assertEqual("19890107", dateUtil.convWarekiToSeireki("昭和64年1月7日"))
        self.assertEqual("19890108", dateUtil.convWarekiToSeireki("平成元年1月8日"))
        self.assertEqual("20190430", dateUtil.convWarekiToSeireki("平成31年4月30日"))
        self.assertEqual("20190501", dateUtil.convWarekiToSeireki("令和元年5月1日"))
        self.assertEqual("20200908", dateUtil.convWarekiToSeireki("令和2年9月8日"))

    def test_isBizDay(self):
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 1, 1)))
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 1, 2)))
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 1, 3)))
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 1, 4)))
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 1, 5)))
        self.assertEqual(True,  dateUtil.isBizDay(datetime.date(2020, 1, 6)))
        self.assertEqual(False, dateUtil.isBizDay(datetime.date(2020, 12, 31)))

    def test_conv_str_datetime(self):
        dt_now = datetime.datetime.today()
        self.assertEqual(dt_now, dateUtil.conv_str_datetime(dt_now))
        self.assertEqual(datetime.datetime(2020, 1, 30), dateUtil.conv_str_datetime("2020-01-30"))
        self.assertEqual(datetime.datetime(2020, 1, 30), dateUtil.conv_str_datetime("2020/01/30"))
        self.assertEqual(datetime.datetime(2020, 7, 31), dateUtil.conv_str_datetime("2020年07月31日"))
        self.assertEqual(datetime.datetime(2020, 1, 30, 12, 30), dateUtil.conv_str_datetime("2020-01-30 12:30"))
        self.assertEqual(datetime.datetime(2020, 1, 30, 12, 30), dateUtil.conv_str_datetime("2020/01/30 12:30"))
        self.assertEqual(datetime.datetime(2020, 7, 31, 12, 30), dateUtil.conv_str_datetime("2020年07月31日 12:30"))
        self.assertEqual(datetime.datetime(2020, 1, 30, 12, 30, 20), dateUtil.conv_str_datetime("2020/01/30 12:30:20"))
        self.assertEqual(datetime.datetime(2020, 1, 30, 12, 30, 20), dateUtil.conv_str_datetime("2020-01-30 12:30:20"))
        self.assertEqual(datetime.datetime(2020, 7, 31, 12, 30, 20), dateUtil.conv_str_datetime("2020年07月31日 12:30:20"))

    def test_get_one_month_before(self):
        # 前の月が閏年(29日まで)の場合
        self.assertEqual(datetime.date(2020,  2, 27), dateUtil.get_one_month_before(datetime.date(2020,  3, 26)))
        self.assertEqual(datetime.date(2020,  2, 28), dateUtil.get_one_month_before(datetime.date(2020,  3, 27)))
        self.assertEqual(datetime.date(2020,  2, 29), dateUtil.get_one_month_before(datetime.date(2020,  3, 28)))
        self.assertEqual(datetime.date(2020,  3,  1), dateUtil.get_one_month_before(datetime.date(2020,  3, 29)))
        self.assertEqual(datetime.date(2020,  3,  1), dateUtil.get_one_month_before(datetime.date(2020,  3, 30)))
        # 前の月が28日までの場合
        self.assertEqual(datetime.date(2019,  2, 27), dateUtil.get_one_month_before(datetime.date(2019,  3, 26)))
        self.assertEqual(datetime.date(2019,  2, 28), dateUtil.get_one_month_before(datetime.date(2019,  3, 27)))
        self.assertEqual(datetime.date(2019,  3,  1), dateUtil.get_one_month_before(datetime.date(2019,  3, 28)))
        self.assertEqual(datetime.date(2019,  3,  1), dateUtil.get_one_month_before(datetime.date(2019,  3, 29)))
        self.assertEqual(datetime.date(2019,  3,  1), dateUtil.get_one_month_before(datetime.date(2019,  3, 30)))
        # 前の月が31日までの場合
        self.assertEqual(datetime.date(2020,  3,  1), dateUtil.get_one_month_before(datetime.date(2020,  3, 31)))
        self.assertEqual(datetime.date(2020, 10, 30), dateUtil.get_one_month_before(datetime.date(2020, 11, 29)))
        self.assertEqual(datetime.date(2020, 10, 31), dateUtil.get_one_month_before(datetime.date(2020, 11, 30)))
        self.assertEqual(datetime.date(2020, 12,  1), dateUtil.get_one_month_before(datetime.date(2020, 12, 31)))
        self.assertEqual(datetime.date(2020, 12,  2), dateUtil.get_one_month_before(datetime.date(2021,  1,  1)))
        # # 前の月が30日までの場合
        self.assertEqual(datetime.date(2020, 11,  2), dateUtil.get_one_month_before(datetime.date(2020, 12,  1)))
        self.assertEqual(datetime.date(2020, 11, 30), dateUtil.get_one_month_before(datetime.date(2020, 12, 29)))
        self.assertEqual(datetime.date(2020, 12,  1), dateUtil.get_one_month_before(datetime.date(2020, 12, 30)))