require './style.less'
time = require '../../functions/time.coffee'

module.exports =
  bind: ->
  update: (new_value, old_value) ->
    if new_value
      el = $(@el)
      that_time = new Date(new_value)
      date_str = time.timeLen(that_time)
      el.html(date_str)
  unbind: ->
