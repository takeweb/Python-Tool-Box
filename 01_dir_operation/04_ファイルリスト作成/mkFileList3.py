import os
import sys
import datetime
import shutil

argvs = sys.argv
argcnt = len(argvs)

target = str(argvs[1])
kizyun = datetime.datetime(2015,12,17,7,48,0)
dstdir_root = os.path.join("D:\ooishi\97_ソースマージ\履歴",kizyun.strftime('%Y%m%d%H%M%S'))
os.makedirs(dstdir_root)

if (argcnt != 2):
    #print 'Usage: # python %s filename' % argvs[0]
    quit()

for dirpath, dirnames, filenames in os.walk(target):
    for f in filenames:
        path, ext = os.path.splitext(f)
        if ext == '.class' or ext == '.xml':
            print(f)
            dt = datetime.datetime.fromtimestamp(os.stat(os.path.join(dirpath, f)).st_mtime)
            if kizyun <= dt:
                frmfile = os.path.join(dirpath, f)
                dstfile = os.path.join(dstdir_root, f)
                strdt = dt.strftime('%Y-%m-%d %H:%M:%S')
                print(os.path.join(dirpath, f) + ' ' + strdt)

                shutil.copy(frmfile, dstfile)
