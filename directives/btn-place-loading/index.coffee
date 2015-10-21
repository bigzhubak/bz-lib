require './style.less'
module.exports =
  bind: ->
    $(@el).prepend("<i class='fa fa-spin fa-spinner'></i>")
    return
  update: (new_value, old_value) ->
    if new_value
      $(@el).children().css('visibility', 'visible')
    else
      $(@el).children().css('visibility', 'hidden')
    return
  unbind: ->
