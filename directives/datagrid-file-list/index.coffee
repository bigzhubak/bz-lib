require './style.less'
module.exports =
  bind: ->
  update: (value, old_value) ->
    params = this.arg.split(".")
    if(params.length < 2)
      throw "file-list 指令中的参数不足，请检查是否指定表名与字段名."
    if(!$)
      throw "JQuery没有正确引用."
    table_name = params[0]
    column = params[1]
    parms_str = [table_name, column, value].join("/")
    ((_this, str)->
      $.get('/file_upload/' + str).done (d) ->
        html = ''
        if d.results.length == 0
          return
        for i of d.results
          f = d.results[i]
          html += '<div><a href=\'' + f.file_path + '\'\' target=\'_blank\'>下载</a></div>'
        # 拼装字符串，注入到list中
        $(_this.el).html html
        return
    ) this, parms_str
  unbind: ->
