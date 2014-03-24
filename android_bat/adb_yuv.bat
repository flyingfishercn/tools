@echo off
adb remount

del /s /q /f c:\dumpdata\
del /s /q /f c:\procrank.log

if not exist  c:/dumpdata/DCIM/Camera (
   mkdir  c:\dumpdata\DCIM\Camera
)

if not exist  c:/dumpdata/Screenshots (
   mkdir  c:\dumpdata\Screenshots
)

if not exist  c:/dumpdata/zsddump (
   mkdir  c:\dumpdata\zsddump
)

if not exist  c:/dumpdata/hdr (
   mkdir  c:\dumpdata\hdr
)

if not exist  c:/dumpdata/doc_hdr_path (
   mkdir  c:\dumpdata\doc_hdr_path
)

adb pull /mnt/sdcard/DCIM/Camera c:/dumpdata/DCIM/Camera
adb pull /mnt/sdcard/Pictures/Screenshots c:/dumpdata/Screenshots
adb pull /mnt/sdcard/zsd/ c:/dumpdata/zsddump
adb pull /mnt/sdcard/hdr/ c:/dumpdata/hdr
adb pull /mnt/sdcard/doc_hdr_path/ c:/dumpdata/doc_hdr_path
adb pull /mnt/sdcard/procrank.log c:/

adb shell rm /mnt/sdcard/DCIM/Camera/*
adb shell rm /mnt/sdcard/Pictures/Screenshots/*
adb shell rm /mnt/sdcard/zsd/*
adb shell rm /mnt/sdcard/hdr/*
adb shell rm /mnt/sdcard/doc_hdr_path/*
adb shell rm /mnt/sdcard/procrank.log

ping -n 15 127.0.0.1>nul
exit
