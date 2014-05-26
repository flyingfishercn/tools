#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:getVendorFiles 
#created by zhiquan.huang on 14-4-28 at 下午3:55
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China

#!/usr/bin/python -tt
import sys
import os
import os.path
import filecmp

#var def

def moveFile(srcFile, dstFile):
    if os.path.isfile(srcFile):
        dstparent = os.path.dirname(dstFile)
        if not os.path.exists(dstparent):
            os.makedirs(dstparent)
        if not os.path.exists(dstFile):
            open(dstFile, "wb").write(open(srcFile, "rb").read())
        elif filecmp.cmp(srcFile, dstFile):
            print("srcFile and dstFils is already same")
        else:
            print("file is not same, pls check it by yourself")

if __name__ == '__main__':
    #check if parameters is valid
    if len(sys.argv) != 3:
        print("pls check your paramters, the valid format is:  xxx/getVendorFils.py dir keyword")
        sys.exit(1)
    spath = sys.argv[1].strip()               # 指明被遍历的文件夹
    if not os.path.isdir(spath):
        print("pls check, the dir path is not exist")
        sys.exit(1)
    skeyword = sys.argv[2].strip()
    if skeyword.strip() == '':
        print("pls check, the keyword is blank")
        sys.exit(1)

    targetdir = os.path.join(spath, "patchfiles")        # 指明复制到的目录
    print("targetdir is "+targetdir)

    for parent, dirnames, filenames in os.walk(spath.strip()):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #for dirname in dirnames:                       #输出文件夹信息
        #    print("parent is:" + parent)
        #    print("dirname is" + dirname)
        for filename in filenames:                        #输出文件信息
            if '.svn' in parent:
                continue
            filepath = os.path.join(parent, filename)
            file_obj = open(filepath, "r")
            #print("the full name of the file is:" + filepath) #输出文件路径信息
            for line in file_obj:
                line = line.strip()
                if line.find(skeyword) > -1:
                    print("the full name of the file is:" + filepath)
                    print("line is" +line)
                    targetfile = os.path.join(targetdir, os.path.relpath(filepath, spath))
                    moveFile(filepath, targetfile)
                    break;



