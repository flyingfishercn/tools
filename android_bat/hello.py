#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

spath=sys.argv[1]
m=0
bExist=0
psid=0
dstString=""
index=0

file_object=open(spath,"r") # Opens file for writing.Creates this file doesn't exist.
line = file_object.readline()
while line:
    length = len(line)
    for m in range(length):
        if line[m]==' ' and dstString[len(dstString)-1]==' ':
            continue;
        else:
            dstString=dstString+line[m]

    sqllist = dstString.split(' ')

    for sql in sqllist:
        if sql.find('mediaserver')>-1:
            print dstString
            index = 1
            break

    if index > 0:
        psid = int(sqllist[1])
        print psid
        break

    dstString=""
    line = file_object.readline()
print psid
file_object.close()
sys.exit(psid)
