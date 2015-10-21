require './style.less'
timeLen = (that_time)-> #计算距今的时间间隔
  second = 1000
  minute = second * 60
  hour = minute * 60
  day = hour * 24
  month = day * 30
  year = month * 12

  now = Date.now()
  interval = now - that_time

  if interval < minute
    desc  = parseInt(interval / second) + "秒前"
  else if interval < hour
    desc = parseInt(interval / minute) + "分钟前"
  else if interval < day
    desc = parseInt(interval / hour) + "小时前"
  else if interval < month
    desc = parseInt(interval / day) + "天前"
  else if interval < year
    desc = parseInt(interval / month) + "个月前"
  else
    desc = parseInt(interval / year)+"年前"
  return desc

module.exports =
  bind: ->
  update: (new_value, old_value) ->
    if new_value
      el = $(@el)
      that_time = Date.parse(new_value)
      date_str = timeLen(that_time)
      el.html(date_str)
  unbind: ->
