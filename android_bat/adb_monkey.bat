@echo off

adb remount

adb shell monkey -p com.oppo.camera -v 1000000

pause

@echo on