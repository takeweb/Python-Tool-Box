#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

def circle():
    for cnt in range(36):
        forward(20)
        left(10)

for i in range(10):
    circle()
    left(36)

input('type to exit')