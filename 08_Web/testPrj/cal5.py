#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/calender/<year>/<month>/')
def calender(year, month):
        if year.isdigit() and month.isdigit():
            return render_template('calender.html', calender=showCalender(int(year), int(month)), year=year, month=month)
        else:
            print('Argument is not digit')

def showCalender(year, month):
    cal = calendar.LocaleHTMLCalendar(calendar.SUNDAY, locale='ja_jp')
    cal.cssclasses = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat blue', 'sun red']
    html = cal.formatmonth(year, month, False)
    print(html)
    return html

if __name__ == '__main__':
    app.run()