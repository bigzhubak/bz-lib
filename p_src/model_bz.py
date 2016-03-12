#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by bigzhu at 15/04/06 20:13:37 存放公用的数据模型
'''
from peewee import TextField
from peewee import IntegerField
from peewee import DateTimeField
from peewee import Model
from playhouse.postgres_ext import JSONField


class base(Model):
    created_date = DateTimeField(null=True)
    stat_date = DateTimeField(null=True)
    is_delete = IntegerField(null=True, default=0)
    user_id = IntegerField(null=True)


class user_info(base):

    '''用户表'''
    '''
    modify by bigzhu at 15/04/28 11:29:24 加入forget_token
    '''
    user_type = TextField(null=True)  # 用户类型 google my twitter
    out_id = TextField(null=True)  # oauth2 的外部 id
    email = TextField(null=True)  # email 地址
    user_name = TextField()  # 用户名
    link = TextField(null=True)  # 链接
    picture = TextField(null=True)  # 头像地址
    gender = TextField(null=True)  # ?
    locale = TextField(null=True)  # 所在区域
    password = TextField(null=True)  # 密码
    original_json = TextField(null=True)  # ?
    slogan = TextField(null=True)  # 个性签名
    forget_token = TextField(null=True)  # 找回密码的token
    blog = TextField(null=True)  # blog
    org = TextField(null=True)  # 组织
    dribbble = TextField(null=True)
    instagram = TextField(null=True)
    twitter = TextField(null=True)
    github = TextField(null=True)
    wechat = TextField(null=True)
    douban = TextField(null=True)
    is_admin = IntegerField(null=True)  # 是否是管理员
    birthday = DateTimeField(null=True)  # 出生日期
    post = TextField(null=True)  # 职位


class comment(base):

    '''评论表'''
    key_type = TextField()  # 用于那个类型 比如一个系统有多个地方都要有评论,则用这个来区别, 站点可以填为 site'
    key = TextField()  # 比如填入 site_id, 使用这个评论的元素
    comment = TextField()  # 评论
    parent_id = IntegerField()  # 可空,父节点 id
    user_id = IntegerField()


class crud_conf(base):

    '''curd配置'''
    name = TextField()  # 字段的名字
    description = TextField()  # 字段的描述 用于显示在 form 的前面
    options = JSONField(null=True)  # select 类型的字段的 value 和 desc json 格式存储
    table_name = TextField()  # 表名 冗余,但是我不想用 id 了
    grid_show = IntegerField(null=True)  # 是否在 grid 显示
    c_type = TextField(null=True)  #
    seq = IntegerField(null=True)  # DEFAULT 0, -- 排列顺序
    sql_parm = TextField(null=True)  #
    is_search = IntegerField(null=True)  # 是否要在高级搜索里出现


class timeline(base):
    oper = TextField()  # 执行的动作
    target_type = TextField()  # 执行的目标对象
    target_id = IntegerField()  # 目标的 id, 用于表关联
    other_info = JSONField(null=True)  # 其他的附加信息, 使用 json 来存放
    user_id = IntegerField()


class uploaded_files_bz(base):

    '''
    create by bigzhu at 15/09/10 20:43:03 保存上传的文件的相关信息
    '''
    key = TextField()
    file_name = TextField()
    path = TextField()

if __name__ == '__main__':
    pass
