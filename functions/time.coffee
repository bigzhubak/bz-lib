###
错误处理相关
###
time =
  timeLen : (that_time)-> #计算距今的时间间隔
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
  dateFormat:(timestamp, mask)->
    date = new Date(timestamp)
    _this = @
    o = {
      "y+": (len)->
        return _this.preZero(date.getFullYear(), len)
      "M+": (len)->
        return _this.preZero(date.getMonth() + 1, len)
      "d+": (len)->
        return _this.preZero(date.getDate(), len)
      "h+": (len)->
        return _this.preZero(date.getHours(), len)
      "m+": (len)->
        return _this.preZero(date.getMinutes(), len)
      "s+": (len)->
        return _this.preZero(date.getSeconds(), len)
    }
    for regStr of o
      matched_array = mask.match(new RegExp(regStr))
      if matched_array
        res = o[regStr](matched_array[0].length)
        mask = mask.replace(matched_array[0], res)
    return mask

module.exports = time
