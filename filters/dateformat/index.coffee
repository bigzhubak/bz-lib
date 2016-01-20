require './style.less'
time = require '../../functions/time.coffee'
module.exports = (value, mask)->
  date_str = time.dateFormat(value, mask)




