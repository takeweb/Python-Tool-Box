import os
import sys
import datetime
import shutil

argvs = sys.argv
argcnt = len(argvs)

target = str(argvs[1])
dst=str(argvs[2])
year = int(argvs[3])
month = int(argvs[4])
day = int(argvs[5])

basename = os.path.basename(target)
#kizyun = datetime.datetime(2016,2,18,0,0)
kizyun = datetime.datetime(year,month,day,0,0)
#dstdir_root = os.path.join(dst, kizyun.strftime('%Y%m%d%H%M%S'))
dstdir_root = os.path.join(dst, kizyun.strftime('%Y%m%d'))
extlist = ['.java', '.jsp', '.css', '.xml', '.html', '.js', '.properties', '.bat','.frm']

if not os.path.exists(dstdir_root):
    os.makedirs(dstdir_root)

if (argcnt != 6):
    #print 'Usage: # python %s filename' % argvs[0]
    quit()

for dirpath, dirnames, filenames in os.walk(target):
    for f in filenames:
        path, ext = os.path.splitext(f)
        if ext in extlist:
            dt = datetime.datetime.fromtimestamp(os.stat(os.path.join(dirpath, f)).st_mtime)
            if kizyun <= dt:
                frmfile = os.path.join(dirpath, f)
                #dstfile = os.path.join(dstdir_root, f)
                strdt = dt.strftime('%Y-%m-%d %H:%M:%S')
                print(os.path.join(dirpath, f) + ' ' + strdt)
                list = dirpath.split('\\')
                index = list.index(basename)
                del list[0:index]
                dstdir = os.path.join(dstdir_root, *list)
#               print('dstdir:' + dstdir)
                dstfile = os.path.join(dstdir_root, *list, f)
#                print('dstfile:' + dstfile)
                if not os.path.exists(dstdir):
                    os.makedirs(dstdir)
                shutil.copy(frmfile, dstfile)
