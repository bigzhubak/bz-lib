###
#用户信息相关
###
cookie = require './cookie'
user_info =
  getUserInfo:->
    $.ajax
      url: '/get_user_info'
      type: 'GET'
      success: (data, status, response) =>
        if data.error != '0'
          console.log data.error
          #throw new Error(data.error)
        else
          localStorage.user_info = JSON.stringify(data.user_info)
          @user_info=data.user_info
      error:(data, status, response)->
        console.log data
        console.log status
        console.log response
  checkNewUserInfo:->
    if cookie.getCookieValue('user_id') == localStorage.cookie_user_id and localStorage.user_info
      JSON.parse(localStorage.user_info)
      @user_info=JSON.parse(localStorage.user_info)
    else
      #为了把this传进去
      user_info.getUserInfo.call()
      localStorage.cookie_user_id = cookie.getCookieValue('user_id')
  isLogin:->
    return cookie.getCookieValue('user_id')

module.exports = user_info
