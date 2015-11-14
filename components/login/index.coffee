###
login

登录页
oauths:参见oauth2-button
###
require './style.less'
module.exports =
  props:['oauths']
  data:->
    user_name:''
    password:''
  template: require('./template.html')
  created:->
    #bz.setOnErrorVm(@)
  components:
    'oauth2-button': require '../oauth2-button'
  methods:
    signup:->
      window.location.href = '/signup?user_name=' + @user_name
    cleanError:->
      @$data.error_info = false
    login:->
      if not @user_name
        throw new Error("请输入用户名")
      if not @password
        throw new Error("请输入用密码")
      @error_info = false
      @loading=true
      parm = JSON.stringify
        user_name:@user_name
        password:@password
        #尝试取验证的数据
        geetest_challenge : $('.geetest_challenge').val()
        geetest_validate : $('.geetest_validate').val()
        geetest_seccode : $('.geetest_seccode').val()
        validate: $('#validate').val()
      $.ajax
        url: '/login'
        type: 'POST'
        data : parm
        success: (data, status, response) =>
          @loading=false
          if data.error != '0'
            #后台说这个用户没有时,提示用户创建
            if data.error == 'user not exist'
              $('#confirm-ask-create').modal()
              return
            else
              throw new Error(data.error)
          else
            location.pathname = '/'
        error: ->
