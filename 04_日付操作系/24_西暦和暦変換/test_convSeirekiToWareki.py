#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import convSeirekiToWareki
import datetime

class TestConvSeirekiToWareki(unittest.TestCase):
    def test_convSeirekiToWareki(self):
        self.assertEqual("明治元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1868, 10, 23)))
        self.assertEqual("明治元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1868, 10, 24)))
        self.assertEqual("明治45年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1912, 7, 28)))
        self.assertEqual("明治45年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1912, 7, 29)))
        self.assertEqual("大正元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1912, 7, 30)))
        self.assertEqual("大正15年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1926, 12, 24)))
        self.assertEqual("昭和元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1926, 12, 25)))
        self.assertEqual("昭和64年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1989, 1, 7)))
        self.assertEqual("平成元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(1989, 1, 8)))
        self.assertEqual("平成31年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(2019, 4, 30)))
        self.assertEqual("令和元年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(2019, 5, 1)))
        self.assertEqual("令和2年", convSeirekiToWareki.convSeirekiToWareki(datetime.date(2020, 9, 8)))