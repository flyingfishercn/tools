#! /bin/sh

PRJ_NAME=OPPO89T_$1

#REF_FILE=./out/target/product/${PRJ_NAME}/boot.img
REF_FILE=./Makefile

SEARCH_PATH=" \
frameworks/base \
frameworks/av \
mediatek/frameworks/av \
mediatek/frameworks/base \
mediatek/frameworks-ext/av \
mediatek/frameworks-ext/base \
mediatek/platform/mt6589/hardware/camera \
mediatek/hardware/camera \
mediatek/custom/common/kernel/imgsensor \
vendor/oppo_preset/OPPO89T_12083/app/multimedia/OppoCamera/"

PATCH_TIME=`date +%F-%H-%M`
PATCH_PATH=./patch_${PATCH_TIME}

mkdir ${PATCH_PATH}
find ${SEARCH_PATH} -type f -newer ${REF_FILE} |xargs cp --parent -t ${PATCH_PATH}
tree ${PATCH_PATH} 
