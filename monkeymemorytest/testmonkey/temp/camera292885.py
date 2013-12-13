from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice 
device = MonkeyRunner.waitForConnection()
device.startActivity(component='com.oppo.camera/.activity.Camera')
MonkeyRunner.sleep(6)
for i in range(0,1000):
    print i
    device.touch(240,30,'DOWN_UP')
    MonkeyRunner.sleep(2)
    device.touch(158,168,'DOWN_UP')
    MonkeyRunner.sleep(2)
    device.touch(240,745,'DOWN_UP')
    MonkeyRunner.sleep(15)
    device.press('KEYCODE_BACK','DOWN_AND_UP')
    MonkeyRunner.sleep(5) 
	print("hello")
else:
    print('end') 