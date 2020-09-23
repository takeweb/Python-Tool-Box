#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

for degree in range(0, 361 ,15):
    #print(degree)
    # 度をラジアンへ変換
    rad = math.radians(degree)
    result = "{:3d}度⇨{}ラジアン".format(degree, rad)
    print(result)
