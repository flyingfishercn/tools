from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice ,MonkeyImage

device = MonkeyRunner.waitForConnection() 

for number in range(1000):
	device.startActivity(component='com.oppo.camera/.Camera')
	print number
	MonkeyRunner.sleep(3)
	#device.touch(240,400,'DOWN_UP')#rand cap
	device.press('KEYCODE_BACK')
	MonkeyRunner.sleep(2)

	
