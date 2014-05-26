#!/bin/bash
#chmod 777 -Rv *

#genetate filenametags for lookupfile
rm -f filenametags
echo -e "!_TAG_FILE_SORTED\t2\t/2=foldcase/" > filenametags
find ./frameworks/base/telephony -not -regex '.*\.\(png\|gif\)' -type f -printf "%f\t%p\t1\n" |  sort -f >> filenametags
find ./frameworks/opt/telephony -not -regex '.*\.\(png\|gif\)' -type f -printf "%f\t%p\t1\n" |  sort -f >> filenametags
find ./oppo/packages/CommCenter/QCOM_phone -not -regex '.*\.\(png\|gif\)' -type f -printf "%f\t%p\t1\n" |  sort -f >> filenametags

#genetate cscope
echo "delete cscope.files, cscope.out, tags"
rm -f cscope.files cscope.out tags
find ./frameworks/base/telephony -regextype posix-extended -regex ".*\.(java|xml|cpp|h)" > cscope.files
find ./frameworks/opt/telephony -regextype posix-extended -regex ".*\.(java|xml|cpp|h)" >> cscope.files
find ./oppo/packages/CommCenter/QCOM_phone -regextype posix-extended -regex ".*\.(java|xml|cpp|h)" >> cscope.files
echo "cscope add cscope.files"
cscope -bCkR -i cscope.files

echo "create tags"
#ctags --languages=c --langmap=c:+.h --extra=+q -R
