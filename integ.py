import os as os
import subprocess, bash
import sys

from bash import bash
from subprocess import PIPE, Popen

path = input("Which directory would you like scanned? ")


obj = os.scandir(path)
for entry in obj :
    if entry.is_file():
        print(entry.name)
        stdoutOrigin=sys.stdout 
        sys.stdout = open("files.txt", "w")
        sys.stdout.close()
        sys.stdout=stdoutOrigin
