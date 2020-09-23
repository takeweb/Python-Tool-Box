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
        print(os.path.join(dirpath, filename))

