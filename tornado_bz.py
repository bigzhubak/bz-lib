#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
tornado 相关的公用代码
'''

import tornado
import os
import public_bz
import functools
import json
import user_bz
import db_bz
from tornado.web import RequestHandler


OK = '0'


class BaseHandler(RequestHandler):

    '''
    create by bigzhu at 15/01/29 22:53:07 自定义一些基础的方法
        设置 pg
        设定 current_user 为 cookie user_id
    modify by bigzhu at 15/01/30 09:59:46 直接返回 user_info
    modify by bigzhu at 15/01/30 10:32:37 默认返回 user_info 的拆离出去
    modify by bigzhu at 15/02/21 00:41:23 修改 js_embed 的位置到 </head> 前
    modify by bigzhu at 15/03/06 17:13:21 修改 js_file 的位置到 </head> 前
    modify by bigzhu at 15/06/28 22:37:24 让js_list用一样的次序显示,改回append
    modify by bigzhu at 15/06/28 22:39:29 为了让js_list能在最前,insert location 改为 <head>后
    modify by bigzhu at 15/09/15 10:22:27 删除对render的重载，vue现在没必要插入最前
    modify by bigzhu at 15/09/17 10:31:49 删除多余的重载，为了在lib用ui module;搞得太复杂了
    '''

    def initialize(self):
        self.pg = self.settings['pg']
        self.template = getTName(self)

    def get_current_user(self):
        return self.get_secure_cookie("user_id")


class UserInfoHandler(BaseHandler):

    '''
    create by bigzhu at 15/01/30 10:32:00 默认返回 user_info 的类单独拆离出来, 某些不需要返回 user_info 的可以继续用 base
    '''

    def get_user_info(self):
        if self.current_user:
            user_info = user_bz.UserOper(self.pg).getUserInfoById(self.current_user)
            if user_info:
                self.user_info = user_info[0]
                return self.user_info
            else:
                self.redirect("/logout")

    def get_template_namespace(self):
        ns = super(UserInfoHandler, self).get_template_namespace()
        ns.update({
            'user_info': self.get_user_info(),
        })

        return ns


def getURLMap(the_globals):
    '''
        根据定义的tornado.web.RequestHandler,自动生成url map
        modify by bigzhu at 15/03/06 15:53:59 在这里需要设置 lib 的 static, 用于访问 lib 的 static 文件
        create by bigzhu at 16/02/23 18:29:49 剔除多余的lib_static
    '''
    url_map = []
    for i in the_globals:
        try:
            if issubclass(the_globals[i], tornado.web.RequestHandler):
                url_map.append((r'/' + i, the_globals[i]))
                url_map.append((r"/%s/(.*)" % i, the_globals[i]))
        except TypeError:
            continue
    return url_map


def getAllWebBzRequestHandlers():
    all_class = {}
    import inspect
    import web_bz
    for name, cls in inspect.getmembers(web_bz):
        try:
            if issubclass(cls, RequestHandler):
                all_class[cls.__name__] = cls
        except TypeError:
            pass
    return all_class


def getSettings():
    '''
        返回 tornado 的 settings ,有一些默认值,省得每次都设置:
            debug:  True 则开启调试模式,代码自动部署,但是有语法错误,会导致程序 cash
            ui_modules 自定义的 ui 模块,默认会引入 tornado_ui_bz
            login_url: 装饰器 tornado.web.authenticated 未登录时候,重定向的网址
    '''
    settings = {
        'static_path': os.path.join(public_bz.getExecutingPath(), 'static'),
        'debug': True,
        'cookie_secret': 'bigzhu so big',
        'autoescape': None,  # 模板自定义转义
        'login_url': "/login"
    }
    return settings


def getTName(self, name=None):
    '''
    取得模板的名字
    与类名保持一致
    '''
    if name:
        return 'template/' + name + '.html'
    else:
        return 'template/' + self.__class__.__name__ + '.html'


def handleError(method):
    '''
    出现错误的时候,用json返回错误信息回去
    很好用的一个装饰器
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        try:
            method(self, *args, **kwargs)
        except Exception:
            print public_bz.getExpInfoAll()
            self.write(json.dumps({'error': public_bz.getExpInfo()}))
    return wrapper


def mustLoginApi(method):
    '''
    必须要登录 api
    create by bigzhu at 15/06/21 08:00:56
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            pass
        else:
            raise Exception('must login')
        return method(self, *args, **kwargs)
    return wrapper


def mustLogin(method):
    '''
    必须要登录,否则弹回登录页面
    很好用的一个装饰器
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            pass
        else:
            self.redirect("/login")
            return
        return method(self, *args, **kwargs)
    return wrapper


