#!/user/bin/env python3
# -*- coding: utf-8 -*-
import re


with open('./CondorHeroes/konfu.txt', 'r', encoding='utf-8') as in_file, open('./CondorHeroes/konfu_all.txt', 'w', encoding='utf-8') as out_file:
    line = in_file.readline()
    while line:
        if not re.search(r'\.',line):
            line = in_file.readline()
            continue
        line = re.sub(r'\d|\.|\t', '', line)
        line.strip()
        out_file.write(line)
        line = in_file.readline()


