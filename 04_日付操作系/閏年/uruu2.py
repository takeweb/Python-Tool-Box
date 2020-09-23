#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar

# 閏年の定義
# 2月が29日まである年
# 西暦年が4で割り切れる場合。だたし100で割り切れる年は除外
# または西暦年が400で割り切れる場合。
print("閏年は1年が366日です。1900年から2029年までの閏年は下記の通り")
for year in range(1900, 2030, 1):
    if calendar.isleap(year):
        print(str(year) + "年")
