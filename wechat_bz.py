#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by bigzhu at 15/04/01 13:30:11  微信相关的操作和接口
modify by bigzhu at 15/04/01 16:18:35  修改为依赖 pip install wechat-sdk 的版本,简化代码
'''

try:
    import requests
except ImportError:
    print 'you need run:'
    print 'sudo pip install requests'
    raise

try:
    from wechat_sdk import WechatBasic
    from wechat_sdk.basic import OfficialAPIError
except ImportError:
    print 'you need run:'
    print 'sudo pip install wechat_sdk'
    raise

import functools
import public_bz


def getUserAccessToken(code, appid, secret):
    """
    create by bigzhu at 15/04/07 16:52:40 从以前的 weixin 项目搬过来的..用于网页获取用户 openid
        根据 code 返回用户 oauth2 access token

    """
    params = {
        "appid": appid,
        "secret": secret,
        "code": code,
        "grant_type": "authorization_code"
    }

    return requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", params=params).json()


def callPlatform(self, url):
    '''
    create by bigzhu at 15/04/07 15:08:27 把对平台的访问,转发到平台上
    '''
    print self.request.body
    signature = self.get_argument('signature')
    timestamp = self.get_argument('timestamp')
    nonce = self.get_argument('nonce')
    #url = 'http://admin.hoywe.com/api.php?hash=WD13B&signature=%s&timestamp=%s&nonce=%s' %(signature, timestamp, nonce)
    url = '%s&signature=%s&timestamp=%s&nonce=%s' % (url, signature, timestamp, nonce)
    r = requests.post(url, data=self.request.body)
    return r.text


def initWechat(settings):
    '''
    create by bigzhu at 15/05/18 14:42:20 初始化wechat,获取必要的信息,返回 settings
    >>> initWechat({'token':'jhxh4lkwscelseyumc4jmoymmqkz1le1', 'appid':'wx2427206f53ca5191', 'appsecret':'96c12db489bf34bddc5b8929f2745937'}) #doctest:+ELLIPSIS
    new access_token= ...
    ({'access_token_expires_at': 1..., 'access_token': u'...', 'jsapi_ticket': u'...', 'appsecret': '96c12db489bf34bddc5b8929f2745937', 'token': 'jhxh4lkwscelseyumc4jmoymmqkz1le1', 'appid': 'wx2427206f53ca5191', 'jsapi_ticket_expires_at': ...}, <wechat_sdk.basic.WechatBasic object at ...>)
    '''

    wechat = WechatBasic(token=settings["token"],
                         appid=settings["appid"],
                         appsecret=settings["appsecret"])
    token = wechat.get_access_token()
    settings['access_token'] = token['access_token']
    settings['access_token_expires_at'] = token['access_token_expires_at']

    ticket_info = wechat.get_jsapi_ticket()
    settings['jsapi_ticket'] = ticket_info['jsapi_ticket']
    settings['jsapi_ticket_expires_at'] = ticket_info['jsapi_ticket_expires_at']
    print 'new access_token=', settings['access_token']
    return settings, wechat


def tokenHandler(method):
    '''
    create by bigzhu at 15/04/20 12:58:17 解决微信token模名失效的问题
    modify by bigzhu at 15/05/18 14:51:18 改用统一的初始化方法
    '''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except OfficialAPIError:
            print public_bz.getExpInfoAll()
            settings, self.wechat = initWechat(self.settings)
            return method(self, *args, **kwargs)
    return wrapper


if __name__ == '__main__':
    pass
