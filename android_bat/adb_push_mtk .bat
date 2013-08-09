@echo off 
rem 关闭自动输出
rem 接收输入
:begin
set home=h:/12083_cmcc_svn4456/
set target=OPPO89T_12083
set psfile=c:/ps.log

set input=0

echo 1: push libandroid_runtime.so
echo 2: push libcam.camadapter.so
echo 3: push libcam.client.so
echo 4: push camera.default.so
echo 5: push libcam.camshot.so
echo 6: push libcameraservice.so
echo 7: push libcam.paramsmgr.so


echo 9: push OppoCamera.apk
echo 0: goto adbshell
echo -1:exit
set /p input=请输入字符串:


rem 输出得到的输入信息

echo 您输入的字符串是：%input%

adb remount
if %input%==0 goto adbshell
if %input%==1 goto libandroid_runtime.so
if %input%==2 goto libcam.camadapter.so
if %input%==3 goto libcam.client.so
if %input%==4 goto camera.default.so
if %input%==5 goto libcam.camshot.so

if %input%==6 goto libcameraservice.so
if %input%==7 goto libcam.paramsmgr.so
if %input%==9 goto OppoCamera.apk
if %input%==-1 goto exit

:libandroid_runtime.so
echo libandroid_runtime.so
adb push %home%\out\target\product\%target%\system\lib\libandroid_runtime.so /system/lib/
goto kill

:libcam.camadapter.so
echo libcam.camadapter.so
adb push %home%\out\target\product\%target%\system\lib\libcam.camadapter.so /system/lib/
goto kill

:libcam.client.so
echo libcam.client.so
adb push %home%\out\target\product\%target%\system\lib\libcam.client.so /system/lib/
goto kill

:camera.default.so
echo camera.default.so
adb push %home%\out\target\product\%target%\system\lib\hw\camera.default.so /system/lib/hw/
goto kill

:libcameraservice.so
echo libcameraservice.so
adb push %home%\out\target\product\%target%\system\lib\libcameraservice.so /system/lib/
goto kill

:libcam.paramsmgr.so
echo libcameraservice.so
adb push %home%\out\target\product\%target%\system\lib\libcam.paramsmgr.so /system/lib/
goto kill

:libcam.camshot.so
echo libcam.camshot.so
adb push %home%\out\target\product\%target%\system\lib\libcam.camshot.so /system/lib/
adb push %home%\out\target\product\%target%\system\lib\libacdk.so /system/lib/
goto kill

:OppoCamera.apk
echo OppoCamera.apk
adb push %home%\out\target\product\%target%\system\app\OppoCamera.apk /system/app/
goto end

:kill
adb shell ps > %psfile%
python hello.py %psfile%
adb shell kill %errorlevel%
goto end

:adbshell
adb shell

:end
set input = 0;
goto begin

:exit
echo good bye
pause
