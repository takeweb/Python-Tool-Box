import os
import sys

argvs = sys.argv
argcnt = len(argvs)

year = int(argvs[1])
base = str(argvs[1])

if (argcnt != 2):
    print('Usage: python %s year(ex.2020)' % argvs[0])
    quit()

for cnt in range(4, 16):
    if cnt > 12:
        month = cnt - 12
        if cnt == 13:
            year += 1
    else:
        month = cnt
    month = str(month).zfill(2)
    os.makedirs( base + "年度" + "/" + str(year) + "年" + str(month) + "月" )

