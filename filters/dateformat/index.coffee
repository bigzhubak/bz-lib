require './style.less'
bz = require '../../lib_old.coffee'
module.exports =
  fn: (value, mask)->
    date_str = bz.dateFormat(value, mask)




