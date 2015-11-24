###
错误处理相关
###
url =
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
  autoLink : (options...) ->
    pattern = ///
      (^|[\s\n]|<br\/?>) # Capture the beginning of string or line or leading whitespace
      (
        (?:https?|ftp):// # Look for a valid URL protocol (non-captured)
        [\-A-Z0-9+\u0026\u2019@#/%?=()~_|!:,.;]* # Valid URL characters (any number of times)
        [\-A-Z0-9+\u0026@#/%=~()_|] # String must end in a valid URL character
      )
    ///gi
  
    return @replace(pattern, "$1<a href='$2'>$2</a>") unless options.length > 0
  
    option = options[0]
    linkAttributes = (
      " #{k}='#{v}'" for k, v of option when k isnt 'callback'
    ).join('')
  
    @replace pattern, (match, space, url) ->
      link = option.callback?(url) or
        "<a href='#{url}'#{linkAttributes}>#{url}</a>"
  
      "#{space}#{link}"

module.exports = url
