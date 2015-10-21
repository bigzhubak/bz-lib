require './style.less'
module.exports =
  bind: ->
  update: (value, old_value) ->
    @el.disabled = value
  unbind: ->
