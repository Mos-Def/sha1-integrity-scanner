#!/data/data/com.termux/files/usr/bin/env python3
"""
Integrity Check                                                  UTF-8
Tuesday, June 28th, 2022                                       RD Siegs
"""
import os as os
import fileinput
import subprocess, bash

from bash import bash
from subprocess import PIPE, Popen

#List of files to be scanned
files = []

#File scanner (w3resources)
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

#the scan function is equal to files, and the list is equal to the function. Can use interchanageably
os.scandir(root) == files


#append scan to list and print it
files.append(root)
print(files)

#Making list into string and printing it
s = "-"
x = s.join(files)


#Using bash module to run the bash script to scan python list of files
integrity = bash('bash integrity.sh' + x)






b = bash('ls . ')
sc = bash('bash *.sh')






