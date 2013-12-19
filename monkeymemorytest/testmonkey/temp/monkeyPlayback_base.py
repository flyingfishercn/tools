from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice ,MonkeyImage
from UserDict import DictMixin

import sys
import time
import os



ratioSwitchBtnPosX=float(647.0/720)
ratioSwitchBtnPosY=float(67.0/1280)
ratioCaptureBtnPosX=float(360.0/720)
ratioCaptureBtnPosY=float(1194.0/1280)

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

#{'type':'downAndUp','x':652,'y':66}
def switchcamera(device):
	cmd="TOUCH"
	objDict = {}
	objDict['type'] = 'downAndUp'
	objDict['x'] = 652
	for number in range(5):
		print(number)
		print(objDict)
		if cmd not in CMD_MAP:
			print("unknown command:" + cmd)
			break;
		CMD_MAP[cmd](device, {'type':'downAndUp','x':652,'y':66})
		time.sleep(4)

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
	screensize = getScreenSize()
	
	switchBtnPosX=ratioSwitchBtnPosX*int(screensize[0])
	switchBtnPosY=ratioSwitchBtnPosY*int(screensize[1])
	captureBtnPosX=ratioCaptureBtnPosX*int(screensize[0])
	captureBtnPosY=ratioCaptureBtnPosY*int(screensize[1])
	
	#file = sys.argv[1]
	#fp = open(file, 'r')
	device = MonkeyRunner.waitForConnection()
	device.startActivity(component='com.oppo.camera/.Camera')
	switchcamera(device)
	#process_file(fp, device)
	#fp.close();

if __name__ == '__main__':
	main()