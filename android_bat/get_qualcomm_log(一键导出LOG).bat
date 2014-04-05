@echo off
title get_qualcomm_log [by Pan tengjiao]
goto BEGIN

:COMMENT
echo ##############################################
rem 	get_qualcomm_log.bat
rem			By Tengjiao.Pan @2014-01-21
rem 	Description:
rem 		Used to get qualcomm log 
rem 	Version: 1.0
rem
echo ##############################################

:BEGIN
echo ##########################################################
echo 功能：获取手机上的LOG文件
echo 注意 1) 获取前连上ADB
echo      2) 发现BUG时，请尽可能截张图片以便分析。
echo      3) 获取的Log默认保存在D:/log目录
echo         @Create by Panda , 2014-01-21,V1.0
echo ##########################################################

set "CURR_TIME=%date:~,4%_%date:~5,2%_%date:~8,2%_%time:~,2%_%time:~3,2%_%time:~6,2%"

set DEST_DIR=d:\log\log_qualcomm_%CURR_TIME%\

md "%DEST_DIR%"
md "%DEST_DIR%cur_log\"

adb pull /cache/admin/assertlog  "%DEST_DIR%cur_log\oppo_assertlog"
adb pull /cache/admin/apps  "%DEST_DIR%cur_log\apps"
adb pull /cache/admin/kernel "%DEST_DIR%cur_log\kernel"

adb pull /mnt/sdcard/Pictures/Screenshots "%DEST_DIR%Screenshots"

md  "%DEST_DIR%per_log"
cd   /d  "%DEST_DIR%per_log"

adb shell ls /sdcard/admin/
for /F  %%i in ('adb shell ls /sdcard/admin/') do (
	set "curline=%%i"
	SETLOCAL EnableDelayedExpansion
	set "templine=!curline:~0,-1!"
	echo !templine!
	adb pull /sdcard/admin/!templine!  !templine!
	ENDLOCAL
)

cd ..
rmdir "%DEST_DIR%per_log"

md  "%DEST_DIR%data/tombstones"
cd   /d  "%DEST_DIR%data/tombstones"

adb shell ls /data/tombstones/

for /F  %%i in ('adb shell ls /data/tombstones/') do (
	set "curline=%%i"
	SETLOCAL EnableDelayedExpansion
	set "templine=!curline:~0,-1!"
	echo !templine!
	adb pull /data/tombstones/!templine!  !templine!
	ENDLOCAL
)

cd ..
rmdir "%DEST_DIR%data/tombstones"
cd ..
rmdir "%DEST_DIR%data"

md  "%DEST_DIR%tombstones"
cd   /d  "%DEST_DIR%tombstones"

for /F  %%i in ('adb shell ls /tombstones/') do (
	set "curline=%%i"
	SETLOCAL EnableDelayedExpansion
	set "templine=!curline:~0,-1!"
	echo !templine!
	adb pull /tombstones/!templine!  !templine!
	ENDLOCAL
)

cd ..
rmdir "%DEST_DIR%tombstones"

md  "%DEST_DIR%dropbox"
cd   /d  "%DEST_DIR%dropbox"

for /F  %%i in ('adb shell ls /data/system/dropbox/') do (
	set "curline=%%i"
	SETLOCAL EnableDelayedExpansion
	set "templine=!curline:~0,-1!"
	echo !templine!
	adb pull /data/system/dropbox/!templine!  !templine!
	ENDLOCAL
)

cd ..
rmdir "%DEST_DIR%dropbox"

md  "%DEST_DIR%device_modem_log"
cd   /d  "%DEST_DIR%device_modem_log"

for /F  %%i in ('adb shell ls /sdcard/diag_logs/') do (
	set "curline=%%i"
	SETLOCAL EnableDelayedExpansion
	set "templine=!curline:~0,-1!"
	echo !templine!
	adb pull /sdcard/diag_logs/!templine!  !templine!
	ENDLOCAL
)

cd ..
rmdir "%DEST_DIR%device_modem_log"


rmdir %DEST_DIR%

if exist "%DEST_DIR%" goto finish
echo ##########################################################
echo  获取LOG失败，有可能ADB没连上或手机中没有LOG存在！！！
echo ##########################################################
goto exit

:finish
echo ##########################################################
echo  请到目录--"%DEST_DIR%"--下获取LOG！
echo ##########################################################

pause
exit

:exit
pause