# -*- coding: utf-8 -*-
import os
import sys
import codecs

argvs = sys.argv
argcnt = len(argvs)

file = str(argvs[1])
cnt  = 0
result = ''

if (argcnt != 2):
    print('Usage: # python %s filename' % argvs[0])
    quit()

f = codecs.open(file, 'r', 'utf-8')
for row in f:
	row = row.rstrip()

	revision = ''
	auther = ''
	datetime = ''
	message = ''
	change = ''

	if u'リビジョン:' in row:
		revision = row
		if cnt > 0:
			print(result)
			cnt = 0
			result = ''
		else:
			result += row
	elif u'作者:' in row:
		auther = row
		result += row
	elif u'日時:' in row:
		datetime = row
		result += row
	elif u'メッセージ:' in row:
		message = row
		result += row
	elif u'変更 :' in row:
		change = row
		result += row
		cnt += 1

"""
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
		print(cnt)
"""
print("Finish!")

f.close
