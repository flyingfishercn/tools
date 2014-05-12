@echo off
for /l %%c in (1,1,1000) do (
echo ______________________
adb shell cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq

echo Wscript.sleep 200 >y.vbs 
call y.vbs &del y.vbs
)
pause