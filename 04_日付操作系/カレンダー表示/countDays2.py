#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime
import sys

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

    for month in range(1, 13):
        total_cnt += calendar.monthrange(now_year, month)[1]
        if now_month > month:
            cnt += calendar.monthrange(now_year, month)[1]
        elif now_month == month:
            cnt += now_day

    #print("今日は" + str(now_year) + "年" + str(now_month) + "月" + str(now_day) + "日(" + w_list[dt_now.weekday()] + ") "
    #        + str(now_hour) + ":" + str(now_minute) + ":" + str(now_second) + " "
    #        + str(cnt) + "/" +  str(total_cnt) + "日 あと" + str(total_cnt - cnt) + "日")
    #print("今日は" + dt_now.strftime('%Y年%m月%d日(' + w_list[dt_now.weekday()] + ')%H:%M:%S')
    #        + " " + str(cnt) + "/" +  str(total_cnt) + "日 あと" + str(total_cnt - cnt) + "日")
    print("今日は{0} {1}/{2}日 あと{3}日".format(dt_now.strftime('%Y年%m月%d日(' + w_list[dt_now.weekday()] + ')%H:%M:%S')
                                                , str(cnt), str(total_cnt), str(total_cnt - cnt)))

    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal.prmonth(now_year, now_month)