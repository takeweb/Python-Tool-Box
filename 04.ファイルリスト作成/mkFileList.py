import os

for dirpath, dirnames, filenames in os.walk('D:/ooishi/tmp'):
    for f in filenames:
        print(os.path.join(dirpath, f))
