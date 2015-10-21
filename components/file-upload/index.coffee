require './style.less'
module.exports =
  template: require('./template.html')
  props: [
    'table-name'
    'field-name'
    'record-id'
    'disabled'
  ]
  computed:
    column: ->
      @fieldName
      # 上传用的字段名标记;
    disabled_b: ->
      if !@disabled
        false
      else
        bool = true
        try
          bool = new Function('return ' + @disabled)
        catch e
          bool = true
        bool
  attached: ->
    if !@tableName or !@column
      throw '组件没有正确的获取参数，请检查声明的HTML'
    # 因为数据的显示传递会覆盖data对象，所以改成在attached方法中声明
    @upload_ids = []
    # 上传成功后的id
    @append_files = []
    # 新增的文件
    @new_file_ids = []
    # 用于保存新增文件的文件id
    @getExistFiles()
    # 初始化的时候调用一次获取当前文件
    return
  methods:
    getExistFiles: ->
      _this = @
      if !_this.recordId
        _this.$set 'files', []
      else
        parms_str = [
          @tableName
          @column
          @recordId
        ].join('/')
        _this.closureAjax (__this) ->
          $.get('/file_upload/' + parms_str).done (d) ->
            __this.$set 'files', d.results
            return
          return
      return
    appendFile:(e) ->
      files = e.target.files
      for i of files
        if !isNaN(i)
          f = files[i]
          fd = new FormData
          fd.append 'file_' + i, f
          # 把文件放入到 all_files列表和 fd上传队列中
          new_file =
            'file_type': 'file'
            'file_name': f.name
            'remove': false
            'suffix': null
            'fd': fd
          @append_files.push new_file
      @uploadFiles()
      return
    removeFile: (f) ->
      _this = this
      if confirm('是否确定删除文件:' + f.file_name + '?')
        $.post('/file_ref', JSON.stringify('remove_file': f.id)).done (d) ->
          if d.error == '0'
            # 删除文件的时候把append_files和files里的清掉
            if _this.files.indexOf(f) >= 0
              _this.files.splice _this.files.indexOf(f), 1
            if _this.append_files.indexOf(f) >= 0
              _this.append_files.splice _this.append_files.indexOf(f), 1
            window.bz.showSuccess5 '文件删除成功.'
          else
            window.bz.showError5 '删除文件时发生错误:' + d.error
          return
      return
    uploadFiles: ->
      _this = @
      _this.append_files.forEach (file, index) ->
        file.suffix = 'uploading'
        _this.closureAjax (__this) ->
          $.ajax(
            url: '/file_upload'
            type: 'POST'
            data: file.fd
            processData: false
            contentType: false).done (d) ->
            if d.error == '0'
              # 删除append_files
              __this.append_files.splice __this.append_files.indexOf(file), 1
              # 放到所有文件列表
              __this.files.push d.results[0]
              window.bz.showSuccess5 '文件上传成功'
            else
              window.bz.showError5 '文件上传时发生错误:' + d.error
            return
          return
        return
      return
    createFileRef: (recordId) ->
      _this = this
      if !_this.recordId and !recordId
        throw '请在调用之前先提交外部表单。'
        # 如果组件参数和调用参数都没有，就抛出异常
      else if recordId
        _this.recordId = recordId
        # 如果参数存在，就赋值给当前的recordId
      # 记录上传成功后的ID
      for i of _this.files
        f = _this.files[i]
        @new_file_ids.push f.file_id
      params =
        'column': @column
        'table_name': @tableName
        'record_id': @recordId
        'new_file_ids': @new_file_ids
      _this.closureAjax (__this) ->
        $.post('/file_ref', JSON.stringify(params)).done (data) ->
          if data.error == '0'
            __this.new_file_ids = []
            __this.$set 'upload_ids', data.results
          else
            throw data.error
          return
        return
      return
    closureAjax: (func) ->
      func this
    clear: ->
      @$set 'upload_ids', []
      # 上传成功后的id
      @$set 'append_files', []
      # 新增的文件
      @$set 'files', []
      # 已上传文件
      @$set 'new_file_ids', []
      # 用于保存新增文件的文件id
      $(@$el).find('.input_file').val ''
      # 清空file选择
      return
  directives:
    'file-icon':require('../../directives/file-icon')
    'file-list':require('../../directives/file-list')
    'href':require('../../directives/href')
