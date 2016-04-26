#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by bigzhu at 15/09/14 09:59:05
这里放所有公用的tornado的web class
    用于暴露到url，因此class name用_分割，不用驼峰法
'''
import tornado.web
import tornado_bz
import json
import hashlib
import user_bz
import public_bz
import db_bz
import tornado_auth_bz
import wechat_bz
import oper_bz

from tornado_bz import UserInfoHandler
from tornado_bz import BaseHandler
from public_bz import storage

salt = "hold is watching you"

md5 = hashlib.md5()


class api_login(UserInfoHandler):

    '''
    登录后台的方法
    modify by bigzhu at 16/03/07 22:52:33 改为单纯的登录
    '''

    @tornado_bz.handleError
    def post(self):
        self.set_header("Content-Type", "application/json")
        login_info = json.loads(self.request.body)
        user_name = login_info.get("user_name")
        password = login_info.get("password")
        user_oper = user_bz.UserOper(self.pg)
        user_info = user_oper.login(user_name, password)
        self.set_secure_cookie("user_id", str(user_info.id))
        self.write(json.dumps({'error': '0'}))


class api_signup(UserInfoHandler):

    @tornado_bz.handleError
    def post(self):
        self.set_header("Content-Type", "application/json")
        login_info = json.loads(self.request.body)

        user_name = login_info.get("user_name")
        password = login_info.get("password")
        email = login_info.get("email")

        user_oper = user_bz.UserOper(self.pg)
        # 用户是否存在应该注册提交前判断?以后优化
        user_info = user_oper.getUserInfo(user_name=user_name)
        if user_info:
            raise Exception('用户已经存在, 请换一个用户名')
        user_info = user_oper.getUserInfo(email=email)
        if user_info:
            raise Exception('邮箱已经被使用, 请更换一个邮箱')

        user_type = login_info.get("user_type", 'my')

        user_oper.signup(user_name, password, email, user_type)
        user_info = user_oper.login(user_name, password, "'%s'" % user_type)
        self.set_secure_cookie("user_id", str(user_info.id))
        self.write(json.dumps({'error': '0'}))


class api_user_info(BaseHandler):

    @tornado_bz.handleError
    def get(self):
        self.set_header("Content-Type", "application/json")
        user_id = self.get_secure_cookie("user_id")
        if not user_id:
            raise Exception('没有登录')
        user_oper = user_bz.UserOper(self.pg)
        user_info = user_oper.getUserInfo(user_id=user_id)
        if not user_info:
            raise Exception('没有用户' + user_id)
        user_info = user_info[0]
        del user_info.password
        self.write(json.dumps({'error': '0', 'user_info': user_info}, cls=public_bz.ExtEncoder))
    @tornado_bz.handleError
    def put(self):
        self.set_header("Content-Type", "application/json")
        data = json.loads(self.request.body)
        user_name = data.get('user_name')
        if user_name == '' or user_name is None:
            raise Exception('必须有用户名才能修改')
        oper_bz.checkSocialData(self.pg, data, 'twitter')
        oper_bz.checkSocialData(self.pg, data, 'github')
        oper_bz.checkSocialData(self.pg, data, 'tumblr')
        oper_bz.checkSocialData(self.pg, data, 'instagram')

        where = "user_name='%s'" % data['user_name']
        db_bz.insertOrUpdate(self.pg, 'user_info', data, where)
        self.write(json.dumps({'error': '0'}, cls=public_bz.ExtEncoder))


class set_openid(BaseHandler):

    """
    微信获取不到openid时, 访问获取信息的页面后的回调页面
    """

    def get(self):
        print 'call setOpenId'
        url = self.get_argument('url')
        code = self.get_argument('code')
        user_access_token = wechat_bz.getUserAccessToken(code, self.settings["appid"], self.settings["appsecret"])

        openid = user_access_token.get("openid")
        if openid is None:
            print json.dumps(user_access_token)
            print 'code= %s url=%s' % (code, url)
            error = '''
            <html>
                <script type="text/javascript">
                alert("微信服务器异常，请关闭后，重新打开");
                WeixinJSBridge.call('closeWindow');
                </script>
            </html>
            '''
            self.write(error)
            return

        self.set_secure_cookie("openid", str(openid))
        self.redirect(url)


class file_upload_bz(BaseHandler):

    '''
    create by bigzhu at 15/09/11 11:38:52
    文件上传相关API
    '''
    @tornado_bz.handleError
    def post(self):
        '''
        新增文件
        '''
        self.set_header("Content-Type", "application/json")
        key = self.get_argument("key")
        if self.request.files:
            for i in self.request.files:
                fd = self.request.files[i]
                for f in fd:
                    file_name = f.get("filename")
                    file_body = f["body"]
                    md5.update(file_body)
                    file_hash = md5.hexdigest()
                    file_path = "static/uploaded_files/%s.%s" % (file_hash, file_name)
                    img = open(file_path, 'w')
                    img.write(file_body)
                    img.close()
                    file_id = self.pg.db.insert("uploaded_files_bz", key=key, file_name=file_name, path='/' + file_path)
        self.write(json.dumps({'error': '0', 'id': file_id}))


class remove_exist_file(BaseHandler):

    '''
    create by bigzhu at 15/09/11 17:38:32 删除某个文件
    '''
    @tornado_bz.handleError
    def post(self):
        '''
        新增文件
        '''
        self.set_header("Content-Type", "application/json")
        data = json.loads(self.request.body)
        id = data.get('id')
        count = self.pg.db.update('uploaded_files_bz', where="id=%s" % id, is_delete=1)
        if count != 1:
            raise Exception('id=%s, count=%' % (id, count))
        self.write(json.dumps({'error': '0'}, cls=public_bz.ExtEncoder))


class get_exist_files(BaseHandler):

    '''
    create by bigzhu at 15/09/11 12:41:52 取文件列表
    '''
    @tornado_bz.handleError
    def post(self):
        '''
        新增文件
        '''
        self.set_header("Content-Type", "application/json")
        data = json.loads(self.request.body)
        key = data.get('key')
        files = list(self.pg.db.select('uploaded_files_bz', where="key='%s' and (is_delete=0 or is_delete is null)" % key))
        self.write(json.dumps({'error': '0', 'files': files}, cls=public_bz.ExtEncoder))


class seq(BaseHandler):

    '''
    取某个表的seq
    '''

    @tornado_bz.handleError
    def post(self):
        self.set_header("Content-Type", "application/json")
        data = json.loads(self.request.body)
        table_name = data.get("table_name")
        id = db_bz.getSeqIdByTableName(self.pg, table_name)
        self.write(json.dumps({'error': '0', 'id': id}))


class login(UserInfoHandler):

    '''
    登录后台的方法
    '''

    def initialize(self):
        '''
        针对 oauth2 ,需要你重载的时候来设置为你自己的参数, 以下是 google twitter douban 的例子
        modify by bigzhu at 15/04/26 21:56:09 对应的oauth登录的参数,应该在对应的oauth里面来设置,这里不用再设置了
        create by bigzhu at 15/06/29 10:48:00 只要纯粹的login
        '''

        UserInfoHandler.initialize(self)
        oauth2 = storage()
        oauth2.google = storage(enabled=False, url='/google')
        oauth2.twitter = storage(enabled=False, url='/twitter')
        oauth2.douban = storage(enabled=False, url='/douban')
        oauth2.github = storage(enabled=False, url='/github')
        self.oauth2 = oauth2

        # 用户操作相关的
        self.user_oper = user_bz.UserOper(self.pg)
        # 是否要验证
        self.validate = False

        # salt
        self.salt = salt

    def get(self):
        self.render(self.template, oauth2=self.oauth2)

    @tornado_bz.handleError
    def post(self):
        self.set_header("Content-Type", "application/json")
        login_info = json.loads(self.request.body)
        user_name = login_info.get("user_name")
        password = login_info.get("password")
        user_info = self.user_oper.login(user_name, password)
        self.set_secure_cookie("user_id", str(user_info.id))
        self.write(json.dumps({'error': '0'}))

    @tornado_bz.handleError
    def put(self):
        self.set_header("Content-Type", "application/json")
        reset_data = json.loads(self.request.body)
        user_id = self.get_secure_cookie("user_id")
        old_password = reset_data.get("old_password")
        new_password = reset_data.get("new_password")
        # 加密
        hashed_old_pwd = hashlib.md5(old_password + salt).hexdigest()
        hashed_new_pwd = hashlib.md5(new_password + salt).hexdigest()
        error_msg = self.user_oper.resetPassword(user_id, hashed_old_pwd, hashed_new_pwd)
        self.write(json.dumps({'error': error_msg}, cls=public_bz.ExtEncoder))


class signup(UserInfoHandler):

    def initialize(self):
        UserInfoHandler.initialize(self)
        self.user_oper = user_bz.UserOper(self.pg)

    def get(self):
        self.render(tornado_bz.getTName(self))

    @tornado_bz.handleError
    def post(self):
        self.set_header("Content-Type", "application/json")
        login_info = json.loads(self.request.body)

        user_name = login_info.get("user_name")
        password = login_info.get("password")
        email = login_info.get("email")
        # 用户是否存在应该注册提交前判断,这里再次判断
        user_info = self.user_oper.getUserInfo(user_name=user_name)
        if user_info:
            raise Exception('用户已经存在, 请换一个用户名')
        user_info = self.user_oper.getUserInfo(email=email)
        if user_info:
            raise Exception('邮箱已经被使用, 请更换一个邮箱')

        user_type = login_info.get("user_type", 'my')

        self.user_oper.signup(user_name, password, email, user_type)
        user_info = self.user_oper.login(user_name, password, "'%s'" % user_type)
        self.set_secure_cookie("user_id", str(user_info.id))
        self.write(json.dumps({'error': '0'}))


class logout(BaseHandler):

    @tornado_bz.handleError
    def get(self):
        self.clear_cookie(name='user_id')
        self.redirect("/")


class get_user_info(BaseHandler):

    @tornado_bz.handleError
    def get(self):
        self.set_header("Content-Type", "application/json")
        user_id = self.get_secure_cookie("user_id")
        print user_id
        if not user_id:
            self.write(json.dumps({'error': '没有登录'}, cls=public_bz.ExtEncoder))
        else:
            user_oper = user_bz.UserOper(self.pg)
            user_info = user_oper.getUserInfo(user_id=user_id)
            if not user_info:
                raise Exception('没有用户' + user_id)
            user_info = user_info[0]
            del user_info.password
            self.write(json.dumps({'error': '0', 'user_info': user_info}, cls=public_bz.ExtEncoder))


class google(BaseHandler, tornado.auth.GoogleOAuth2Mixin):

    '''
    显而易见, google 登录
    '''

    def initialize(self):
        BaseHandler.initialize(self)

    @tornado.gen.coroutine
    def get(self):
        redirect_uri = self.settings['google_oauth']['redirect_uri']
        if self.get_argument('code', False):
            user = yield self.get_authenticated_user(
                redirect_uri=redirect_uri,
                code=self.get_argument('code')
            )
            self.user = user
            user_info = self.getUserInfo()
            self.user_oper = user_bz.UserOper(self.pg)
            user_info = self.user_oper.googleLogin(user_info)
            self.set_secure_cookie("user_id", str(user_info.id))
            self.redirect("/")
            # Save the user with e.g. set_secure_cookie
        else:
            yield self.authorize_redirect(
                redirect_uri=redirect_uri,
                client_id=self.settings['google_oauth']['key'],
                scope=['profile', 'email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})

    def getUserInfo(self):
        token = self.user.get('access_token')
        import requests

        response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=%s' % token)
        return response.json()


class twitter(BaseHandler, tornado.auth.TwitterMixin):

    def initialize(self):
        BaseHandler.initialize(self)
        self.merge = None

    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("oauth_token", None):
            user_info = yield self.get_authenticated_user()

            self.user_oper = user_bz.UserOper(self.pg)
            user_info = self.user_oper.twitterLogin(user_info, self.merge)
            self.set_secure_cookie("user_id", str(user_info.id))
            self.redirect("/")

            # Save the user using e.g. set_secure_cookie()
        else:
            yield self.authorize_redirect()


class github(BaseHandler, tornado_auth_bz.GithubOAuth2Mixin):

    '''
    modify by bigzhu at 15/08/05 15:11:14 merge 用来判断是否和同名用户合并
    '''

    def initialize(self):
        BaseHandler.initialize(self)
        self.merge = None

    @tornado.gen.coroutine
    def get(self):
        # if we have a code, we have been authorized so we can log in
        if self.get_argument("code", False):
            user = yield self.get_authenticated_user(
                redirect_uri=self.settings['github_oauth']['redirect_uri'],
                client_id=self.settings['github_oauth']['client_id'],
                client_secret=self.settings['github_oauth']['client_secret'],
                code=self.get_argument("code"),
                extra_fields="user:email"
            )

            self.user_oper = user_bz.UserOper(self.pg)
            user_info = self.user_oper.githubLogin(user, self.merge)
            self.set_secure_cookie('user_id', str(user_info.id))
            self.redirect('/')

        else:
            yield self.authorize_redirect(
                redirect_uri=self.settings['github_oauth']['redirect_uri'],
                client_id=self.settings['github_oauth']['client_id'],
                extra_params={
                    "scope": "user:email",
                }
            )


class douban(BaseHandler, tornado_auth_bz.DoubanOAuth2Mixin):

    def initialize(self):
        BaseHandler.initialize(self)

    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('code', False):
            # 获取到个人信息
            user = yield self.get_authenticated_user(
                redirect_uri=self.settings['redirect_uri'],
                code=self.get_argument('code')
            )
            if user:
                self.user_oper = user_bz.UserOper(self.pg)
                user_info = self.user_oper.doubanLogin(user, self.merge)
                self.set_secure_cookie("user_id", str(user_info.id))
                self.redirect("/")

                # self.set_secure_cookie("user_id", str(user['uid']))
                # self.redirect(self.get_argument("next", "/"))
        else:
            yield self.authorize_redirect(
                redirect_uri=self.settings['redirect_uri'],
                client_id=self.settings['douban_api_key'],
                scope=None,  # 使用默认的scope权限
                response_type='code'
            )

if __name__ == '__main__':
    pass
