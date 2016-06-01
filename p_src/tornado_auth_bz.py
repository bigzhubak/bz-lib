#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
基于 Oauth2 的登录
'''
import tornado.httputil
import tornado.httpclient
import tornado.web
import tornado.gen
import urllib
import logging
import functools

from tornado.auth import AuthError
from tornado.auth import OAuth2Mixin
from tornado.auth import _auth_return_future
from tornado.concurrent import return_future
from tornado import escape

from tornado import httpclient


from tornado.httputil import url_concat
from tornado import gen
import re


class QQAuth2Minix(OAuth2Mixin):

    """docstring for QQAuth2Minix"""
    _OAUTH_OPEND_API = "https://graph.qq.com"
    _OAUTH_AUTHORIZE_URL = "https://graph.qq.com/oauth2.0/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "https://graph.qq.com/oauth2.0/token"
    _OAUTH_OPEND_ID_URL = "https://graph.qq.com/oauth2.0/me"
    _OAUTH_NO_CALLBACKS = False

    def authorize_redirect(self, redirect_uri=None, client_id=None,
                           client_secret=None, extra_params=None):
        """调用父类方法跳转认证获取code, QQ认证需要加入
           参数response_type:(code)和state所以作为附加参数传递给父类方法"""
        args = {
            "response_type": "code",
            "state": "authorize",
        }
        logging.warn("redirect: " + str(args))
        if extra_params:
            args.update(extra_params)
        super(QQAuth2Minix, self).authorize_redirect(redirect_uri, client_id,
                                                     client_secret, args)

    @gen.engine
    def get_authenticated_user(self, redirect_uri, client_id, client_secret,
                               code, callback, extra_fields=None):
        """获取用户的token和openId, 并传入回调函数"""
        http = self.get_auth_http_client()
        args = {
            "redirect_uri": redirect_uri,
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "extra_params": {
                "grant_type": "authorization_code"
            }
        }
        response = yield gen.Task(http.fetch, self._oauth_request_token_url(**args))
        self._on_access_token(redirect_uri, client_id,
                              client_secret, callback, response)

    @gen.engine
    def _on_access_token(self, redirect_uri, client_id, client_secret,
                         callback, response):
        if response.error:
            logging.warning('QQ auth error: %s' % str(response))
            callback(None)
            return
        args = escape.parse_qs_bytes(escape.native_str(response.body))
        session = {
            "access_token": args["access_token"][-1],
            "expires": args.get("expires_in")[0]
        }
        http = self.get_auth_http_client()
        response = yield gen.Task(http.fetch, url_concat(self._OAUTH_OPEND_ID_URL, {"access_token": session["access_token"]}))
        self._on_open_id(redirect_uri, client_id,
                         client_secret, callback, session, response)

    def _on_open_id(self, redirect_uri, client_id, client_secret,
                    callback, session, response):
        if response.error:
            logging.warning('QQ get openId error: %s' % str(response))
            callback(None)
            return
        res_json = re.match(r".*?\((.*?)\)", escape.native_str(response.body)).group(1)
        args = escape.json_decode(res_json)
        session.update(args)
        callback(session)

    @gen.engine
    def qq_request(self, path, method, open_id, token, client_id, callback, **args):
        """调用QQ API接口, path需要传绝对路径"""
        params = {
            "access_token": token,
            "oauth_consumer_key": client_id,
            "openid": open_id
        }
        params.update(args)
        url = self._OAUTH_OPEND_API + path
        http = self.get_auth_http_client()
        if "POST" == method:
            response = yield gen.Task(http.fetch, url, method=method, body=urllib.urlencode(params))
            self._on_qq_request(callback, response)
        else:
            url = url_concat(url, params)
            response = yield gen.Task(http.fetch, url)
            self._on_qq_request(callback, response)

    def _on_qq_request(self, callback, response):
        if response.error:
            logging.warning("Error response %s fetching %s", response.error,
                            response.request.url)
            callback(None)
            return
        callback(escape.native_str(response.body))

    def get_auth_http_client(self):
        """Returns the AsyncHTTPClient instance to be used for auth requests.

        May be overridden by subclasses to use an http client other than
        the default.
        """
        return httpclient.AsyncHTTPClient()


class DoubanMixin(object):

    @return_future
    def authorize_redirect(self, redirect_uri=None, client_id=None,
                           client_secret=None, extra_params=None,
                           callback=None, scope=None, response_type="code"):
        args = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'response_type': response_type
        }
        if scope:
            args['scope'] = ' '.join(scope)

        self.redirect(
            tornado.httputil.url_concat(self._OAUTH_AUTHORIZE_URL, args))  # 跳转到认证页面
        callback()

    def _oauth_request_token_url(self, redirect_uri=None, client_id=None, client_secret=None, code=None):
        url = self._OAUTH_ACCESS_TOKEN_URL
        args = dict(
            client_id=client_id,
            redirect_uri=redirect_uri,
            client_secret=client_secret,
            grant_type="authorization_code",
            code=code
        )
        return tornado.httputil.url_concat(url, args)


class DoubanOAuth2Mixin(DoubanMixin):
    _OAUTH_ACCESS_TOKEN_URL = 'https://www.douban.com/service/auth2/token'
    _OAUTH_AUTHORIZE_URL = 'https://www.douban.com/service/auth2/auth?'

    def get_auth_http_client(self):
        return tornado.httpclient.AsyncHTTPClient()

    @_auth_return_future
    def get_authenticated_user(self, redirect_uri, code, callback):
        http = self.get_auth_http_client()
        body = urllib.urlencode({
            'redirect_uri': redirect_uri,
            'code': code,
            'client_id': self.settings['douban_api_key'],
            'client_secret': self.settings['douban_api_secret'],
            "grant_type": "authorization_code",
        })

        http.fetch(self._OAUTH_ACCESS_TOKEN_URL, functools.partial(self._on_access_token, callback),
                   method="POST", body=body, user_agent="Etherpy")

    def _on_access_token(self, future, response):
        if response.error:
            future.set_exception(AuthError('Douban Auth Error: %s' % str(response)))
            return
        args = escape.json_decode(response.body)
        # future.set_result(args)
        self.get_user_info(access_token=args['access_token'],
                           callback=functools.partial(self._on_get_user_info, future))

    def _on_get_user_info(self, future, user):
        if user is None:
            future.set_result(None)
            return
        future.set_result(user)

    @_auth_return_future
    def get_user_info(self, access_token, callback):
        url = 'https://api.douban.com/v2/user/~me'
        http = tornado.httpclient.AsyncHTTPClient()
        req = tornado.httpclient.HTTPRequest(url, headers={"Authorization": "Bearer " + access_token})
        http.fetch(req, functools.partial(self._on_get_user_request, callback))

    def _on_get_user_request(self, future, response):
        if response.error:
            future.set_exception(AuthError('Error response fetching',
                                           response.error, response.request.url))
            return
        future.set_result(escape.json_decode(response.body))


class GithubOAuth2Mixin(OAuth2Mixin):

    """Github authentication using OAuth2"""

    _OAUTH_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
    _OAUTH_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
    _OAUTH_NO_CALLBACKS = False
    _GITHUB_BASE_URL = "https://api.github.com"

    @_auth_return_future
    def get_authenticated_user(self, redirect_uri, client_id, client_secret,
                               code, callback, extra_fields=None):
        http = tornado.httpclient.AsyncHTTPClient()
        args = {
            "redirect_uri": redirect_uri,
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        fields = set(["id", "login", "name", "email",
                      "location", "url", "gists_url",
                      "avatar_url", "gravatar_id",
                      "blog", ])
        if extra_fields:
            fields.update(extra_fields)

        http.fetch(self._oauth_request_token_url(**args),
                   functools.partial(self._on_access_token, redirect_uri,
                                     client_id, client_secret, callback,
                                     fields))

    def _on_access_token(self, redirect_uri, client_id, client_secret,
                         future, fields, response):
        if response.error:
            future.set_exception(
                AuthError("Github auth error: %s" % str(response)))
            return
        logging.info("response: %r" % response)
        logging.info("response.body: %r" % response.body)
        args = escape.parse_qs_bytes(escape.native_str(response.body))
        logging.info("args: %r" % args)
        session = {
            "access_token": args['access_token'][0],
            "expires": args.get("expires"),
        }

        logging.info("session: %s" % session)
        self.github_request(
            path="/user",
            callback=functools.partial(self._on_get_user_info,
                                       future, session, fields),
            access_token=session['access_token'],
            fields=",".join(fields)
        )

    def _on_get_user_info(self, future, session, fields, user):
        if user is None:
            future.set_result(None)
            return
        logging.info("session: %r" % session)
        fieldmap = {}
        for field in fields:
            fieldmap[field] = user.get(field)

            fieldmap.update(
                {
                    "access_token": session['access_token'],
                    "session_expires": session.get("expires"),
                }
            )
        logging.info("fieldmap: %r" % fieldmap)
        logging.info("fields: %r" % fields)
        logging.info("user: %r" % user)
        future.set_result(fieldmap)

    @_auth_return_future
    def github_request(self, path, callback, access_token=None,
                       post_args=None, **args):
        url = self._GITHUB_BASE_URL + path
        all_args = {}
        if access_token:
            all_args['access_token'] = access_token
            all_args.update(args)

        if all_args:
            url += "?" + urllib.urlencode(all_args)
        callback = functools.partial(self._on_github_request, callback)
        http = tornado.httpclient.AsyncHTTPClient()
        logging.info("http connection: %s" % http)
        if post_args is not None:
            http.fetch(url, method="POST", body=urllib.urlencode(post_args),
                       callback=callback)
        else:
            http.fetch(url, callback=callback, user_agent="Etherpy")

    def _on_github_request(self, future, response):
        if response.error:
            future.set_exception(AuthError("Error response: %s" % response,
                                           response.error,
                                           response.request.url,
                                           response.body))
            return
        future.set_result(escape.json_decode(response.body))

if __name__ == '__main__':
    pass
