#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 角度
th = np.arange(0, 360)

# 円周上の点Pの座標
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

#print("x={}".format(x))
#print("y={}".format(y))

# 描画
plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
