from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice ,MonkeyImage
import os;
import sys;

varProcrankPage = "c:/procrankpage"
varProcrankTotal = "c:/procranktotal"
times=0



def getPidLine(procrankPage, procrankToatal):
	fileSrcObj=open(procrankPage)
	fileDstObj=open(procrankToatal, "ab+")
	for line in fileSrcObj:
		if line.find("com.oppo.camera")>-1:
			fileDstObj.write(line)
			fileDstObj.write("\n")
			print(line)
	fileSrcObj.close()
	fileDstObj.close()
			
if __name__ == '__main__':
	device = MonkeyRunner.waitForConnection() 
	times=int(sys.argv[1])
	shellCmd="adb shell procrank > "+varProcrankPage
	for number in range(times):
		device.startActivity(component='com.oppo.camera/.Camera')
		print number
		MonkeyRunner.sleep(3)
		#device.touch(240,400,'DOWN_UP')#rand cap
		device.press('KEYCODE_BACK')
		os.system(shellCmd)
		getPidLine(varProcrankPage, varProcrankTotal)

	
