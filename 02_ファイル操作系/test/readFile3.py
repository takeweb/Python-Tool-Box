# -*- coding: utf-8 -*-
import os
import sys
import codecs

argvs = sys.argv
argcnt = len(argvs)

file = str(argvs[1])

if (argcnt != 2):
    print('Usage: # python %s filename' % argvs[0])
    quit()

f = codecs.open(file, 'r', 'utf-8')
for row in f:
	row = row.rstrip()
	(path, filename) = os.path.split(row)
	print(path + '\t' + filename)

f.close
