#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
import json
import time
import datetime
import decimal
import urllib2
import utils

import os


def downloadImageFile(img_url, path_file_name=None):
    '''
    create by bigzhu at 15/04/02 17:24:09 下载图片到指定路径
    '''
    import requests
    if path_file_name is None:
        path_file_name = img_url.split('/')[-1]
    r = requests.get(img_url, stream=True)  # here we need to set stream = True parameter
    with open(path_file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return path_file_name


class ExtEncoder(json.JSONEncoder):

    '''
    modify by bigzhu at 15/01/30 11:25:22 增加对 utils.IterBetter 的支持
    '''

    def default(self, o):
        if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
            return time.mktime(o.timetuple()) * 1000
        elif isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, utils.IterBetter):
            return list(o)
        # Defer to the superclass method
        return json.JSONEncoder(self, o)


def getExpInfoAll(just_info=False):
    '''得到Exception的异常'''
    if just_info:
        info = sys.exc_info()
        return str(info[1])
    else:
        return traceback.format_exc()


def getExpInfo():
    '''得到Exception的异常'''
    return getExpInfoAll(True)


class Storage(dict):

    """
    Storage 就是把 python 的字典的 get set 方法 override 了
    这样用起来比较方便
        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'

    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

storage = Storage


def analyzeStrTable(str_table, title_list, start_with, end_with=None):
    '''
    解析抓取回来的 str table
    转换为 storage 列表,类似从数据库中查出的 data list

    :str_table 需要拆分的 str
    :title_list title 指定切片的对应的 title, 对并表的列名
    :start_with 从哪一行开始,一般会自己带着一列 title, 那么要从1行开始
    :end_with 一些末尾会有多余的空行,需要抛弃
    '''
    title_len = len(title_list)
    li = str_table.split('\n')
    li = li[start_with:end_with]
    li = [i.split() for i in li]
    table = []
    for i in li:
        d = storage()
        for n, v in enumerate(i):
            if n >= title_len:
                d[title_list[title_len - 1]] += ' ' + v
            else:
                d[title_list[n]] = v
        table.append(d)
    return table


def getExecutingPathFile():
    '''
    返回当前执行的 python 文件,带路径
    '''
    # return inspect.getfile(inspect.currentframe()) # script filename
    # (usually with path)
    return os.path.abspath(sys.argv[0])


def getExecutingPath():
    '''
    返回当前执行的 python 文件所在路径
    '''
    # return
    # os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # script directory
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    return dirname


def getLibPath():
    '''
    create by bigzhu at 15/03/06 15:56:48 返回 Lib,也就是现在这段代码所在的路径
    '''
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname


def getProjectName():
    '''
    create by bigzhu at 15/04/04 12:39:07 获取代码所在文件夹
    '''

    path = getExecutingPath()
    project_name = path.split('/')
    return project_name[-1]


def runCommand(command):
    '''
    运行命令
    '''
    try:
        p = os.popen(command)
        content = p.read()
        p.close()
    except Exception:
        content = 'djoin_error:' + getExpInfo(True)
    return content


if __name__ == '__main__':
    #print getExecutingPathFile()
    pass
