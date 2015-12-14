###

###
require './style.less'
module.exports =
  components:
    'nav-user-info': require '../nav-user-info'
  props:['navbar_header', 'nav_links']
  template: require('./template.html')
  methods:
    search:(e)->
      # 如果定义了 header_search 方法, 就不用默认的 google search 了
      e.preventDefault()
      if window.header_search
        window.header_search(@search_value)
        return
      host = window.location.hostname
      url = "https://www.google.com/search?q=site:"+host+" "+@search_value+"&gws_rd=ssl"
      window.open(url)
