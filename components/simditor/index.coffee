require './style.less'
check = require 'lib/functions/check.coffee'

Simditor = require('simditor')
module.exports =
  template: require('./template.html')
  props: [ 'content']
  ready:->
    @initSimditor()
    @$watch 'content',  (newVal, oldVal)-> #只是用来做第一次初始值同步的
      #if @simditor.getValue()
      #  return
      if newVal != @simditor.getValue()
        @simditor.setValue newVal
  methods:
    initSimditor:->
      toolbar = [
        'title'
        'bold'
        'italic'
        'underline'
        'strikethrough'
        'color'
        '|'
        'ol'
        'ul'
        'blockquote'
        'code'
        'table'
        '|'
        'link'
        'image'
        'hr'
        '|'
        'indent'
        'outdent'
        'alignment'
      ]
      mobileToolbar = [
        'bold'
        'underline'
        'strikethrough'
        'color'
        'ul'
        'ol'
      ]
      small_tool_bar = [
        'title'
        'link'
        'image'
        'bold'
      ]
      if check.mobileCheck()
        toolbar = mobileToolbar
      @simditor = new Simditor(
        textarea: @$el
        placeholder: '这里输入文字...'
        #toolbar: toolbar
        toolbar: small_tool_bar
        toolbarFloat:false
        pasteImage: true
        defaultImage: 'assets/images/image.png'
        upload:
          url: '/upload_image'
          params: null
          fileKey: 'upload_file'
          connectionCount: 3
          leaveConfirm: '正在上传文件，如果离开上传会自动取消'
      )
      @simditor.on 'valuechanged', (e, src) =>
        #vue如果要双向绑定,要定义这个函数
        @content = @simditor.getValue()
