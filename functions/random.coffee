###
随机处理相关
###
colors = ['red','orange', 'yellow', "olive", "green", "teal", "blue", "violet", "purple", "pink" ,"brown" ,"grey" ,"black" ]
random =
    color: ->
      index = _.random(0, colors.length)
      return colors[index]

module.exports = random
