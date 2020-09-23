#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 閏年の定義
# 2月が29日まである年
# 西暦年が4で割り切れる場合。だたし100で割り切れる年は除外
# または西暦年が400で割り切れる場合。
for year in range(1900, 2030, 1):
    if ((year % 4 == 0) and year % 100) or (year % 400 == 0):
        print(str(year) + "年は閏年、1年は366日です。")
