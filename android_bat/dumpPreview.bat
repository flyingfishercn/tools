@echo off 
adb remount
set propertyfile=c:/property
adb shell getprop camera.dumpbuffer.enable > %propertyfile%

python proprety.py %propertyfile%

if %errorlevel%==1  goto disable
if %errorlevel%==0  goto enable

:disable
echo disable previewdump
adb shell setprop camera.dumpbuffer.enable 0

goto exit

:enable
echo enable previewdump
adb shell setprop camera.dumpbuffer.enable 1
ping -n 20 127.0.0.1>nul
goto disable

:exit
echo Goodbye, all over
pause
