###
渲染 oauth 的图标
oauth.name: oauth.name (必填)
oauth.icon_class: 图标样式
oauth.href: link
oauth.show_name:显示为什么，比如‘豆瓣’
###
require './style.less'
module.exports =
  template: require('./template.html')
  propos:['oauth']
  computed:
    the_href:->
      if _.has(@oauth, 'href')
        return @oauth.href
      else
        return '/'+@oauth.name
    the_icon_class:->
      if _.has(@oauth, 'icon_class')
        return @oauth.icon_class
      else
        return "fa-#{@oauth.name}"
    the_show_name:->
      if _.has(@oauth, 'show_name')
        return @oauth.show_name
      else
        return @oauth.name

