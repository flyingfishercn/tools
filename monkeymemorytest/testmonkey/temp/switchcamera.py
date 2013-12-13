from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, os, stat
device = MonkeyRunner.waitForConnection()
P1=360 #px of front camera switch
P2=1195 #py of front camera switch
P3=630 #px of back camera switch
P4=70 #py of back camera switch
P5=65 #px of back camera switch
P6=1195 #py of back camera switch

if not os.path.isdir('D:\\photo'):
    os.mkdir('D:\\photo')
    os.mkdir('D:\\photo\\f')
    os.mkdir('D:\\photo\\b')    

def txt(str):
    if os.path.exists('D:\\AndroidAuto\\Message\\inspect.txt'):
        os.remove('D:\\AndroidAuto\\Message\\inspect.txt')
    f = open('D:\\AndroidAuto\\Message\\inspect.txt', 'a') 
    f.write(str)
    f.close()

try:
    for i in range(1000):
        p=device.getProperty('display.height')
        if str(p)=='None':
            break
        MonkeyRunner.sleep(3)
        device.touch(P1,P2,'DOWN_UP')#cap button
        device.takeSnapshot().writeToFile('D:\\photo\\f\\'+str(i+1)+'1.jpg','.jpg')        
        MonkeyRunner.sleep(3)
        device.touch(P1,P2,'DOWN_UP')#cap button
        device.takeSnapshot().writeToFile('D:\\photo\\f\\'+str(i+1)+'2.jpg','.jpg') 
        MonkeyRunner.sleep(3)
        device.touch(240,400,'DOWN_UP')#rand cap
        device.takeSnapshot().writeToFile('D:\\photo\\f\\'+str(i+1)+'3.jpg','.jpg') 
        MonkeyRunner.sleep(3)
        device.touch(240,400,'DOWN_UP')#rand cap
        device.takeSnapshot().writeToFile('D:\\photo\\f\\'+str(i+1)+'4.jpg','.jpg') 
        MonkeyRunner.sleep(3)                
        device.touch(P3,P4,'DOWN_UP')#cam switch
        MonkeyRunner.sleep(3)
        device.touch(P1,P2,'DOWN_UP')#cap button
        device.takeSnapshot().writeToFile('D:\\photo\\b\\'+str(i+1)+'1.jpg','.jpg')        
        MonkeyRunner.sleep(3)
        device.touch(P1,P2,'DOWN_UP')#cap button
        device.takeSnapshot().writeToFile('D:\\photo\\b\\'+str(i+1)+'2.jpg','.jpg') 
        MonkeyRunner.sleep(3)
        device.touch(240,400,'DOWN_UP')#rand cap
        device.takeSnapshot().writeToFile('D:\\photo\\b\\'+str(i+1)+'3.jpg','.jpg') 
        MonkeyRunner.sleep(3)
        device.touch(240,400,'DOWN_UP')#rand cap
        device.takeSnapshot().writeToFile('D:\\photo\\b\\'+str(i+1)+'4.jpg','.jpg') 
        MonkeyRunner.sleep(3)
        device.touch(P3,P4,'DOWN_UP')#cam switch         
        MonkeyRunner.sleep(3)
        device.touch(P5,P6,'DOWN_UP')#go in pic
        MonkeyRunner.sleep(3)
        device.press('KEYCODE_BACK','DOWN_AND_UP')
        MonkeyRunner.sleep(1)
        device.touch(P1,P2,device.DOWN)#cap button
        MonkeyRunner.sleep(10)
        device.touch(P1,P2,device.UP)#cap button
        MonkeyRunner.sleep(1)
        device.touch(P3,P4,'DOWN_UP')#cam switch
        MonkeyRunner.sleep(3)
        device.touch(P1,P2,device.DOWN)#cap button
        MonkeyRunner.sleep(10)
        device.touch(P1,P2,device.UP)#cap button
        MonkeyRunner.sleep(1)
        device.touch(P5,P6,'DOWN_UP')#go in pic
        MonkeyRunner.sleep(3)
        device.press('KEYCODE_BACK','DOWN_AND_UP')
        MonkeyRunner.sleep(1)        
        device.touch(P3,P4,'DOWN_UP')#cam switch
        MonkeyRunner.sleep(3)        
        txt(str(i+1)+'|'+str(1000)+'#0')
    txt(str(i+1)+'|'+str(1000)+'#1')
    p=device.getProperty('display.width')
    if str(p)=='None':
        txt(str(i+1)+'|'+str(1000)+'#2')    
except:
    txt(str(i+1)+'|'+str(1000)+'#2')
