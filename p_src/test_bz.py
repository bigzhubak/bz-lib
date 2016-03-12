#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by bigzhu at 15/05/17 10:53:17 用于将所有的module都调用一遍 doctest
    只选出当前运行脚本的目录所有的module来测试
'''
import public_bz
import pkgutil
import doctest


def add(a, b):
    '''
    >>> add(1,1)
    2
    '''
    return a + b


def testAll(test_lib=True):
    '''
    create by bigzhu at 15/05/17 17:44:31 用于测试
        test_lib 决定是否要测试公用库
    '''
    path = public_bz.getExecutingPath()
    all_path=[path]
    if test_lib:
        lib_path = public_bz.getLibPath()
        all_path.insert(0, lib_path)
    print 'starting test path:', path
    for importer, modname, ispkg in pkgutil.iter_modules(all_path):
        if not ispkg:
            print 'test ', modname
            module = importer.find_module(modname).load_module(modname)
            doctest.testmod(module)
if __name__ == '__main__':
    testAll()
