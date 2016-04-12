<style lang='less'>
  .hide{
    display: none
  }
  .icon.github{
    color:black
  }
</style>
<template>
  <div class="ui piled center aligned segment">
    <h4 class="ui header">{{user_info.user_name}}</h4>
    <input :disabled="disable_edit" id="profile-image-upload" class="hide" type="file" @change="previewImg" accept="image/*"/>
    <a id="avatar" @click="changeImg" href="javascript:void(0)" data-content="点击更换头像">
      <img :src="avatar" id="profile-image" class="ui centered image" />
    </a>
    <sub v-show="!disable_edit" >点击更换头像</sub>
    <p v-html="user_info.bio">
    </p>
    <form class="ui form">
      <!--
      <div class="inline field">
        <label>Blog</label>
        <input @focus="autoInsert('blog')" v-model="user_info.blog" :disabled="disable_edit" type="text" placeholder="Blog">
      </div>
      -->
      <div v-show="!disable_edit" class="field">
        <label>个性签名</label>
      </div>

      <div class="inline field">
        <label>
          <a :class="{ disabled: !user_info.twitter }" href="https://twitter.com/{{user_info.twitter}}" target="_blank" class="ui circular twitter icon button" data-content="Twitter">
            <i class="twitter icon"></i>
          </a>
        </label>
        <input v-model="user_info.twitter" @focus="autoInsert('twitter', user_info.user_name)" :disabled="disable_edit" type="text" >
      </div>

      <div class="inline field">
        <label>
          <a :class="{ disabled: !user_info.github }" href="https://github.com/{{user_info.github}}" target="_blank" class="ui circular github icon button" data-content="Github">
            <i class="github icon"></i>
          </a>
        </label>
        <input v-model="user_info.github" @focus="autoInsert('github', user_info.user_name)" :disabled="disable_edit" type="text">
      </div>

      <div class="inline field">
        <label>
          <a :class="{ disabled: !user_info.instagram }" href="https://instagram.com/{{user_info.instagram}}" target="_blank" class="ui circular instagram icon button" data-content="Instagram">
            <i class="instagram icon"></i>
          </a>
        </label>
        <input v-model="user_info.instagram" @focus="autoInsert('instagram', user_info.user_name)" :disabled="disable_edit" type="text" >
      </div>

      <div class="inline field">
        <label>
          <a :class="{ disabled: !user_info.tumblr }" href="http://{{user_info.tumblr}}.tumblr.com" target="_blank" class="ui circular tumblr icon button" data-content="Tumblr">
            <i class="tumblr icon"></i>
          </a>
        </label>
        <input v-model="user_info.tumblr" @focus="autoInsert('tumblr', user_info.user_name)" :disabled="disable_edit" type="text">
      </div>
    </form>

    <div class="ui center aligned basic segment">
      <button v-show="disable_edit" @click="save" class="ui basic button">
        <i class="icon file text"></i>
        编辑
      </button>
      <button v-show="!disable_edit" @click="save" class="ui basic button">
        <i class="icon save"></i>
        保存
      </button>
    </div>
  </div>
</template>

<script>
  var toastr = require('toastr')
  var $ = require('jquery')

  import store from '../store'
  export default {
    components: {
    },
    directives: {
    },
    props: {
      user_info: {
        type: Object,
        default: function () {
          return {
            user_name: '',
            avatar: '',
            bio: '',
            github: '',
            twitter: '',
            instagram: '',
            tumblr: ''
          }
        }
      }
    },
    computed: {
      avatar: function () {
        if (this.user_info.avatar) {
          var avatar_url = this.user_info.avatar
          return '/api_sp/' + btoa(btoa(avatar_url))
        } else {
          return '/media/images/avatar.svg'
        }
      }
    },
    ready: function () {
      store.actions.queryUserInfo()
      $(this.$el).find('.button').popup(
        {
          inline: true
        }
      )
    },
    data: function () {
      return {
        loading: false,
        disable_edit: true,
        button_text: '修改资料'
      }
    },
    methods: {
      autoInsert: function (key, scheme) {
        if (key === 'blog') {
          scheme = 'http://'
        }
        if (!this.user_info[key]) {
          this.user_info[key] = scheme
        }
      },
      changeImg: function () {
        return $('#profile-image-upload').click()
      },
      previewImg: function (e) {
        var file, reader
        file = e.target.files[0]
        if (!file) {
          return
        }
        if (file.size > (10 * 1024 * 1024)) {
          throw new Error('图片大小只能小于10m哦~')
        }
        reader = new FileReader()
        reader.onload = function (e) {
          return $('#profile-image-upload').attr('src', e.target.result)
        }
        reader.readAsDataURL(file)
        return this.uploadImage()
      },
      uploadImage: function () {
        var fd, file
        fd = new FormData()
        file = $('#profile-image-upload')[0].files[0]
        if (file) {
          fd.append('img', file)
          return $.ajax(
            {
              url: '/upload_image',
              type: 'POST',
              data: fd,
              processData: false,
              contentType: false,
              success: (
                function (_this) {
                  return function (data, status, response) {
                    _this.loading = false
                    if (!data.success) {
                      throw new Error(data.msg)
                    } else {
                      toastr.info('保存成功')
                      _this.user_info.avatar = data.file_path
                      return $('#profile-image').attr('src', _this.user_info.avatar)
                    }
                  }
                }
              )(this),
              error: function (error_info) {
                this.loading = false
                throw new Error(error_info)
              }
            }
          )
        }
      },
      save: function () {
        if (this.disable_edit) {
          this.disable_edit = false
        } else {
          // this.loading = true
          this.disable_edit = true
          var user = {
            user_name: this.user_info.user_name,
            blog: this.user_info.blog,
            twitter: this.user_info.twitter,
            github: this.user_info.github,
            instagram: this.user_info.instagram,
            slogan: this.user_info.bio,
            picture: this.user_info.avatar
          }
          store.actions.updateOrInsertUser(user)
        }
      }
    }
  }
</script>
