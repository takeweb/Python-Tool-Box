#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from openpyxl import load_workbook

def readAllCells(filename):
    wb = load_workbook(filename, read_only=True)
    print(f'{filename}のワークシート情報を読み込みます')
    ws0 = wb.worksheets[1]
    print(f'{ws0.title}のセルを１行ずつ表示します。')

    for row in ws0:
        values = [str(column.value) for column in row]
        print(values)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        readAllCells(args[1])
    else:
        print(f'Usage: python {args[0]} filename')