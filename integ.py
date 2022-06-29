#!/data/data/com.termux/files/usr/bin/env python3
"""
Integrity Check                                                  UTF-8
Tuesday, June 28th, 2022                                       RD Siegs
"""
import os as os
import fileinput

from bash import bash
from subprocess import PIPE, Popen


files = []


root = input("Which directory do you want scanned? ")
for entry in os.scandir(root):
   if entry.is_dir():
       typ = 'dir'
   elif entry.is_file():
       typ = 'file'
   elif entry.is_symlink():
       typ = 'link'
   else:
       typ = 'unknown'
   print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))


os.scandir(root) == files


file.append(root)

*print(files)

s = "-"

x = s.join(files)
print(x)

integrity = bash('bash integrity.sh' + x)

print(integrity)





