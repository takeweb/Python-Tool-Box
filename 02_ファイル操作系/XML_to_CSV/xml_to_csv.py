#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, shutil, argparse
import xml.etree.ElementTree as ET

groupId_list = []
artifactId_list = []
version_list = []

def get_node(node):
    # XMLファイルをパース
    #print("{} {} {}".format(node.tag, node.attrib, node.text.strip()))
    #print("{}{} {} {}".format('    ' * indent, node.tag, node.attrib, node.text.strip()))
    #print("{}{} {}".format('    ' * indent, node.tag, node.text.strip()))
    if node.tag == 'groupId':
        groupId_list.append(node.text.strip())
    elif node.tag == 'artifactId':
        artifactId_list.append(node.text.strip())
    elif node.tag == 'version':
        version_list.append(node.text.strip())

    for child in node:
        get_node(child)

def print_csv():
    out_file = 'result.csv'
    with open(out_file, mode='w') as f:
        for i, groupId in enumerate(groupId_list):
            result = [groupId, artifactId_list[i], version_list[i]+'\n']
            result = ",".join(result)
            f.write(result)

if __name__ == '__main__':
    try:
        # コマンドライン引数設定
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input')

        # コマンドライン引数受け取り
        args = parser.parse_args()
        arg_input = str(args.input)

        # ファイル単品の場合
        in_file = arg_input
        if os.path.isfile(in_file):
            # XMLパース
            tree = ET.parse(in_file)
            get_node(tree.getroot())
            print_csv()
            sys.exit()

    except Exception as e:
        print(e)
