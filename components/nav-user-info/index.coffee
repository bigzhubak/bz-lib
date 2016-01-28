###

###
require './style.less'
#cookie = require '../../functions/cookie'
f_user_info = require '../../functions/user_info'
module.exports =
  template: require('./template.html')
  data:->
    user_info:
      user_name:''
      email:''
  created:->
    f_user_info.checkNewUserInfo()
  computed:
    avatar:->
      if @user_info.picture
        return @user_info.picture
      else
        return '/static/images/avatar.svg'
    desc:->
      if @user_info.slogan
        return @user_info.slogan
      else
        return 'Nothing'
  methods:
    delAndLogout:->
      localStorage.removeItem('user_info')
      window.location.href="/logout"
