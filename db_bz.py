#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public_bz
import psycopg2
import functools
import time
from webpy_db import SQLLiteral
from webpy_db import SQLQuery
from webpy_db import sqlparam


def daemonDB(method):
    '''
    自动重连数据库的一个装饰器
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except(psycopg2.OperationalError, psycopg2.InterfaceError, psycopg2.DatabaseError):
            print public_bz.getExpInfoAll()
            self.pg.connect()
            time.sleep(5)
            return wrapper(self, *args, **kwargs)
            print '重新连接数据库'
    return wrapper


def getTableDesc(pg, table_name):
    '''
    create by bigzhu at 15/03/10 10:05:45 查询表的描述
    '''
    sql = '''
        select obj_description('public.%s'::regclass)
    ''' % table_name
    data = pg.db.query(sql)
    if data:
        return data[0].obj_description


def getTableColum(pg, table_name, name=None, just_time=None):
    '''
    获取表的字段名称
    modify by bigzhu at 15/03/11 11:31:48 如果传了 name, 就只取这个 colum, 可以用来检查是否存在
    modify by bigzhu at 15/04/24 14:19:25 可以只查timestamp出来
    '''
    sql = '''
        select format_type(a.atttypid,a.atttypmod) as type,a.attname as name
        from pg_class as c,pg_attribute as a
        where c.relname = '%s' and a.attrelid = c.oid and a.attnum>0 and a.atttypid<>0
    ''' % table_name
    if name:
        sql += " and a.attname='%s'" % name
    if just_time:
        sql += " and format_type(a.atttypid,a.atttypmod)='timestamp without time zone' "
    return list(pg.db.query(sql))


def transTimeValueByTable(pg, table_name, v):
    '''
    create by bigzhu at 15/04/24 14:14:52 为了让time能 insert/update 数据库
    modify by bigzhu at 15/04/24 16:10:51 自动除以1000以应对js
    '''
    time_colums = getTableColum(pg, table_name, just_time=True)
    for time_colum in time_colums:
        name = time_colum.name
        if v.get(name):
            time = int(v[name]) / 1000
            v[name] = SQLLiteral("to_timestamp(%s)" % time)
    return v


def insertIfNotExist(pg, table_name, values, where=None):
    '''
    create by bigzhu at 15/07/09 14:08:25 如果没有时,再insert,返回id
        example: insertIfNotExist(test_pg, 'user_info', {'id':988, 'user_name':'bigzhu', 'user_type':'my'}, " id=988")
    modify by bigzhu at 15/07/09 15:18:41 where 默认None时,用id
    modify by bigzhu at 15/07/09 19:44:16 目前是用 repr 来处理内容有单引号的, 放在insert的value里没问题,但是在select里就不行了.
    modify by bigzhu at 15/07/09 20:01:36 必须要字符串拼接的方式, 转换 string 为 <class 'webpy_db.SQLQuery'>
    modify by bigzhu at 15/07/09 20:09:35 也不是转换的问题, 拼接了就可以执行,简直神奇

    '''
    def q(x):
        return "(" + x + ")"
    _keys = SQLQuery.join(values.keys(), ', ')
    _values = SQLQuery.join([sqlparam(v) for v in values.values()], ', ')

    if where is None:
        where = 'id = %s' % values['id']
    sql = " INSERT INTO %s " % table_name + q(_keys) + \
          " SELECT " + _values + \
          " WHERE NOT EXISTS (" + \
          "    SELECT id " +\
          "    FROM %s " % table_name +\
          "    WHERE %s " % where +\
          "    ) " +\
          " RETURNING id "
    sql = SQLQuery(sql)
    try:
        result = list(pg.db.query(sql))
    except Exception as e:
        print sql
        raise e

    if result:
        return result[0].id


def insertOrUpdate(pg, table_name, values, where=None):
    '''
    create by bigzhu at 15/09/03 09:15:35 insert or update
    '''
    result = insertIfNotExist(pg, table_name, values, where=where)
    if result is None:
        if where is None:
            where = 'id=%s' % (values['id'])
        count = pg.db.update(table_name, where=where, **values)
        return count
    else:
        return result


def getSeqIdByTableName(pg, table_name):
    '''
    create by bigzhu at 15/09/14 10:16:29 get seq by table_name
    '''
    seq_name = table_name + '_id_seq'
    sql = '''
    select nextval('%s') as id
    ''' % seq_name
    id = pg.db.query(sql)[0].id
    return id

if __name__ == '__main__':
    import test_pg
    print insertIfNotExist(test_pg, 'user_info', {'id': 990, 'user_name': "big'zhu", 'user_type': 'my'}, " id=990")
    # print test_pg.db.insert('user_info', _test=False, user_type='my', user_name="big'zhu")
