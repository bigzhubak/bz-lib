###
错误处理相关
###
toast = require './toast.coffee'
top_toast = toast.getTopRightToast()

error =
  setOnErrorVm:(vm)-> #注册vm，以设置error_info
    window.onerror = (errorMsg, url, lineNumber)->
      error = errorMsg.replace('Uncaught Error: ', '')
      top_toast.error(error,'出错了!')
      console.log error
      console.log top_toast
      if _.has(vm, 'error_info')
        vm.$set('error_info', error)

module.exports = error
