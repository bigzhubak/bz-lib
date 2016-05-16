require './style.less'
module.exports =
  bind: ->
  update: (value, old_value) ->
    if value
      $(@el).removeAttr('disabled').attr 'href', value
    else
      $(@el).attr 'disabled', true
  unbind: ->
