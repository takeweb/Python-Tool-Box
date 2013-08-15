import os
import sys
import datetime

argvs = sys.argv
argcnt = len(argvs)

day = datetime.date(2013,8,23)

for cnt in range(1, 6):
    name = str(day)
    os.makedirs(name)
    day = day + datetime.timedelta(days=7)

