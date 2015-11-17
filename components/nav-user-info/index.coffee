###

###
require './style.less'
module.exports =
  template: require('./template.html')
  data:->
    user_info:null
  created:->
    if localStorage.user_info
      JSON.parse(localStorage.user_info)
      @user_info=JSON.parse(localStorage.user_info)
    else
      @getUserInfo()
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
        error: ->
    delAndLogout:->
      localStorage.removeItem('user_info')
      window.location.href="/logout"
