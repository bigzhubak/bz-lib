# 当datagrid中需要显示file_upload字段的时候，根据传入的参数查出已经上传的文件
module.exports =
  bind: ->
  update: (value, old_value) ->
    # 拼接参数，处理异常情况
    params = @arg.split('.')
    if params.length < 2
      throw 'file-list 指令中的参数不足，请检查是否指定表名与字段名.'
    if !$
      throw 'JQuery没有正确引用.'
    table_name = params[0]
    column = params[1]
    parms_str = [
      table_name
      column
      value
    ].join('/')
    # 闭包ajax
    ((_this, str) ->
      $.get('/file_upload/' + str).done (d) ->
        html = ''
        if d.results.length == 0
          return
        for i of d.results
          f = d.results[i]
          html += '<div><a href=\'' + f.file_path + '\'\' target=\'_blank\'>' + f.file_name + '</a></div>'
        # 拼装字符串，注入到list中
        $(_this.el).html html
        return
    ) this, parms_str
    return
  unbind: ->
