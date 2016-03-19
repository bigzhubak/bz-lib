#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
发送短信模块 create by bigzhu at 16/03/19 08:34:35
'''
import top.api

appkey = '23328985'
secret = 'eb1015e6dda445cd1c84420be9e3c819'


def send(appkey, secret, rec_num, sms_param, sms_template_code, extend=None, sms_free_sign_name="大鱼测试"):
    '''
    create by bigzhu at 16/03/19 08:36:08 发送
    appkey
    secret
    extend 公共回传参数,再返回中用来判断是身份(可选)
    rec_num 接收的手机号
    sms_param 短信内容的参数
    sms_free_sign_name 签名

    '''
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey, secret))

    if extend is not None:
        req.extend = extend
    req.sms_type = "normal"
    req.sms_free_sign_name = sms_free_sign_name
    req.sms_param = sms_param
    req.rec_num = rec_num
    req.sms_template_code = sms_template_code
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)
if __name__ == '__main__':
    pass
