#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def calc(input_num1, input_num2):
    if input_num1 < input_num2:
        input_num1, input_num2 = input_num2, input_num1
    
    while input_num2 != 0:
        input_num1, input_num2 = input_num2, input_num1 % input_num2

    print(input_num1)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print("使い方：" + sys.argv[0] + " input_num1 input_num2")
        sys.exit()

    if args[1].isdigit() and args[2].isdigit():
        calc(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print('Argument is not digit')
