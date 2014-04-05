#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:subpackage2File2
#created by zhiquan.huang on 13-12-28 at 下午10:13
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice ,MonkeyImage
from UserDict import DictMixin

import sys
import time
import os

######################### adb shell procrank ##################
#file name
gProcrankPage = "c:/testCameraMemory/procrankpage.tmp"
gProcrankCameraTotal = "c:/testCameraMemory/procrankCameratotal.tmp"
gProcrankMediaserverTotal = "c:/testCameraMemory/procrankMediaservertotal.tmp"
#shell cmd
gShellProcrankCmd = "adb shell procrank > "+gProcrankPage

######################### adb shell cat /proc/meminfo ##################
#file name
gCatMeminfoPage = "c:/testCameraMemory/catmeminfopage.tmp"
gCatMeminfoTotalPage = "c:/testCameraMemory/catmeminfototal.tmp"
#shell cmd
gShellCatMeminfoCmd = "adb shell cat /proc/meminfo > "+gCatMeminfoPage

################## adb shell dumpsys meminfo ###############
gShellDumpsysMeminfoCmd = "adb shell dumpsys meminfo"

################## adb shell dumpsys window ###############
gWinInfo = "c:/testCameraMemory/windowInfo.tmp"
gShellWininfoCmd = "adb shell dumpsys window > "+gWinInfo

CMD_MAP = {
    'TOUCH': lambda dev, arg: dev.touch(**arg),
    'DRAG': lambda dev, arg: dev.drag(**arg),
    'PRESS': lambda dev, arg: dev.press(**arg),
    'TYPE': lambda dev, arg: dev.type(**arg),
    'WAIT': lambda dev, arg: MonkeyRunner.sleep(**arg)
}

#########################tools begin###################
class OrderedDict(dict, DictMixin):

    def __init__(self, *args, **kwds):
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__end
        except AttributeError:
            self.clear()
        self.update(*args, **kwds)

    def clear(self):
        self.__end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.__map = {}                 # key --> [key, prev, next]
        dict.clear(self)

    def __setitem__(self, key, value):
        if key not in self:
            end = self.__end
            curr = end[1]
            curr[2] = end[1] = self.__map[key] = [key, curr, end]
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        key, prev, next = self.__map.pop(key)
        prev[2] = next
        next[1] = prev

    def __iter__(self):
        end = self.__end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.__end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def popitem(self, last=True):
        if not self:
            raise KeyError('dictionary is empty')
        if last:
            key = reversed(self).next()
        else:
            key = iter(self).next()
        value = self.pop(key)
        return key, value

    def __reduce__(self):
        items = [[k, self[k]] for k in self]
        tmp = self.__map, self.__end
        del self.__map, self.__end
        inst_dict = vars(self).copy()
        self.__map, self.__end = tmp
        if inst_dict:
            return (self.__class__, (items,), inst_dict)
        return self.__class__, (items,)

    def keys(self):
        return list(self)

    setdefault = DictMixin.setdefault
    update = DictMixin.update
    pop = DictMixin.pop
    values = DictMixin.values
    items = DictMixin.items
    iterkeys = DictMixin.iterkeys
    itervalues = DictMixin.itervalues
    iteritems = DictMixin.iteritems

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, self.items())

    def copy(self):
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        d = cls()
        for key in iterable:
            d[key] = value
        return d

    def __eq__(self, other):
        if isinstance(other, OrderedDict):
            if len(self) != len(other):
                return False
            for p, q in  zip(self.items(), other.items()):
                if p != q:
                    return False
            return True
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self == other

#procrank
def getPidLine(procrankPage, procrankToatal, processName):
    fileSrcObj=open(procrankPage)
    fileDstObj=open(procrankToatal, "ab+")
    processName = processName.strip()
    for line in fileSrcObj:
        if line.find(processName)>-1:
            fileDstObj.write(line)
            fileDstObj.write("\n")
            #print(line)
    fileSrcObj.close()
    fileDstObj.close()

