import os

year = 2013
base = "2013年度"
for cnt in range(4, 16):
    if cnt > 12:
        month = cnt - 12
        if cnt == 13:
            year += 1
    else:
        month = cnt
    month = str(month).zfill(2)
    os.makedirs( base + "/" + str(year) + "年" + str(month) + "月" )
