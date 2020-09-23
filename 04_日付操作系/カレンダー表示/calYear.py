#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import sys

def showCalender(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal.pryear(year)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        if args[1].isdigit():
            showCalender(int(args[1]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')