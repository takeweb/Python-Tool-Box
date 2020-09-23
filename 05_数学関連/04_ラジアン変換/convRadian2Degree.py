#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
# ラジアンを度へ変換
if __name__ == '__main__':
    try:
        rad_list = [1/12, 1/6, 1/4, 1/3, 5/12, 1/2, 7/12, 2/3, 5/6, 11/12
                    , 1, 13/12, 7/6, 5/4, 4/3, 17/12, 3/2, 19/12, 5/3
                    , 7/4, 11/6, 23/12, 2]
        for rad in rad_list:
            deg = math.degrees(rad * math.pi)
            print("{0}→{1}°".format(str(round(rad, 4)), str(round(deg))))
            #print(str(rad) + "→" + str(round(deg)))
    except Exception as e:
        print(e)

