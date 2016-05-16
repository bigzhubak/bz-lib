#2015-06-02 23:05 - modify by ZhangRui
#正则表达式的指令
require './style.less'
module.exports =
  bind: ->
  update: (value, old_value) ->
    if not window.regexp
      window.regexp = {}
    if value
      reg = new RegExp(@arg)
      r = reg.test(value)
      if r
        $(@el).css('border-color','#d2d6de')
        window.regexp[@expression] = r
      else
        $(@el).css('border-color','#ff0000')
    else
      window.regexp[@expression] = false
  unbind: ->
