###
local storage 相关，没写完
###
local_storage =
  update:(key, value)-> #取最后的参数
    original_value = JSON.parse(localStorage[key])
module.exports = local_storage
