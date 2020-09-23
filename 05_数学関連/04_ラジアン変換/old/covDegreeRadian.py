#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys

args = sys.argv

if len(args) == 2 and args[1].isdigit():
    degree = int(args[1])

# 度をラジアンへ変換
rad = math.radians(degree)

print(rad)
