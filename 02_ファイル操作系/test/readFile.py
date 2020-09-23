# -*- coding: utf-8 -*-
import os
import sys

argvs = sys.argv
argcnt = len(argvs)

file = str(argvs[1])

if (argcnt != 2):
    print('Usage: # python %s filename' % argvs[0])
    quit()

with open(file, "r", "utf-8") as f:
	for row in f:
		row = row.rstrip()

		revision = ''
		auther = ''
		datetime = ''
		message = ''
		change = ''

		if row in u'リビジョン:':
			revision = row
		elif row in u'作者:':
			auther = row
		elif row in u'日時:':
			datetime = row
		elif row in u'メッセージ:':
			message = row
		elif row in u'変更:':
			change = row

		if revision:
			print(revision)
		if auther:
			print(auther)
		if datetime:
			print(datetime)
		if message:
			print(message)
		if change:
			print(change)

print("Finish!")
