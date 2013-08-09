@echo off 
rem 关闭自动输出
rem 接收输入
:begin
set home=G:\FIND5_V1891
set target=msm8960
set psfile=c:/ps.log

set input=0
echo PROJECT=G:\FIND5_V1891
echo 1: push libmmcamera_frameproc.so
echo 2: vendor_server


echo 0: goto adbshell
echo -1:exit
set /p input=请输入字符串:


rem 输出得到的输入信息

echo 您输入的字符串是：%input%

adb remount
if %input%==0 goto adbshell
if %input%==1 goto HAL
if %input%==2 goto vendor_server
if %input%==-1 goto exit

:libmmcamera_frameproc.so
echo libandroid_runtime.so
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_frameproc.so /system/lib/
goto kill

:vendor_server
echo camera.msm8960.so
adb push %home%\out\target\product\%target%\system\lib\hw\camera.msm8960.so /system/lib/hw/
adb push %home%\out\target\product\%target%\system\lib\liboemcamera.so                         /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_3a_legacy.so                /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_statsproc31.so              /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_plugin.so                   /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_frameproc.so                /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_cpp.so                      /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_interface.so                /system/lib
adb push %home%\out\target\product\%target%\system\lib\libmmcamera_interface2.so               /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_imx135_default_video.so    /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_imx135_preview.so          /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_imx135_zsl.so              /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_imx135_hfr_120fps.so       /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_s5k6a3yx_default_video.so  /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_s5k6a3yx_preview.so        /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_s5k6a3yx_zsl.so            /system/lib
adb push %home%\out\target\product\%target%\system\lib\libchromatix_s5k6a3yx_video_hd.so       /system/lib
adb push %home%\out\target\product\%target%\system\lib\hw\camera.msm8960.so                    /system/lib/hw
goto kill

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
