import os
import sys
import datetime

def mkYearDir(year, month, day):
    day = datetime.date(year, month, day)

    #for cnt in range(1, 6):
    for cnt in range(5):
        name = str(day)
        os.makedirs(name)
        day = day + datetime.timedelta(days=7)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        if args[1].isdigit() and args[2].isdigit() and args[3].isdigit():
            mkYearDir(int(args[1]), int(args[2]), int(args[3]))
        else:
            print('Argument is not digit')
    else:
        print(f'Usage: python {args[0]} year(ex.2020) month(ex.5) day(ex.4)')
