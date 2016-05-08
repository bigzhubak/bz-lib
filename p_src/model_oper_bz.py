#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by bigzhu at 15/04/03 17:23:47 初始化数据库
create by bigzhu at 15/04/03 17:23:35 字段映射参见 http://peewee.readthedocs.org/en/latest/peewee/models.html
modify by bigzhu at 15/04/06 20:09:43 修改文件名称为 model_oper_bz.py
modify by bigzhu at 15/04/08 15:05:36 改用 PostgresqlExtDatabase 为了支持 json
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import public_bz
host = 'mygit'
# host='127.0.0.1'
try:
    #from peewee import PostgresqlDatabase
    from peewee import Model
    from playhouse.postgres_ext import PostgresqlExtDatabase
    import peewee
except ImportError:
    print 'you need install peewee, please run:'
    print 'sudo pip install peewee'
    exit(1)

from model_bz import base
import inspect


def getModelAttributes(model):
    '''
    create by bigzhu at 15/07/11 22:31:50
        获取model里的属性名
    用来构造空的storage 对象
    '''
    attributes = inspect.getmembers(model, lambda a: not(inspect.isroutine(a)))
    return [a[0] for a in attributes if not(a[0].startswith('_') or a[0] in ['DoesNotExist', 'dirty_fields'])]


def reCreateTable(the_model, db_name, user=None, password=None, host=None):
    '''
    重建表
    create by bigzhu at 15/07/04 14:30:22
    '''
    dropTable(the_model, db_name, user, password, host)
    createTable(the_model, db_name, user, password, host)


def dropTable(Model, db_name, user=None, password=None, host='127.0.0.1'):
    '''
    create by bigzhu at 15/04/04 13:12:02 还是需要一个删除表的功能
    '''
    if user is None:
        user = db_name
    if password is None:
        password = db_name
    if host is None:
        host = '127.0.0.1'

    #db = PostgresqlDatabase(db_name, user=user, password=password, host='127.0.0.1')
    #db = PostgresqlExtDatabase(db_name, user=user, password=password, host='127.0.0.1', register_hstore=False)
    db = PostgresqlExtDatabase(db_name, user=user, password=password, host=host, register_hstore=False)
    Model._meta.database = db
    try:
        Model.drop_table(True)
    except peewee.OperationalError:
        print public_bz.getExpInfo()
        showDBCreate(db_name)
        exit(1)
    print 'drop table ' + Model.__name__


def createTable(Model, db_name, user=None, password=None, host='127.0.0.1'):
    '''
    create by bigzhu at 15/04/04 01:08:30 建立数据库表; peewee 要在定义时候指定 db 相当不人性化,修正
    modify by bigzhu at 15/04/04 01:32:46 没有这个数据库的时候,直接返回建立数据的语句
    modify by bigzhu at 15/04/04 01:45:43 如果表已经存在,不能往下继续了
    '''
    if user is None:
        user = db_name
    if password is None:
        password = db_name
    if host is None:
        host = '127.0.0.1'

    #db = PostgresqlExtDatabase(db_name, user=user, password=password, host='127.0.0.1', register_hstore=False)
    db = PostgresqlExtDatabase(db_name, user=user, password=password, host=host, register_hstore=False)
    Model._meta.database = db
    try:
        if Model.table_exists():
            print 'table %s already exists' % Model.__name__
            return
        createBaseTable(db)
        Model.create_table()
        print 'create table ' + Model.__name__
    except peewee.OperationalError:
        print public_bz.getExpInfo()
        showDBCreate(db_name)
        exit(1)

    table_name = Model.__name__
    if table_name != 'base':
        sql = '''
            alter table %s inherit base;
            ''' % table_name
        db.execute_sql(sql)
        resetBaseDefault(db)
        # add table comment
        comment = Model.__doc__
        sql = '''
            COMMENT ON TABLE %s IS '%s';
        ''' % (table_name, comment)
        db.execute_sql(sql)


def resetBaseDefault(db):
    '''
    create by bigzhu at 15/04/04 01:25:45 强制重新设置的 base 的 default, 保证新建立的表也是 default
    '''
    sql = '''
        alter table base
           alter column created_date set default now();
        alter table base
           alter column stat_date set default now();
        alter table base
           alter column is_delete set default 0;
    '''
    db.execute_sql(sql)


def showDBCreate(db_name):
    '''
    create by bigzhu at 15/04/04 01:20:33 根据名字拼装出建立数据库及用户的语句
    '''
    sql = '''
        create role %s login encrypted password '%s' noinherit valid until 'infinity';
        create database %s with encoding='utf8' owner=%s;
    ''' % (db_name, db_name, db_name, db_name)
    print sql


def createBaseTable(db):
    '''
    create by bigzhu at 15/04/04 01:39:26 建立 base 表
    '''
    from model_bz import base
    base._meta.database = db
    base.create_table(True)


def createAllTable(all_class, db_name, user=None, password=None, host=None):
    #all_class = globals().copy()
    for model in all_class:
        try:
            if issubclass(all_class[model], Model):
                createTable(all_class[model], db_name, user, password, host)
        except Exception:
            continue


def reCreateAllTable(all_class, db_name, user=None, password=None, host=None):
    '''
    建立全部的 model create by bigzhu at 15/07/11 17:40:10
    '''

    for model in all_class:
        try:
            if issubclass(all_class[model], Model):
                print model
                reCreateTable(all_class[model], db_name, user=user, password=password, host=host)
        except Exception:
            continue


if __name__ == '__main__':
    pass
    # createAllTable(pg_db)
