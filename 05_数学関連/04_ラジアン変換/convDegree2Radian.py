#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    try:
        for deg in range(0, 361, 15):
            rad = math.radians(deg)
            print(str(deg).zfill(3) + "→" + str(rad))
    except Exception as e:
        print(e)

