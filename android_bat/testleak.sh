#!/system/bin/sh
while true
do

    date >> /mnt/sdcard/procrank.log
    procrank >> /mnt/sdcard/procrank.log
    echo >> /mnt/sdcard/procrank.log
    sleep 5
done
