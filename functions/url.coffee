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

module.exports = url
