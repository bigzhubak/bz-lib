export function preZero (num, len) {
  var a, numStr
  numStr = num.toString()
  if (len < numStr.length) {
    return numStr
  } else {
    a = new Array(len + 1).join('0') + numStr
    return a.substr(a.length - len, a.length - 1)
  }
}
export function timeLen (that_time) {
  var day, desc, hour, interval, minute, month, now, second, year
  second = 1000
  minute = second * 60
  hour = minute * 60
  day = hour * 24
  month = day * 30
  year = month * 12
  now = Date.now()
  interval = now - that_time
  if (interval < minute) {
    desc = parseInt(interval / second, 10) + '秒前'
  } else if (interval < hour) {
    desc = parseInt(interval / minute, 10) + '分钟前'
  } else if (interval < day) {
    desc = parseInt(interval / hour, 10) + '小时前'
  } else if (interval < month) {
    desc = parseInt(interval / day, 10) + '天前'
  } else if (interval < year) {
    desc = parseInt(interval / month, 10) + '个月前'
  } else {
    desc = parseInt(interval / year, 10) + '年前'
  }
  return desc
}
export function dateFormat (timestamp, mask) {
  var _this, date, matched_array, o, regStr, res
  date = new Date(timestamp)
  _this = this
  o = {
    'y+': function (len) {
      return _this.preZero(date.getFullYear(), len)
    },
    'M+': function (len) {
      return _this.preZero(date.getMonth() + 1, len)
    },
    'd+': function (len) {
      return _this.preZero(date.getDate(), len)
    },
    'h+': function (len) {
      return _this.preZero(date.getHours(), len)
    },
    'm+': function (len) {
      return _this.preZero(date.getMinutes(), len)
    },
    's+': function (len) {
      return _this.preZero(date.getSeconds(), len)
    }
  }
  for (regStr in o) {
    matched_array = mask.match(new RegExp(regStr))
    if (matched_array) {
      res = o[regStr](matched_array[0].length)
      mask = mask.replace(matched_array[0], res)
    }
  }
  return mask
}
