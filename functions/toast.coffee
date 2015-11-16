###
错误处理相关
###
toastr = require 'toastr'
toast =
  getTopRightToast:->
    toastr.options =
      'closeButton': false
      'debug': false
      'newestOnTop': false
      'progressBar': false
      'positionClass': 'toast-top-right'
      'preventDuplicates': false
      'onclick': null
      'showDuration': '300'
      'hideDuration': '1000'
      'timeOut': '5000'
      'extendedTimeOut': '1000'
      'showEasing': 'swing'
      'hideEasing': 'linear'
      'showMethod': 'fadeIn'
      'hideMethod': 'fadeOut'
    return toastr

module.exports = toast