#/proc/meminfo
def getExtraMem(meminfoPage, meminfoTotal):
    fileSrcObj=open(meminfoPage)
    fileDstObj=open(meminfoTotal, "ab+")
    sep = ':'
    memfree = 0;
    buffers = 0;
    cached = 0;
    for line in fileSrcObj:
        if line.find('MemFree')>-1:
            sz = line.strip().split(sep)
            memfree = int(sz[1].strip(' kKBb'))
            print('memfree is '+str(memfree))
        if line.find('Buffers')>-1:
            sz = line.strip().split(sep)
            buffers = int(sz[1].strip(' kKBb'))
            print('buffers is '+str(buffers))
        if line.find('Cached')>-1 and line.find('SwapCached') == -1 :
            sz = line.strip().split(sep)
            cached = int(sz[1].strip(' kKBb'))
            print('cached is '+str(cached))
    extramem = memfree + buffers + cached;
    print('extramem is ' + str(extramem))
    fileDstObj.write(str(extramem))
    fileDstObj.write("\n")
    fileSrcObj.close()
    fileDstObj.close()
    return extramem

def getScreenSize():
    os.system(gShellWininfoCmd)
    screensize=[]
    try:
        fileObj = open(gWinInfo)
        for line in fileObj:
            if line.find("mUnrestrictedScreen")>-1:
                line=" ".join(line.split())
                linetokens=line.split(" ")
                (height, width)=linetokens[1].split("x")
                print("screen size width and height is"+width +" "+height)
                screensize.append(height)
                screensize.append(width)
                break
    except:
        print(" "+gWinInfo+"is not exist")
    fileObj.close()
    return screensize

def getcurrentmeminfo():
    os.system(gShellProcrankCmd)
    os.system(gShellCatMeminfoCmd)
    if os.path.exists(gProcrankPage):
        getPidLine(gProcrankPage, gProcrankCameraTotal, 'com.oppo.camera')
        getPidLine(gProcrankPage, gProcrankMediaserverTotal, 'system/bin/mediaserver')
    if os.path.exists(gCatMeminfoPage):
        getExtraMem(gCatMeminfoPage, gCatMeminfoTotalPage)

#########################tools end###################

#########################enter-exit begin#############
def enterexit(device, times):
    #print("gShellProcrankCmd is"+gShellProcrankCmd)
    for number in range(times):
        device.startActivity(component='com.oppo.camera/.Camera')
        #print number
        time.sleep(4)
        #device.touch(240,400,'DOWN_UP')#rand cap
        device.press('KEYCODE_BACK')
        os.system(gShellProcrankCmd)
        getcurrentmeminfo()
        if number==times:
            time.sleep(4)
#########################enter-exit end##############
	
#########################switch-camera begin#########
ratioSwitchBtnPosX=float(967.0/1080)
ratioSwitchBtnPosY=float(101.0/1920)

#{'type':'downAndUp','x':652,'y':66}
def switchCamera(device, times):
    #print("gShellProcrankCmd is"+gShellProcrankCmd)
    cmd="TOUCH"
    screensize = getScreenSize()
    switchBtnPosX=ratioSwitchBtnPosX*int(screensize[0])
    switchBtnPosY=ratioSwitchBtnPosY*int(screensize[1])
    objOrderDict = OrderedDict()
    objOrderDict["type"]="downAndUp"
    objOrderDict["x"]=switchBtnPosX
    objOrderDict["y"]=switchBtnPosY
    for number in range(times):
        #print(number)
        #print(objOrderDict)
        #for i in objOrderDict:
        #print "dict[%s]=" % i,objOrderDict[i]
        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            break
        CMD_MAP[cmd](device, objOrderDict)
        time.sleep(4)
        os.system(gShellProcrankCmd)
        getcurrentmeminfo()
        if number==times:
            device.press('KEYCODE_BACK')
#########################switch-camera end##########

#########################  capture begin  ##########
ratioCaptureBtnPosX=float(274.0/540)
ratioCaptureBtnPosY=float(897.0/960)
#TOUCH|{'x':357,'y':1200,'type':'downAndUp',}
def captureCamera(device, times):
    #print("gShellProcrankCmd is"+gShellProcrankCmd)
    cmd="TOUCH"
    screensize = getScreenSize()
    captureBtnPosX=ratioCaptureBtnPosX*int(screensize[0])
    captureBtnPosY=ratioCaptureBtnPosY*int(screensize[1])
    objOrderDict = OrderedDict()
    objOrderDict["type"]="downAndUp"
    objOrderDict["x"]=captureBtnPosX
    objOrderDict["y"]=captureBtnPosY
    for number in range(times):
        #print(number)
        #print(objOrderDict)
        #for i in objOrderDict:
        #print "dict[%s]=" % i,objOrderDict[i]
        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            break;
        CMD_MAP[cmd](device, objOrderDict)
        time.sleep(1.5)
        #os.system(gShellProcrankCmd)
        #getcurrentmeminfo()
        if number==times:
            device.press('KEYCODE_BACK')
