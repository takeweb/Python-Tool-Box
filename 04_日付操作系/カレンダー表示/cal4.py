#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import sys

def showCalender(year, month):
    cal = calendar.LocaleTextCalendar(calendar.SUNDAY, locale='ja_jp')
    cal.prmonth(year, month, w=7, l=2)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        if args[1].isdigit() and args[2].isdigit():
            showCalender(int(args[1]), int(args[2]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')