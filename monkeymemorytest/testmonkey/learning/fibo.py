#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name:fibo 
#created by zhiquan.huang on 13-12-28 at 下午8:35
#Pls contact flyingfishercn@gmail.com or huangzq@oppo.com
#Software Engineer
#Product Software Department
#Guangdong OPPO Mobile Telecommunications Corp.，Ltd
#Gaoxin park South District 1st Road shenzhen, China
import sys
import subpackage1.subpackage1File1
import subpackage1.subpackage1File2
import subpackage2.subpackage2File2

sys.path.append('c:/testsyspath/')
print(sys.path)

__all__=['fib']  #exposure interface

a=47
print('fibo.py import')

def fib(n):    # write Fibonacci series up to n
    a = 1
    print(a)

if __name__=='__main__':        #当前非main模块执行
    print('fibo main begin')
    print('fibo main end')
    print(sys.path)
    subpackage1.subpackage1File1.test()
    subpackage1.subpackage1File2.test()
else:
    print('test')
