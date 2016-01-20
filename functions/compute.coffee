###
错误处理相关
###
compute =
  calculateHeight: (img_height, img_width, max_width)->
    if max_width<=img_width
      real_height = max_width*img_height/img_width
    else
      real_height = img_height
    return real_height
  getFitHeight: (img_height, img_width)->
      #还没渲染，无法动态取，只能用 bootstrap的栅格来算
      window_width = $(window).width()
      border = 15*2 #边框总是有15，两边30
      if window_width <=768
        message_width = window_width-border
      if 768<window_width<992
        message_width = 750-border
      if 992<=window_width<1200
        message_width = 970*(8/12)-border
      if window_width>=1200
        message_width = 1170*(8/12)-border
      img_border = 20
      max_width = message_width-img_border
      real_height = compute.calculateHeight(img_height, img_width, max_width)
      return real_height
  getFitHeightForSemantic: (img_height, img_width)-> #先搞定<768的
    window_width = $(window).width()
    container_border = 14*2 #边框总是有14，两边28
    card_content_padding = 14*2 #有14，两边28
    if window_width <768
      message_width = window_width-container_border
    if 768<=window_width<=991
      message_width = 723
    if 992<=window_width<=1200
      message_width = 933
    if window_width>1200
      message_width = 1127
    max_width-=card_content_padding
    real_height = compute.calculateHeight(img_height, img_width, max_width)
    return real_height
module.exports = compute
