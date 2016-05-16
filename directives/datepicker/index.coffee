require './style.less'
module.exports =
  bind: ->
    _this = @
    datepicker = $(@el)
    datepicker.datepicker
      format: "yyyy-mm-dd"
      language: "zh-CN"
      autoclose: true
      forceParse: true
      clearBtn: true
      startDate: '1980-01-01'
      orientation: "top left"
    .on("changeDate", (e)->
      levels = _this.raw.split(".")
      d_str = ""
      if e.date
        d_str = e.date.valueOf()
      temp_obj = _this.vm[levels[0]]
      index  = 1
      while index <= levels.length - 1
        level = levels[index]
        if typeof temp_obj[level] == "undefined" and index < levels.length - 1
          temp_obj.$add(levels[index], {})
          temp_obj = temp_obj[level]
        else if index == levels.length - 1
          temp_obj[level] = d_str
        index += 1
    ).siblings(".input-group-addon")
      .on("click", ->
        datepicker.datepicker("show")
      )
  update: (value, old_value) ->
    if isNaN(value)
      $(@el).datepicker('update', value)
    else if value
      $(@el).datepicker('update', new Date(parseInt(value)))
    else
      $(@el).datepicker('update', '')
  unbind: ->
