#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db_bz import daemonDB
import re
import hashlib
import public_bz
import model_oper_bz
import model_bz
salt = "hold is watching you"


def createTable(db_name):
    '''
    create by bigzhu at 15/04/06 20:15:55 建立 user_info 数据模型库(依赖)
    '''
    import model_oper_bz
    import model_bz
    model_oper_bz.createTable(model_bz.user_info, db_name)


class UserOper:

    '''
    对用户相关的操作
    create by bigzhu at 15/04/26 22:22:21 其实还是一个db操作合集,为了避免反复的传入 pg 参数而建立的 class
    >>> import test_pg as pg
    >>> f = UserOper(pg)
    '''

    def __init__(self, pg):
        self.pg = pg

    def getEmptyUserInfo(self):
        user_info = public_bz.storage()
        for p in model_oper_bz.getModelAttributes(model_bz.user_info):
            user_info[p] = ''
        return user_info

    @daemonDB
    def login(self, user_name, password, user_type=None):
        '''
        modify by bigzhu at 15/02/25 13:57:19 加入唯一约束
        modify by bigzhu at 15/03/08 14:24:57 加入 email; 根据 email 来判断是注册还是登录
            --登录模块,如果不存在这个用户名,则注册--
        modify by bigzhu at 15/04/24 17:49:15 注册和登录分开
        modify by bigzhu at 15/04/27 16:49:21 没有用户时提示注册
        modify by bigzhu at 15/05/17 16:12:29 密码加密放到函数内
        modify by bigzhu at 15/05/17 17:01:12 添加用户登录的测试,使用base数据库
        >>> import test_pg as pg
        >>> f = UserOper(pg)
        >>> f.login('bigzhu', 'bigzhu') #doctest:+ELLIPSIS
        <Storage {...
        '''

        password = hashlib.md5(password + salt).hexdigest()
        user_infos = self.getUserInfo(user_type=user_type, user_name=user_name)
        if not user_infos:
            user_infos = self.getUserInfo(email=user_name)
        if user_infos:
            for user_info in user_infos:
                if user_info.password == password:
                    return user_info
            raise Exception('密码错误!')
        else:
            # 前台要根据这个来弹出建议用户注册的提示,请不要修改
            raise Exception('user not exist')
        '''

        user_infos = self.getUserInfo(user_name=user_name)
        if user_infos:
            if user_infos[0].password == password:
                return user_infos[0]
            else:
                if email is None:
                    raise Exception('密码错误!')
                else:
                    raise Exception('用户已经存在!')
        else:
            if email is None:
                if len(user_name) > 7:
                    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", user_name) is not None:
                        email = user_name
            self.pg.db.insert('user_info', user_type='my', user_name=user_name, password=password, email=email)
            return self.login(user_name, password)
        '''

    @daemonDB
    def signup(self, user_name, password, email, user_type):
        password = hashlib.md5(password + salt).hexdigest()
        self.pg.db.insert('user_info', user_type=user_type, user_name=user_name, password=password, email=email)

    @daemonDB
    def getUserInfo(self, user_type=None, user_name=None, out_id=None, email=None):
        '''
        create by bigzhu at 15/04/27 10:36:01 根据条件查出用户信息
        '''
        sql = " select * from user_info where (is_delete=0 or is_delete is null)"
        if email:
            sql += " and email='%s' " % email
        if user_type:
            sql += " and user_type in (%s)" % user_type
        if user_name:
            sql += " and user_name='%s' " % user_name
        if out_id:
            sql += " and out_id='%s' " % out_id
        return list(self.pg.db.query(sql))

    @daemonDB
    def googleLogin(self, user_info):
        '''
        google 登录信息存到 db 中
            {
             "id": "112340346785758313259",
             "email": "vermiliondun@gmail.com",
             "verified_email": true,
             "name": "朱一凡",
             "given_name": "一凡",
             "family_name": "朱",
             "link": "https://plus.google.com/112340346785758313259",
             "picture": "https://lh5.googleusercontent.com/-E4rb72RaQHE/AAAAAAAAAAI/AAAAAAAAJzQ/p-tx9D78Mik/photo.jpg",
             "gender": "male",
             "locale": "zh-CN"
            }
        '''
        user_infos = self.getUserInfo(user_type="'google'", out_id=user_info['id'])
        if user_infos:
            return user_infos[0]
        else:
            self.pg.db.insert('user_info',
                              user_type='google',
                              out_id=user_info['id'],
                              email=user_info['email'],
                              user_name=user_info['name'],
                              link=user_info.get('link'),
                              picture=user_info['picture'],
                              gender=user_info['gender'],
                              locale=user_info['locale']
                              )
            return self.googleLogin(user_info)

    def mergeLogin(self, type, name):
        '''
        create by bigzhu at 15/08/05 16:24:09 根据类型来合并, 如果有同名用户, update 对应数值
        '''
        sql = '''
        select * from user_info where lower(%s)=lower('%s')
        ''' % (type, name)
        user_infos = self.pg.db.query(sql)
        if user_infos:
            return user_infos

        sql = '''
        select * from user_info where lower(user_name)=lower('%s')
        ''' % name
        user_infos = self.pg.db.query(sql)
        if user_infos:
            sql = '''
            update user_info set %s='%s' where lower(user_name)=lower('%s')
            ''' % (type, name, name)
            self.pg.db.query(sql)
            return user_infos

    @daemonDB
    def twitterLogin(self, user_info, merge=None):
        '''
        twitter 登录信息存到 db 中
        '''
        if merge:
            user_infos = self.mergeLogin('twitter', user_info['name'])
        else:
            user_infos = self.getUserInfo(user_type="'twitter'", out_id=user_info['id'])
        if user_infos:
            return user_infos[0]
        else:
            self.pg.db.insert('user_info',
                              user_type='twitter',
                              out_id=user_info['id'],
                              # email=user_info['email'],
                              user_name=user_info['username'],
                              # link=user_info['link'],
                              picture=user_info.get('profile_image_url_https'),
                              # gender=user_info['gender'],
                              #locale=user_info['profile_location']
                              locale=user_info.get('profile_location')

                              )
            return self.twitterLogin(user_info)

    @daemonDB
    def doubanLogin(self, user_info, merge=None):
        '''
        douban 登录信息存到 db 中
        '''
        if merge:
            user_infos = self.mergeLogin('douban', user_info['name'])
        else:
            user_infos = self.getUserInfo(user_type="'douban'", out_id=user_info['id'])
        if user_infos:
            return user_infos[0]
        else:
            self.pg.db.insert('user_info',
                              user_type='douban',
                              out_id=user_info.get('id'),
                              # email=user_info['email'],
                              user_name=user_info.get('name'),
                              link=user_info.get('alt'),
                              picture=user_info.get('avatar'),
                              # gender=user_info['gender'],
                              locale=user_info.get('loc_name')
                              )
            return self.doubanLogin(user_info)

    def githubLogin(self, user_info, merge=None):
        '''
        github 登录信息存到 db 中
            {
             "id": "112340346785758313259",
             "email": "vermiliondun@gmail.com",
             "name": "朱一凡",
             "link": "https://plus.google.com/112340346785758313259",
             "picture": "https://lh5.googleusercontent.com/-E4rb72RaQHE/AAAAAAAAAAI/AAAAAAAAJzQ/p-tx9D78Mik/photo.jpg",
             "locale": "zh-CN"
            }
        modify by bigzhu at 15/08/05 15:13:52 可以合并
        '''
        if merge:
            user_infos = self.mergeLogin('github', user_info['login'])
        else:
            user_infos = self.getUserInfo(user_type="'github'", out_id=user_info['id'])
        if user_infos:
            return user_infos[0]
        else:
            self.pg.db.insert('user_info',
                              user_type='github',
                              out_id=user_info['id'],
                              email=user_info['email'],
                              user_name=user_info['login'],
                              #link = user_info['html_url'],
                              picture=user_info['avatar_url'],
                              locale=user_info['location']
                              )
            return self.githubLogin(user_info)

    @daemonDB
    def resetPassword(self, user_id, old_password, new_password):
        users = self.getUserInfoById(user_id)
        if not users:
            return "该用户不存在，请重新登录"
        else:
            user = users[0]
            if user.get('password') == old_password:
                self.pg.db.update("user_info", where="id=%s" % user_id, password=new_password)
                return "0"
            else:
                return "密码错误"

    @daemonDB
    def getUserInfoById(self, user_id):
        users = list(self.pg.db.select("user_info", where="id=%s" % user_id, limit=1))
        return users


if __name__ == '__main__':
    pass
