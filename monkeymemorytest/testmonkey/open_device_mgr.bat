@echo off
if %1%==0 goto devmgmt
if %1%==1 goto appwiz.cpl
goto end

rem 环境变量
:devmgmt
start devmgmt.msc
goto end

:appwiz.cpl
start appwiz.cpl
goto end

:end
ping -n 2 127.0.0.1>nul
exit

rem 安装卸载程序


