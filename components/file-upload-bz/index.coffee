###
key: 唯一的名字，建议 表名+业务字段名+id;保证不重复即可
is_edit: 可编辑(true)还是只能查看(false/不传)
###
require './style.less'
module.exports =
  props: ['key', 'is_edit']
  directives:
    'btn-loading':require('../../directives/btn-loading')
    'file-icon':require('../../directives/file-icon')
    'file-list':require('../../directives/file-list')
  template: require('./template.html')
  data:->
    files:[] #已经上传的文件列表
    loading:false
  ready:->
    @getExistFiles()
  methods:
    removeFile:(f)->
      @loading = true
      data = JSON.stringify
        id:f.id
      $.ajax
        url: '/remove_exist_file'
        type: 'POST'
        data: data
        success: (data, status, response) =>
          @loading = false
          @getExistFiles()
    clickButton:->
      $(@$el.parentElement).find('input').click()
    upload:->
      @loading=true
      files = this.$$.file.files
      data = new FormData()
      data.append('file', files[0])
      data.append('key', @key)
      @$http.post('/file_upload_bz', data, (data, status, request) =>
        @loading = false
        @clear()
        @getExistFiles()
        #handling
        return
      ).error (data, status, request) ->
        console.log data
        #handling
        return
    clear:-> #清空，保证选择同一个文件还是能触发 change
      files = this.$$.file
      $(files).val(null)
    getExistFiles:->
      @loading = true
      data = JSON.stringify
        key:@key
      $.ajax
        url: '/get_exist_files'
        type: 'POST'
        data: data
        success: (data, status, response) =>
          @loading = false
          @files = data.files
