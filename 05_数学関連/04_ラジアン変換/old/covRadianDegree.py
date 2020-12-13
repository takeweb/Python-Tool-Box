#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys

args = sys.argv

if len(args) == 2:
    rad = float(args[1])
else:
    print("args error!")

# ラジアンを度へ変換
degree = math.degrees(rad)

print(degree)
