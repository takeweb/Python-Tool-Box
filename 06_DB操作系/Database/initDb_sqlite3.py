#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('./enterprise.db')
curs = conn.cursor()
curs.execute('CREATE TABLE zoo(critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)')
curs.execute('INSERT INTO zoo VALUES("duck2", 5, 0)')
ins = ('INSERT INTO zoo VALUES(?, ?, ?)')
curs.execute(ins, ('bear', 1, 1000))
curs.execute(ins, ('weasel', 1, 2000))
conn.commit()

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()