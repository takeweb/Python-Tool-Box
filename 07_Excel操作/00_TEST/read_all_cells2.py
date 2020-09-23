#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from openpyxl import load_workbook

def readAllCells(filename):
    wb = load_workbook(filename, read_only=True, data_only=True)
    print(f'{filename}のワークシート情報を読み込みます')
    ws = wb.worksheets[0]
    print(f'{ws.title}のセルを１行ずつ表示します。')

    for i, row in enumerate(ws):
#       print(f"{i}行目")
        if i < 1:
            continue
        elif i == 1:
            headers = [str(column.value) for column in row]
            headers.pop(0)

        for j, col in enumerate(row):
            if col.value is not None:
                if col.data_type == "d":
                    value = col.value
                    print(F'date:{value}')
                else:
                    value = str(col.value)
                    print(col.data_type + ':' + value)

    print(headers)

    wb.close()

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        readAllCells(args[1])
    else:
        print(f'Usage: python {args[0]} filename')