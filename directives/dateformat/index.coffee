require './style.less'
bz = require '../../lib.coffee'
module.exports =
  bind: ->
  update: (value, old_value) ->
    if value
      el = $(@el)
      mask = @arg
      date_str = bz.dateFormat(value, mask)
      $(@el).html(date_str)
  unbind: ->
