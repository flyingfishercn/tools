#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:fibotest 
#created by zhiquan.huang on 13-12-28 at 下午8:40
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China
import sys
import os.path

#sys.path.append('./fibo.py')
from fibo import *
import imp

#imp.reload(fibo)


if __name__=='__main__':
    print('main begin')
    a=40
    fib(20)
    print(a)
    print('main end')
else:
    print('test')