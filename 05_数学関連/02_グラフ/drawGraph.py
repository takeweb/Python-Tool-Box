#!/usr/bin/env python
# -*- coding: utf-8 -*-

#%matplotlib inline
import matplotlib.pyplot as plt

# データ
x = [1, 2, 3, 4, 5, 6, 7]
y = [63.3, 64.5, 64.0, 61.0, 67.5, 66.5, 63.1]

plt.plot(x, y)
plt.grid(color='0.8')
plt.xlabel("days")
plt.ylabel("weight")
plt.show()
