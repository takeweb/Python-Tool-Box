#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import datetime, os, pathlib, calendar
import com_health
import com
import datetime

class TestComHealth(unittest.TestCase):
    def test_judge_bmi_jp(self):
        self.assertEqual('痩せ型',   com_health.judge_bmi_jp(18.4))
        self.assertEqual('普通体重',  com_health.judge_bmi_jp(18.5))
        self.assertEqual('普通体重',  com_health.judge_bmi_jp(24.99))
        self.assertEqual('肥満(1度)', com_health.judge_bmi_jp(25))
        self.assertEqual('肥満(1度)', com_health.judge_bmi_jp(29.99))
        self.assertEqual('肥満(2度)', com_health.judge_bmi_jp(30))
        self.assertEqual('肥満(2度)', com_health.judge_bmi_jp(34.99))
        self.assertEqual('肥満(3度)', com_health.judge_bmi_jp(35))
        self.assertEqual('肥満(3度)', com_health.judge_bmi_jp(39.99))
        self.assertEqual('肥満(4度)', com_health.judge_bmi_jp(40))

    def test_judge_bmi_who(self):
        self.assertEqual('痩せすぎ',    com_health.judge_bmi_who(15.99))
        self.assertEqual('痩せ',       com_health.judge_bmi_who(16))
        self.assertEqual('痩せ',       com_health.judge_bmi_who(16.99))
        self.assertEqual('痩せぎみ',    com_health.judge_bmi_who(17))
        self.assertEqual('痩せぎみ',    com_health.judge_bmi_who(18.49))
        self.assertEqual('普通体重',    com_health.judge_bmi_who(18.5))
        self.assertEqual('普通体重',    com_health.judge_bmi_who(24.99))
        self.assertEqual('前肥満',      com_health.judge_bmi_who(25))
        self.assertEqual('前肥満',      com_health.judge_bmi_who(29.99))
        self.assertEqual('肥満(1度)',   com_health.judge_bmi_who(30))
        self.assertEqual('肥満(1度)',   com_health.judge_bmi_who(34.99))
        self.assertEqual('肥満(2度)',   com_health.judge_bmi_who(35))
        self.assertEqual('肥満(2度)',   com_health.judge_bmi_who(39.99))
        self.assertEqual('肥満(3度)',   com_health.judge_bmi_who(40))
