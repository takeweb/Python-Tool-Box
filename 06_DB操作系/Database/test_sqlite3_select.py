#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)