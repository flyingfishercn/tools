from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice ,MonkeyImage
from UserDict import DictMixin

import sys
import time
import os

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




CMD_MAP = {
	'TOUCH': lambda dev, arg: dev.touch(**arg),
	'DRAG': lambda dev, arg: dev.drag(**arg),
	'PRESS': lambda dev, arg: dev.press(**arg),
	'TYPE': lambda dev, arg: dev.type(**arg),
	'WAIT': lambda dev, arg: MonkeyRunner.sleep(**arg)
}

fileWinInfo="c:/windowInfo"

def getScreenSize():
	shellCmd="adb shell dumpsys window > "+fileWinInfo
	os.system(shellCmd)
	screensize=[]
	try:
		fileObj = open(fileWinInfo)
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
		print(" "+fileWinInfo+"is not exist")
	fileObj.close()
	return screensize

###################################################
ratioSwitchBtnPosX=float(647.0/720)
ratioSwitchBtnPosY=float(67.0/1280)
ratioCaptureBtnPosX=float(360.0/720)
ratioCaptureBtnPosY=float(1194.0/1280)

#{'type':'downAndUp','x':652,'y':66}
def switchcamera(device):
	cmd="TOUCH"

	screensize = getScreenSize()
	switchBtnPosX=ratioSwitchBtnPosX*int(screensize[0])
	switchBtnPosY=ratioSwitchBtnPosY*int(screensize[1])
	#captureBtnPosX=ratioCaptureBtnPosX*int(screensize[0])
	#captureBtnPosY=ratioCaptureBtnPosY*int(screensize[1])
	objOrderDict = OrderedDict()
	objOrderDict["type"]="downAndUp"
	objOrderDict["x"]=switchBtnPosX
	objOrderDict["y"]=switchBtnPosY
	for number in range(100):
		print(number)
		#print(objOrderDict)
		#for i in objOrderDict: 
		#print "dict[%s]=" % i,objOrderDict[i] 
		if cmd not in CMD_MAP:
			print("unknown command:" + cmd)
			break;
		CMD_MAP[cmd](device, objOrderDict)
		time.sleep(4)
###################################################

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
	
def main():
	device = MonkeyRunner.waitForConnection()
	device.startActivity(component='com.oppo.camera/.Camera')
	switchcamera(device)

if __name__ == '__main__':
	main()