import os
import sys
import time

argvs = sys.argv
argcnt = len(argvs)

target = str(argvs[1])

if (argcnt != 2):
    #print 'Usage: # python %s filename' % argvs[0]
    quit()

file_list = []
for dirpath, dirnames, filenames in os.walk(target):
    for f in filenames:
        fullpath = os.path.join(dirpath, f)
        print(fullpath)
        if os.path.isfile(fullpath):
            timestamp = time.localtime(os.path.getmtime(fullpath))
            file_list.append((fullpath, time.strftime('%Y/%m/%d %X',(timestamp))))

for i, path in enumerate(sorted(file_list, key=lambda a: a[1], reverse=True)):
    print(path)

