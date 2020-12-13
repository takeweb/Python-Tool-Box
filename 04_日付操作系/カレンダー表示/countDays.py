#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar

for year in range(1900, 2030, 1):
    cnt = 0
    for month in range(1, 13):
        cnt += calendar.monthrange(year, month)[1]
    print(str(year) + "年は" + str(cnt) + "日")