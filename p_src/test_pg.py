# !/usr/bin/env python
# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import webpy_db

DB_IP = '127.0.0.1'
db = None


def connect():
    global db
    db = webpy_db.database(
        port=5432,
        host=DB_IP,
        dbn='postgres',
        db='base',
        user='base',
        pw='base')
    print '开始连接数据库 %s' % DB_IP

connect()

if __name__ == '__main__':
    connect()
    pass
