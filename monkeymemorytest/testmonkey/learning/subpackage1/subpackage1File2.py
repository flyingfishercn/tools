#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:subpackage1File2 
#created by zhiquan.huang on 13-12-28 at 下午10:28
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China
#relative reference need to run in this module file to test
#PACKAGE_PARENT = '..'
#SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
#sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#from subpackage1 import subpackage1File1     #相对路径导入

from . import subpackage1File1
#from ..subpackage2 import subpackage2File2 error 上级无__init__.py, 非出于同一个层次中
def test():
    print('subpackage1File2')

print('haha')