def addHits(method):
    '''
    记录某个微信用户点击的页面
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        openid = self.get_secure_cookie('openid')
        path = self.request.path
        if not openid:
            pass
        else:
            self.pg.db.insert('hits', openid=openid, path=path)
        return method(self, *args, **kwargs)
    return wrapper


def getUserId(request):
    '''
    获取当前 user_id
    未登录则为 1
    '''
    user_id = request.current_user
    if user_id:
        pass
    else:
        user_id = 1
    return user_id


class oper(BaseHandler):

    '''
    create by bigzhu at 15/04/23 16:49:57 用来操作,做一些通用的增删改
    协议说明:
        put: update
        post: insert
        get: select
        delete: delete

    参数解释:
        t: table_name
        w: where
        s: sql(完整的原始sql,太危险暂时取消)
        v: update 或者 insert 的值
        c: 记录数,要删除的记录数
    '''
    @handleError
    def get(self):
        self.set_header("Content-Type", "application/json")
        t = self.get_argument('t')
        w = self.get_argument('w', '1=1')
        order = self.get_argument('order', None)
        if order:
            data = list(self.pg.db.select(t, where=w, order=order))
        else:
            data = list(self.pg.db.select(t, where=w))

        self.write(json.dumps({'error': '0', 'data': data}, cls=public_bz.ExtEncoder))

    @handleError
    def post(self):
        '''
        create by bigzhu at 15/04/23 17:33:09 insert 返回 id
        '''
        self.set_header("Content-Type", "application/json")
        if self.current_user:
            user_id = self.current_user
        else:
            raise Exception('必须登录才能操作')

        data = json.loads(self.request.body)
        t = data.get('t')  # table
        v = data.get('v')  # value

        v = db_bz.transTimeValueByTable(self.pg, t, v)
        # 插入的值有id就update,只能udpate一条,没有就 insert
        id = v.get('id')
        if id is not None:
            w = "id=%s" % id
            trans = self.pg.db.transaction()
            count = self.pg.db.update(t, w, **v)
            if count == 1:
                trans.commit()
                self.write(json.dumps({'error': '0'}))
                return
            else:
                trans.rollback()

        seq = t + '_id_seq'
        v['user_id'] = user_id
        id = self.pg.db.insert(t, seqname=seq, **v)
        self.write(json.dumps({'error': '0', 'id': id}))

    @handleError
    def put(self):
        '''
        create by bigzhu at 15/04/23 17:33:33 udpate数据,只要value有id, 可以不写where
        '''
        self.set_header("Content-Type", "application/json")
        if self.current_user:
            pass
        else:
            raise Exception('必须登录才能操作')
        data = json.loads(self.request.body)
        t = data.get('t')  # table
        w = data.get('w')  # where
        v = data.get('v')  # value

        v = db_bz.transTimeValueByTable(self.pg, t, v)
        if w is None:
            id = v.get('id')
            if id is None:
                raise Exception('没有足够的信息来进行update操作')
            w = "id=%s" % id

        trans = self.pg.db.transaction()
        count = self.pg.db.update(t, w, **v)
        if count == 1:
            trans.commit()
        else:
            trans.rollback()
            raise Exception('不允许update %s 条记录,请检查条件' % count)

        self.write(json.dumps({'error': '0'}))

    @handleError
    def delete(self):
        '''
        create by bigzhu at 15/04/23 17:37:36 其实只是做update
        '''
        self.set_header("Content-Type", "application/json")
        if self.current_user:
            pass
        else:
            raise Exception('必须登录才能操作')
        t = self.get_argument('t')
        w = self.get_argument('w')
        c = self.get_argument('c')

        trans = self.pg.db.transaction()
        count = self.pg.db.update(t, w, is_delete=1)
        if count == int(c):
            trans.commit()
        else:
            trans.rollback()
        self.write(json.dumps({'error': '0'}))


class oper_post(BaseHandler):

    '''
    通用操作,http 协议太难用了,全用 post搞定
    create by bigzhu at 15/06/07 12:38:39
    '''
    @handleError
    def post(self):
        '''
        type: insert delete query select
        create by bigzhu at 15/06/07 12:40:20
        '''
        self.set_header("Content-Type", "application/json")
        if self.current_user:
            user_id = self.current_user
        else:
            raise Exception('必须登录才能操作')

        data = json.loads(self.request.body)
        oper_type = data.get('type')
        if oper_type == 'insert':
            v = data.get('v')
            t = data.get('t')
            v = db_bz.transTimeValueByTable(self.pg, t, v)
            # 插入的值有id就update,只能udpate一条,没有就 insert
            id = v.get('id')
            if id is not None:
                w = "id=%s" % id
                trans = self.pg.db.transaction()
                count = self.pg.db.update(t, w, **v)
                if count == 1:
                    trans.commit()
                    self.write(json.dumps({'error': OK}))
                    return
                else:
                    trans.rollback()

            seq = t + '_id_seq'
            v['user_id'] = user_id
            id = self.pg.db.insert(t, seqname=seq, **v)
            self.write(json.dumps({'error': OK, 'id': id}))
            return
        elif oper_type == 'delete':
            t = data.get('t')
            ids = data.get('ids')
            w = 'id in (%s) ' % ids
            c = data.get('c')
            trans = self.pg.db.transaction()
            count = self.pg.db.update(t, w, is_delete=1)
            if count == int(c):
                trans.commit()
            else:
                trans.rollback()
                raise Exception("按条件找到%s条,指定要删除%s条,取消删除" % (count, c))
            self.write(json.dumps({'error': '0'}))


if __name__ == '__main__':
    pass
