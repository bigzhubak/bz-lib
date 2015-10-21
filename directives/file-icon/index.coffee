# 把disabled和href合并了
module.exports =
  bind: ->
    #$(@el).prepend("<i class='fa fa-spin fa-spinner'></i>")
    #return
  update: (value, old_value) ->
    #if value
    #  $(@el).removeAttr('disabled').attr 'href', value
    #else
    #  $(@el).attr 'disabled', true
    #return

    file_icon = "fa fa-upload"
    if value == "uploading"
      file_icon = "fa fa-spin fa-spinner"
    else if [".xls", ".xlsx"].indexOf(value) >= 0
      file_icon = "fa fa-file-excel-o"
    else if [".doc", ".docx"].indexOf(value) >= 0
      file_icon = "fa fa-file-word-o"
    else if [".doc", ".docx"].indexOf(value) >= 0
      file_icon = "fa fa-file-word-o"
    else if [".ppt", ".pptx"].indexOf(value) >= 0
      file_icon = "fa fa-file-powerpoint-o"
    else if [".zip", ".rar", ".7z"].indexOf(value) >= 0
      file_icon = "fa fa-file-archive-o"
    else if [".txt"].indexOf(value) >= 0
      file_icon = "fa fa-file-text-o"
    else if [".pdf"].indexOf(value) >= 0
      file_icon = "fa fa-file-pdf-o"
    else if [".png", ".jpeg", ".jpg", ".gif"].indexOf(value) >= 0
      file_icon = "fa fa-file-image-o"
    else if value
      file_icon = "fa fa-file-o"
    $(@el).attr("class", file_icon)

  unbind: ->
