###
错误处理相关
###
error =
  setOnErrorVm:(vm)-> #注册vm，以设置error_info
    window.onerror = (errorMsg, url, lineNumber)->
      error = errorMsg.replace('Uncaught Error: ', '')
      vm.$set('error_info', error)

module.exports = error
