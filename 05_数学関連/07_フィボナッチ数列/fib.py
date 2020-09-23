#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    if n in (0, 1):
        return n
    return fib(n -1) + fib(n -2)

if __name__ == '__main__':
    for i in range(0, 11):
        print(fib(i))