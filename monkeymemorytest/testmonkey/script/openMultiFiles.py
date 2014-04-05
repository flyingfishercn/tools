#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:openMultiFiles 
#created by zhiquan.huang on 14-4-3 at 下午9:14
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China

import sys
import os
import pipes
import subprocess
import re
#subprocess.pOpen

spath = sys.argv[1]
psid = 0
gShellProcrankCmd = "D:/software/notepad++/notepad++.exe "
listAndroidFilenames = []

"""
def getmaxfiles():
    result = -1
    filelist = os.listdir(spath)
    for filename in filelist:
        if filename.startswith("android.txt"):
            listAndroidFilenames.append(filename)
    maxfilename = max(listAndroidFilenames)
    print("maxfilename is "+maxfilename)
    listnumber = [int(s) for s in maxfilename.split(".") if s.isdigit()]
    if len(listnumber) != 0:
        result = listnumber[0]
    return result
"""

def getmaxfiles():
    result = -1
    filelist = os.listdir(spath)
    for filename in filelist:
        if filename.startswith("android.txt."):
            listnum = re.findall("\d+", filename)
            listAndroidFilenames.append(''.join(re.findall("\d+", filename)))
    #print(listAndroidFilenames)
    if len(listAndroidFilenames) != 0:
        result = max([int(elem) for elem in listAndroidFilenames])
    return result


if __name__ == '__main__':
    #("openMultiFiles spath"+spath)
    maxfilenameindex = getmaxfiles()
    #print("maxfilenameindex is"+str(maxfilenameindex))

    os.chdir(spath)
    if maxfilenameindex == -1:
        if os.path.exists("android.txt"):
            gShellProcrankCmd = gShellProcrankCmd + "android.txt"+" "
            #print("gShellProcrankCmd"+gShellProcrankCmd)
            subprocess.Popen(gShellProcrankCmd)
    else:
        for i in range(maxfilenameindex, -1, -1):
            if int(i) == 0:
                #print(gShellProcrankCmd)
                gShellProcrankCmd = gShellProcrankCmd + "android.txt" + " "
                subprocess.Popen(gShellProcrankCmd)
            else:
                gShellProcrankCmd = gShellProcrankCmd + "android.txt." + str(i) + " "
