#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:subpackage2File2
#created by zhiquan.huang on 13-12-28 at 下午10:13
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China

import sys
import time
import datetime

def Caltime(strTime1, strTime2):
    TIME_FORMAT = '%H:%M:%S.%f'
    seconds = (datetime.datetime.strptime(strTime1, TIME_FORMAT) - datetime.datetime.strptime(strTime2, TIME_FORMAT)).total_seconds()
    print(seconds)
    #print(structTime1)
    #time1 = time.mktime(structTime1)
    #time2 = time.mktime(structTime2)
    #return time2-time1

spath = sys.argv[1]
skeyword = 'ShutterThread begin'
print('skeyword is '+skeyword)
psid = 0
file_object = open(spath, 'r', encoding='utf-8') # Opens file for writing.Creates this file doesn't exist.
before = '0:0:0.0'
for line in file_object:
    if line.strip() == '':
        continue

    if line.find(skeyword) > -1:
        line = ' '.join(line.split())
        lineTokens = line.split(' ')
        #psid = int(lineTokens[1])
        #print(line)
        Caltime(lineTokens[1], before)
        before = lineTokens[1]
        #print(Caltime('14:42:35.893', '14:42:36.894'))
file_object.close()
sys.exit(psid)
