@echo off 
rem 关闭自动输出
rem 接收输入
:begin
rem set /p input=请输入字符串:

rem 输出得到的输入信息

rem echo 您输入的字符串是：%input%

adb remount
call python %~dp0\script\analyseTime.py C:\1234.log
@pause 
