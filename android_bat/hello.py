#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import sys

spath=sys.argv[1]
spidname=sys.argv[2]
psid=0
dstString=""
index=0

file_object=open(spath,"r") # Opens file for writing.Creates this file doesn't exist.
for line in file_object:
	if line.strip()=="":
		continue
	#reset
	index=0
	line = ' '.join(line.split(' '))
	sqllist= line.split(' ')

	for sql in sqllist:
		if sql.find(spidname)>-1:
			print(line)
			index=index+1
			break

	if index > 0:
		#index 5 is the spidname's process id
		print(sqllist)
		psid = int(sqllist[5])
		break

	dstString=""
file_object.close()
sys.exit(psid)
