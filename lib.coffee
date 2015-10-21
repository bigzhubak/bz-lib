if $().toastmessage
  $().toastmessage(
    sticky: false
    position: 'top-right'
    stayTime: 5000
    closeText: '<i class="fa fa-times"></i>'
    successText: '<i class="fa fa-check"></i>'
    warningText: '<i class="fa fa-exclamation-triangle"></i>',
    noticeText: '<i class="fa fa-exclamation"></i>',
    errorText: '<i class="fa fa-exclamation-circle"></i>'
  )
window.bz =
  calculateHeight: (img_height, img_width, max_width)->
    if max_width<=img_width
      real_height = max_width*img_height/img_width
    else
      real_height = img_height
    return real_height
  getFitHeight: (img_height, img_width)->
      #还没渲染，无法动态取，只能用 bootstrap的栅格来算
      window_width = $(window).width()
      border = 15*2 #边框总是有15，两边30
      if window_width <=768
        message_width = window_width-border
      if 768<window_width<992
        message_width = 750-border
      if 992<=window_width<1200
        message_width = 970*(8/12)-border
      if window_width>=1200
        message_width = 1170*(8/12)-border
      img_border = 20
      max_width = message_width-img_border
      real_height = window.bz.calculateHeight(img_height, img_width, max_width)
      return real_height
  delay: (ms, func)-> # underscorejs 有做好的 
    setTimeout func, ms
  mobilecheck: ->
    check = false
    ((a) ->
      if /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a) or /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))
        check = true
      return
    ) navigator.userAgent or navigator.vendor or window.opera
    check
  setOnErrorVm:(vm)->
    window.onerror = (errorMsg, url, lineNumber)->
      error = errorMsg.replace('Uncaught Error: ', '')
      vm.$set('error_info', error)
      bz.showError5(error)
  isEmpty : (obj) -> #是不是空对象
    if obj == null
      return true
    if obj.length > 0
      return false
    if obj.length == 0
      return true
    for key of obj
      if Object::hasOwnProperty.call(obj, key)
        return false
    true
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
  getLastParm:-> #取最后的参数
    parms = window.location.pathname.split( '/' )
    return parms[parms.length-1]
  getUrlPath:(number)-> #传入参数来获取url path, 为 'last' 时取最后一个; crate by bigzhu
    parms = window.location.pathname.split( '/' )
    if number == 'last'
      number = parms.length-1
    return parms[number]
  getUrlParm:->
    parms = window.location.pathname.split( '/' )
    return parms
  getHashParms:-> #获取hash参数，返回数组
    parms = window.location.hash.split('/')
    return parms
  showSuccess5:(message)-> #显示一个消息提示5s 依赖 https://github.com/akquinet/jquery-toastmessage-plugin 
    if $().toastmessage
      successToast = $().toastmessage('showSuccessToast', message)
    else
      console.log "require jquery-toastmessage-plugin"
  showNotice5:(message)->
    if $().toastmessage
      myToast =  $().toastmessage('showNoticeToast', message)
    else
      console.log "require jquery-toastmessage-plugin"
  showWarning5:(message)->
    if $().toastmessage
      warningToast = $().toastmessage('showNoticeToast', message)
    else
      console.log "require jquery-toastmessage-plugin"
  showError5:(message)->
    if $().toastmessage
      errorToast = $().toastmessage('showErrorToast', message)
    else
      console.log "require jquery-toastmessage-plugin"
  preZero:(num, len)->
    numStr = num.toString()
    if len < numStr.length
      return numStr
    else
      a = new Array(len + 1).join("0") + numStr
      return a.substr(a.length - len, a.length - 1)
  # 清除html标签
  HTMLEncode:(value)->
    return $("<div/>").html(value).text()
  HTMLDecode:(value)->
    return $("<div/>").text(value).html()

  #时间格式化工具 timestramp -> string
  #支持 y - 年,M - 月,d - 日,h - 小时,m - 分钟,s - 秒 根据mask中对应字符的数量自动补0
  dateFormat:(timestramp, mask)->
    date = new Date(timestramp)
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
  #转换单位
  #传入kb
  #超过1024kb为m
  #超过1024m的按照g显示
  #超过1024g的按照T显示
  formatUnit:(value)->
    value = parseFloat(value)
    m = 1024
    g = m*1024
    t = g*1024
    if value>t
      desc = (value/t).toFixed(2) + 'TB'
    else if value>g
      desc = (value/g).toFixed(2) + 'GB'
    else if value>m
      desc = (value/m).toFixed(2) + 'MB'
    else
      desc = value + 'KB'
    return desc
  formatCount:(value)-> #转换数额，>=10000 的改为w >=1000 改为k
    f_value = parseFloat(value)
    w = 10000
    k = 1000
    if f_value>=w
      desc = (f_value/w).toFixed(1) + 'W'
    else if f_value>=k
      desc = (f_value/k).toFixed(1) + 'K'
    else
      desc = parseInt(value)
    return desc
  getHashPram: (key) -> # 获取hash参数的值
    _hashStr = window.location.hash.replace('#','')
    if(!_hashStr || _hashStr == "")
      return undefined
    _hashs = _hashStr.split(";")
    for _hashItem in _hashs
      _hash = _hashItem.split("=")
      if(key == _hash[0])
        return _hash[1]
    return undefined
  setHashPram: (key,value) -> # 设置hash参数,格式如: aa=bb;cc=dd;  
    _hashStr = window.location.hash.replace('#','')
    if(!window.bz.getHashPram(key) && value)
      window.location.hash = _hashStr + key + "=" + value + ";"
    else
      _hashs = _hashStr.split(";")
      _newHashStr = ""
      for _hashItem in _hashs
        if (!_hashItem || _hashItem == "")
             continue
          _hash = _hashItem.split("=")
          if(key == _hash[0])
            if(value != "")
              _newHashStr = _newHashStr + key + "=" + value + ";"
          else
            _newHashStr = _newHashStr + _hash[0] + "=" + _hash[1] + ";"
      window.location.hash = _newHashStr
  isInclude : (key,words)->
    if words.toLocaleLowerCase().indexOf(key.toLocaleLowerCase()) > -1
        return true
    else
        return false
  resolve: (obj, path, value) ->
    r=path.split(".")
    if r.length > 1
      key = r.shift()
      if not obj[key]
        obj[key]={}
      return window.bz.resolve(obj[key], r.join("."), value)
    else
      obj[path] = value or {}
    @

module.exports = window.bz
