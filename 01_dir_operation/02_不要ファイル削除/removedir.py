import sys
import shutil

argvs = sys.argv
argcnt = len(argvs)

path = str(argvs[1])

shutil.rmtree(path)
