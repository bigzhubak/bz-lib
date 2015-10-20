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
import urllib
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
        #self.pg = self.settings['pg']
        self.template = getTName(self)

    def get_current_user(self):
        return self.get_secure_cookie("user_id")


def getURLMap(the_globals):
    '''
        根据定义的tornado.web.RequestHandler,自动生成url map
        modify by bigzhu at 15/03/06 15:53:59 在这里需要设置 lib 的 static, 用于访问 lib 的 static 文件
    '''
    url_map = []
    for i in the_globals:
        try:
            if issubclass(the_globals[i], tornado.web.RequestHandler):
                url_map.append((r'/' + i, the_globals[i]))
                url_map.append(
                    (r'/lib_static/(.*)', tornado.web.StaticFileHandler, {'path': public_bz.getLibPath() + "/static"})
                )
                # url_map.append((r"/%s/([0-9]+)" % i, the_globals[i]))
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
            print(public_bz.getExpInfoAll())
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


def mustSubscribe(method):
    '''
    create by bigzhu at 15/04/08 10:25:59 wechat 使用,必须要关注
    '''
    #from wechat_sdk import WechatBasic
    from wechat_sdk.basic import OfficialAPIError

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        openid = self.get_secure_cookie("openid")
        if openid is None:
            # 连openid 都没有,首先要获取 openid
            params = {
                "appid": self.settings['appid'],
                # "redirect_uri": "http://" + self.settings['domain'] + "/setOpenid?url=/" + self.__class__.__name__,
                # "redirect_uri": "http://" + self.settings['domain'] + "/setOpenid?url=" + self.request.uri,
                "redirect_uri": "http://" + "admin.hoywe.com/" + self.settings['suburl'] + "/?url=" + self.request.uri,
                "response_type": "code",
                "scope": "snsapi_base",
            }
            auth_url = "https://open.weixin.qq.com/connect/oauth2/authorize?%s#wechat_redirect"
            auth_url = auth_url % urllib.urlencode(params)
            self.redirect(auth_url)
            return
        else:
            #exists_users = list(self.pg.db.select('wechat_user', where="openid='%s'" % openid))
            # if not exists_users:
            try:
                wechat_user_info = self.wechat.get_user_info(openid, lang='zh_CN')
            except OfficialAPIError as e:
                print(public_bz.getExpInfoAll())
                self.clear_cookie(name='openid')
                error = public_bz.getExpInfo()
                if error.find('40001') != -1:
                    raise e
                else:
                    error_info = '''
                    <html>
                        <script type="text/javascript">
                        alert("微信服务器异常，请关闭后，重新打开");
                        WeixinJSBridge.call('closeWindow');
                        </script>
                    </html>
                    '''
                    self.write(error_info)
                return

            # 没有关注的,跳转到配置的关注页面
            if wechat_user_info['subscribe'] == 0:
                self.redirect('http://' + self.settings["domain"] + self.settings["subscribe"])
                return
            # else:
            #    print 'add user'
            #    self.pg.db.insert('wechat_user', **wechat_user_info)

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


if __name__ == '__main__':
    pass
