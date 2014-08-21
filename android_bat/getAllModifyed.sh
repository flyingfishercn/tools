#! /bin/sh

PRJ_NAME=OPPO89T_$1

#REF_FILE=./out/target/product/${PRJ_NAME}/boot.img
REF_FILE=./frameworks/opt/telephony/Android.mk

#add here the paths
SEARCH_PATH=" \
frameworks/opt"

PATCH_TIME=`date +%F-%H-%M`
PATCH_PATH=./patch_${PATCH_TIME}

mkdir ${PATCH_PATH}
find ${SEARCH_PATH} -type f -newer ${REF_FILE} |xargs cp --parent -t ${PATCH_PATH}
tree ${PATCH_PATH} 
