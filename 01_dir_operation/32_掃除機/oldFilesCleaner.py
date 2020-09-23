import os
import sys
import datetime
import shutil

argvs = sys.argv
argcnt = len(argvs)

target = str(argvs[1])
kizyun = datetime.datetime(2016,1,6,0,0)
#extlist = ['.java', '.jsp', '.css', '.xml', '.html', '.js', '.properties', '.bat']

if (argcnt != 2):
    #print 'Usage: # python %s filename' % argvs[0]
    quit()

for dirpath, dirnames, filenames in os.walk(target):
    for dir in dirnames:
        print(dir)
        dt = datetime.datetime.fromtimestamp(os.stat(dir).st_mtime)
        if kizyun > dt:
            strdt = dt.strftime('%Y-%m-%d %H:%M:%S')
            print('ディレクトリ：' + dir + ' ' + strdt)

    for f in filenames:
        dt = datetime.datetime.fromtimestamp(os.stat(os.path.join(dirpath, f)).st_mtime)
        if kizyun > dt:
            targetfile = os.path.join(dirpath, f)
            #dstfile = os.path.join(dstdir_root, f)
            strdt = dt.strftime('%Y-%m-%d %H:%M:%S')
            print('ファイル：' + os.path.join(dirpath, f) + ' ' + strdt)

