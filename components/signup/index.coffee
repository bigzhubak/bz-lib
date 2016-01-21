###
注册页面
###
require './style.less'
error = require '../../functions/error.coffee'
module.exports =
  data:->
    user_name_error:false
    email_error:false
    password_error:false
    error_info:null
  template: require './template.html'
  directives:
    "regexp": require 'lib/directives/regexp'
    "disable": require 'lib/directives/disable'
    "btn-loading": require 'lib/directives/btn-loading'
  created:->
    error.setOnErrorVm(@)
  methods:
    signup:->
      if not @user_name
        @user_name_error=true
        throw new Error("请输入用户名")
      if not @email
        @email_error=true
        throw new Error("请输入邮箱")
      if not @password
        @password_error=true
        throw new Error("请输入用密码")
      #if @password != @repassword
      #  throw new Error("两次密码不一致")

      #if @user_type is ''
      #  throw new Error("请选择用户类型")
      #for key of regexp
      #  value = regexp[key]
      #  if value == false
      #    throw new Error("您的邮箱无法验证, 请填写正确的邮箱")
      parm = JSON.stringify
        user_name:@user_name
        user_type:@user_type
        password:@password
        email:@email
      @loading = true
      $.ajax
        url: '/signup'
        type: 'POST'
        data : parm
        success: (data, status, response) =>
          if data.error != '0'
            throw new Error(data.error)
          else
            bz.showSuccess5('注册成功, 正在自动登录')
            bz.delay 1500, =>
              location.pathname = '/'
          @loading=false
        error: ->
    cleanError:->
      @user_name_error=false
      @email_error=false
      @password_error=false
      @$data.error_info = false
