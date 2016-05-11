###
###
format =
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

module.exports = format
