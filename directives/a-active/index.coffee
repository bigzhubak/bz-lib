#根据 a 的是否是当前 url 的一部分来判断是否设置 active
#modify by bigzhu v-a-active 改为放到li里
#modify by bigzhu v-a-active 保持原样不动,增加给li的active: li-a-active

require './style.less'
module.exports =
  bind: ->
    href = $(this.el).attr('href')
    href = encodeURI(href)
    path = window.location.pathname
    if path.search(href) != -1
      $(this.el).addClass("active")
  update: (value, old_value) ->
  unbind: ->