#########################  capture end  ###########

#########################  record begin  ##########
ratioRecordBtnPosX=float(130.0/1080)
ratioRecordBtnPosY=float(1790.0/1920)
#TOUCH|{'x':81,'y':1194,'type':'downAndUp',}
def recordCamera(device, times):
    #print("gShellProcrankCmd is"+gShellProcrankCmd)
    cmd="TOUCH"
    screensize = getScreenSize()
    recordBtnPosX=ratioRecordBtnPosX*int(screensize[0])
    recordBtnPosY=ratioRecordBtnPosY*int(screensize[1])
    objOrderDict = OrderedDict()
    objOrderDict["type"]="downAndUp"
    objOrderDict["x"]=recordBtnPosX
    objOrderDict["y"]=recordBtnPosY
    for number in range(times):
        print(number)
        #print(objOrderDict)
        #for i in objOrderDict:
        #print "dict[%s]=" % i,objOrderDict[i]
        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            break;
        #start recording
        CMD_MAP[cmd](device, objOrderDict)
        time.sleep(10)
        #stop recording
        CMD_MAP[cmd](device, objOrderDict)
        os.system(gShellProcrankCmd)
        getcurrentmeminfo()
        if number==times:
            device.press('KEYCODE_BACK')
#########################  record end  ###########

#########################  autofocus begin  ##########
ratioAutofocusBtnPosX=float(540.0/1080)
ratioAutofocusBtnPosY=float(960/1920)
##TOUCH|{'x':360,'y':640,'type':'downAndUp',}
def autofocusCamera(device, times):
    #print("gShellProcrankCmd is"+gShellProcrankCmd)
    cmd="TOUCH"
    screensize = getScreenSize()
    autofocusPosX=ratioAutofocusBtnPosX*int(screensize[0])
    autofocusPosY=ratioAutofocusBtnPosY*int(screensize[1])
    objOrderDict = OrderedDict()
    objOrderDict["type"]="downAndUp"
    objOrderDict["x"]=autofocusPosX
    objOrderDict["y"]=autofocusPosY
    for number in range(times):
        #print(number)
        #print(objOrderDict)
        #for i in objOrderDict:
        #print "dict[%s]=" % i,objOrderDict[i]
        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            break;
        CMD_MAP[cmd](device, objOrderDict)
        time.sleep(4)
        os.system(gShellProcrankCmd)
        getcurrentmeminfo()
        if number==times:
            device.press('KEYCODE_BACK')
#########################  autofocus end  ###########
def hdrtestCamera(device, times):
     for number in range(times):
        cmd="TOUCH"
        screensize = getScreenSize()
        capturePosX=272
        capturePosY=898
        objOrderDict = OrderedDict()
        objOrderDict["type"]="downAndUp"
        objOrderDict["x"]=capturePosX
        objOrderDict["y"]=capturePosY
        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            break;
        CMD_MAP[cmd](device, objOrderDict)
        time.sleep(2)
        os.system(gShellProcrankCmd)
        getcurrentmeminfo()
        if number==times:
            device.press('KEYCODE_BACK')



######################### change camera mode only begin #####
'''
ratioHdrBtnPosX
ratioHdrBtnPosY
ratioPanBtnPosX
ratioPanBtnPosY
ratioFaceBeautyPosX
ratioFaceBeautyPosY
ratioSlowShutterPosX
ratioSlowShutterPosY
ratio
'''

######################### change camera mode only end #####

def process_file(fp, device):
    for line in fp:
        print("sequence is"+line)
        (cmd, rest) = line.split('|')
        try:
            rest = eval(rest)
        except:
            print("unable to parse options")
            continue

        if cmd not in CMD_MAP:
            print("unknown command:" + cmd)
            continue
        CMD_MAP[cmd](device, rest)
        time.sleep(4)

def funcmodule(type, device, times):
    testfunc = {'1':lambda:enterexit(device, times),
                '2':lambda:switchCamera(device, times),
                '3':lambda:captureCamera(device, times),
                '4':lambda:recordCamera(device, times),
                '5':lambda:autofocusCamera(device, times),
                '6':lambda:hdrtestCamera(device, times)}
    print("type is"  +type )
    return testfunc[type]()

def main():
    device = MonkeyRunner.waitForConnection()
    device.startActivity(component='com.oppo.camera/.Camera')
    #type=int(sys.argv[1])
    type=sys.argv[1].strip()
    times =int(sys.argv[2])
    funcmodule(type, device, times)

if __name__ == '__main__':
	main()