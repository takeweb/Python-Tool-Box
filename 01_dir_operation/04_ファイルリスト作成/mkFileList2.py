import os
import sys

argvs = sys.argv
argcnt = len(argvs)

target = str(argvs[1])

if (argcnt != 2):
    #print 'Usage: # python %s filename' % argvs[0]
    quit()

for dirpath, dirnames, filenames in os.walk(target):
    for filename in filenames:
        path, ext = os.path.splitext(filename)
        if ext == '.java' or ext == '.jsp' or ext == '.css' or ext == '.xml' or ext == '.properties' or ext == '.py':
            print(dirpath + ',' + filename)
