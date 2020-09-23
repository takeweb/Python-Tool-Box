#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime
import jpholiday
import sys
sys.path.append('/Users/oishi/develop/python3/Python-Tool-Box/99_common/util')
import dateUtil

dt_now = datetime.datetime.now()
now_year = dt_now.year
now_month = dt_now.month
now_day = dt_now.day
now_hour = dt_now.hour
now_minute = dt_now.minute
now_second = dt_now.second
w_list = ['月', '火', '水', '木', '金', '土', '日']
total_cnt = 0
cnt = 0

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 1:
        print("使い方：" + sys.argv[0])
        sys.exit();

    cnt_biz = 0
    cnt_dn = 0
    cnt_hol = 0
    for month in range(1, 13):
        max = calendar.monthrange(now_year, month)[1]
        for day in range(1, max + 1):
            target_date = datetime.date(now_year, month, day)
            if dateUtil.isBizDay(target_date):
                cnt_biz += 1
            if target_date.weekday() in (5, 6) and jpholiday.is_holiday(target_date) == False:
                cnt_dn += 1
            if jpholiday.is_holiday(target_date):
                cnt_hol += 1
    print("営業日合計" + str(cnt_biz))
    print("祝日合計" + str(cnt_hol))
    print("土日合計" + str(cnt_dn))

    #print("今日は" + dt_now.strftime('%Y年%m月%d日(' + w_list[dt_now.weekday()] + ')%H:%M:%S')
    #        + " " + str(cnt) + "/" +  str(total_cnt) + "日 あと" + str(total_cnt - cnt) + "日")

    #cal = calendar.TextCalendar(calendar.SUNDAY)
    #cal.prmonth(now_year, now_month)