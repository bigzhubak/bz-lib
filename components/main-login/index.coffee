###
包装了 login signup forget 的用户登录相关组件
###
require './style.less'
module.exports =
  props:['oauths']
  data:->
    current_view:'login'
  methods:
    change:(view)->
      @current_view = view

  template: require('./template.html')
  components:
    "login": require '../login'
    "signup": require '../signup'
    "forget": require '../forget'
