#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import decUtil
import datetime

class TestConvertDecToAny(unittest.TestCase):
    def test_convert_dec_to_any(self):
        self.assertEqual('1100100', decUtil.convert_dec_to_any(100, 2))
        self.assertEqual('144', decUtil.convert_dec_to_any(100, 8))
        self.assertEqual('64', decUtil.convert_dec_to_any(100, 16))
        self.assertEqual('1A', decUtil.convert_dec_to_any(26, 16))

    def test_convert_any_to_dec(self):
        self.assertEqual(100, decUtil.convert_any_to_dec(1100100, 2))
        self.assertEqual(100, decUtil.convert_any_to_dec(144, 8))
        self.assertEqual(100, decUtil.convert_any_to_dec(64, 16))
        self.assertEqual(26, decUtil.convert_any_to_dec('1A', 16))
