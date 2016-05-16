require './style.less'
module.exports =
  bind: ->
  update: (value, old_value) ->
    el = $(@el)
    if value
      el.children().hide()
      el.prepend("<i class='fa fa-spin fa-spinner'></i>")
    else
      el.children(".fa.fa-spin.fa-spinner").remove()
      el.children().show()
  unbind: ->
