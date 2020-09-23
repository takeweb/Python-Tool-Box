#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse
from openpyxl import load_workbook

def createDDL(filename):
    wb = load_workbook(filename, read_only=True, data_only=True)
    sheet_list = wb.sheetnames
    for sheet_name in sheet_list:
        col_info_list = []
        ws = wb[sheet_name]
        for i, row in enumerate(ws):
            col_info = {}
            name = ""
            for j, col in enumerate(row):
                if j == 3:
                    if i == 1:
                        table_name = str(col.value).rstrip()
                    elif i == 2:
                        table_remarks = str(col.value).rstrip() 
 
                if col.value is not None:
                    if col.data_type == "d":
                        value = col.value
                    else:
                        value = str(col.value).rstrip()

                    if i >= 6:
                        if j == 1:
                            col_info["remarks"] = value
                        elif j == 2:
                            col_info["name"] = value
                            name = value
                        elif j == 3:
                            col_info["data_type"] = value
                        elif j == 4:
                            col_info["pk"] = "  , PRIMARY KEY (" + name + ")"
                        elif j == 5:
                            col_info["not_null"] = " NOT NULL"
                        elif j == 6:
                            col_info["default"] = " DEFAULT " + value
                        #print(f'data:{value}')
            if len(col_info) > 0:
                #print(col_info)
                col_info_list.append(col_info)
        #print(table_name)
        #print(table_remarks)
        #print(col_info_list)
        writeFile(table_name, table_remarks, col_info_list)
    wb.close()

def writeFile(table_name, table_remarks, col_info_list):
    file_name = "./sql/" + table_name + ".sql"
    col = ""
    pk = ""
    with open(file_name, "w", encoding = "utf_8", newline='\n') as out_f:
        out_f.write("CREATE TABLE " + table_name + "(\n")
        for i, col_info in enumerate(col_info_list):
            col = ""
            if i == 0:
                col += "    "
            else:
                col += "  , "
            col += col_info["name"] + " " + col_info["data_type"]
            if "not_null" in col_info:
                col += col_info["not_null"]
            if "default" in col_info:
                col += col_info["default"]
            col += "\n"
            out_f.write(col)
            if "pk" in col_info:
                pk = col_info["pk"]
        out_f.write(pk + "\n")
        out_f.write(");\n\n")

        # コメント出力
        out_f.write("COMMENT ON TABLE " + table_name + " IS '" + table_remarks + "';\n")
        for i, col_info in enumerate(col_info_list):
            col = "COMMENT ON COLUMN " 
            col += table_name + "." + col_info["name"] + " IS '" + col_info["remarks"] + "';\n"
            out_f.write(col)

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        input_file = args.file

        createDDL(input_file)

        print("Done!!")

    except Exception as e:
        print(e)

