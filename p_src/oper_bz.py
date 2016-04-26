#!/usr/bin/env python
# -*- coding: utf-8 -*-


def checkSocialData(pg, data, type):
    name = data.get(type)
    user_name = data.get('user_name')
    if name:
        user_info = checkSocialExists(pg, type, name, user_name)
        if user_info:
            raise Exception('系统已有同名的%s帐号:%s，位于用户%s下' % (type, name, user_info[0].user_name))


def cleanSocialData(pg, data, type):
    '''
    create by bigzhu at 16/04/26 10:43:04 用于add god 时，存在就清除对应的 data.name
    '''
    name = data.get(type)
    user_name = data.get('user_name')
    if name:
        user_info = checkSocialExists(pg, type, name, user_name)
        if user_info:
            del data[type]


def checkSocialExists(pg, type, name, user_name):
    sql = '''
        select * from user_info where %s='%s' and user_name != '%s'
    ''' % (type, name, user_name)
    user_info = list(pg.query(sql))
    return user_info
if __name__ == '__main__':
    pass
