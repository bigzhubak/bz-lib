###
忘记密码
###
require './style.less'
module.exports =
  directives:
    "btn-loading": require 'lib/directives/btn-loading'
  template: require('./template.html')
  created:->
    error = require '../../functions/error.coffee'
    error.setOnErrorVm(@)
  methods:
    forget:->
      if not @email
        throw new Error("请输入邮箱")
      @loading=true
      for key of regexp
        value = regexp[key]
        if value == false
          throw new Error("您的邮箱无法验证, 请填写正确的邮箱")
      parm = JSON.stringify
        email:@email
      $.ajax
        url: '/forget'
        type: 'POST'
        data : parm
        success: (data, status, response) =>
          @loading=false
          if data.error != '0'
            throw new Error(data.error)
          else
            bz.showSuccess5('找回密码成功,请登录你的邮箱继续修改密码')
            @email = ''
        error: ->
    cleanError:->
      @$data.error_info = false
