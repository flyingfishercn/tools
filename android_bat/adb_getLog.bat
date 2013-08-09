@echo off

echo =========================================================
echo 功能：获取手机上的LOG文件
echo 注意 1) 获取前连上ADB
echo      2) 获取前要把MTKLOG关闭
echo      3) 发现BUG时，请尽可能截张图片(11059，11091，11071，
echo         12007截屏长按menu键,12009及以后机型同时按下电源键
echo         与音量下键（或上键）)以便分析。  
echo      4) 本脚本适用于MTK平台Android智能手机
echo  ---------------------------------------                 
echo  @产品软件部 刘齐虎, 2012-12-07, V2.6
echo  ---------------------------------------                 
echo =========================================================


set "CURR_TIME=%date:~,4%_%date:~5,2%_%date:~8,2%_%time:~,2%_%time:~3,2%_%time:~6,2%"

set DEST_DIR=d:\log\log_pack_%CURR_TIME%\

md "%DEST_DIR%"
cd  /d  "%DEST_DIR%"

rem ==begin.....

adb pull /cache/assertlog  oppo_assertlog
adb pull /data/anr  anr
adb pull /data/tombstones  tombstones
adb pull /data/core  data_core

adb pull /sdcard/screencapture  screen_capture
adb pull /sdcard/Pictures/Screenshots  Screenshots

adb pull /sdcard/灞忓箷鎴浘  屏幕截图
adb pull /sdcard/external_sd/灞忓箷鎴浘  屏幕截图

adb pull /sdcard/mtklog mtklog
adb pull /sdcard/external_sd/mtklog mtklog

rem =======read log from phone storage begin ====
if not exist mtklog md mtklog
adb pull /data/aee_exp mtklog/aee_exp-phone
rem =======read log from phone storage end ====

rmdir mtklog

rem ===================== get oppo log begin ===========================
adb pull /data/data/com.mediatek.engineermode/files/oppoMobileLog oppoMobileLog-phone

if not exist oppoMobileLog-phone md oppoMobileLog-phone
adb pull /data/bootlog oppoMobileLog-phone/bootlog
rmdir oppoMobileLog-phone

adb pull /mnt/sdcard/oppoMobileLog oppoMobileLog
adb pull /mnt/sdcard/external_sd/oppoMobileLog oppoMobileLog
rem ===================== get oppo log end    ===========================


rem =====================state info begin===========================
rem echo dump phone state, please wait...
rem adb shell dumpstate > dumpstate.txt
rem echo dump phone state successfully!
rem =====================state info end=============================

cd ..
rmdir %DEST_DIR%

if exist "%DEST_DIR%" goto finish
echo ============================================================
echo  获取LOG失败，有可能ADB没连上或手机中没有LOG存在！！！
echo ============================================================
goto exit

:finish
echo ============================================================
echo  请到目录--"%DEST_DIR%"--下获取LOG！
echo ============================================================

:exit
pause

@echo on