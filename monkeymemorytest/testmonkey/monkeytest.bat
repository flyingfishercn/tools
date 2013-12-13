@echo off 
rem close the auto output
rem autotest 1000 times by default
set times=1000
set option=0
set platform=0

set report_enter_exit=c:/testCameraMemory/report_enter_exit.png
set report_switch_camera=c:/testCameraMemory/report_switch_camera.png
set report_capture_camera=c:/testCameraMemory/report_capture_camera.png
set report_record_camera=c:/testCameraMemory/report_record_camera.png
set report_autofocus_camera=c:/testCameraMemory/report_autofocus_camera.png

set procrank_camera_total=c:/testCameraMemory/procrankCameratotal.tmp
set procrank_mediaserver_total=c:/testCameraMemory/procrankMediaservertotal.tmp
set extramem_total=c:/testCameraMemory/catmeminfototal.tmp
set procrank_page=c:/testCameraMemory/procrankpage.tmp

set psfile=c:/ps.log
echo #####################################
rem edit by zhiquan.huang
echo 压力测试，默认1000次
echo 0: 测试所有(all) 
echo 1: 进入退出相机(enter-exit)
echo 2: 前后切换摄像头(switch-camera)
echo 3：普通拍照(capture)
echo 4: 录像(recording)
echo 5: 对焦(autofocus)
echo ##################################### 

set /p option=请输入选项(多项请用.分割):
set /p times=测试次数(enter默认1000次)
echo 您选择测试: %option%  次数 %times%
choice /C 1 /N /M "选项MTK请选择1，选项qualcomm请选择2"
echo platform为%ERRORLEVEL%

cd /d c:/testCameraMemory
del /s/q *.tmp
del /s/q *.png

adb remount

:again
echo  the option is %option% 
if "%option%"=="" goto kill
for /F "tokens=1,* delims=." %%a in ("%option%") do (
	set option=%%b
	if %%a==0 goto all
	if %%a==1 goto enter-exit
	if %%a==2 goto switch-camera
	if %%a==3 goto capture
	if %%a==4 goto recording
	if %%a==5 goto autofocus
	echo invalid option exit
	goto end
)

:all
echo all
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 1 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_enter_exit%

del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 2 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_switch_camera%

del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 3 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_capture_camera%

del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 4 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_record_camera%

del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 5 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_autofocus_camera%
goto again

:enter-exit
echo 进入退出相机测试begin
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 1 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_enter_exit%
goto again

:switch-camera
echo switch-camera
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 2 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_switch_camera%
goto again
 
:capture
echo capture
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 3 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_capture_camera%
goto again

:recording
echo recording
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 4 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_record_camera%
goto again

:autofocus
echo autofocus
cd /d c:/testCameraMemory
del /s/q *.tmp
call monkeyrunner %~dp0\script\units-monkeyPlayback.py 5 %times% %procrank_page% %procrank_camera_total%
call python %~dp0\script\analyseUssDate.py %procrank_camera_total% %procrank_mediaserver_total% %extramem_total% %report_autofocus_camera%
goto again

:kill
echo kill-mediaserver
adb shell ps > %psfile%
call python %~dp0\script\getMediaserverPid.py %psfile%
rem adb shell kill %errorlevel%
echo kill-mediaserver success
goto end

:end
echo Goodbye
pause