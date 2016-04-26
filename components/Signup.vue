<style lang=less>
</style>

<template>
  <div>
    <div class="ui center aligned secondary segment">
      <b>用户注册</b>
    </div>
    <div class="ui segment">
      <form class="ui form fluid ">
        <div v-bind:class="{ 'error': user_name_error }" class="field" >
          <label>用户名</label>
          <input @focus="cleanError" v-model="user_name"  placeholder="请输入用户名" type="text">
        </div>
        <div v-bind:class="{ 'error': email_error }" class="field" >
          <label>邮箱</label>
          <input @focus="cleanError" v-model="email" placeholder="请输入邮箱地址，便于密码找回" type="text">
        </div>
        <div v-bind:class="{ 'error': password_error }" class="field">
          <label>密码</label>
          <input v-model="password" @keyup.enter="signup" @focus="cleanError" placeholder="请输入密码"  type="password">
        </div>
        <a @click="signup" class="ui basic submit button">注册</a>
      </form>
      <div v-show="error_info" class="ui bottom  warning message">
        <i class="icon help"></i>
        {{error_info}}
      </div>
    </div>
  </div>
</template>

<script>
  import store from '../store'
  import {signup} from '../functions/toast.js'

  import {getTopRightToast} from '../functions/toast.js'
  var toast = getTopRightToast()
  export default {
    store,
    vuex: {
      actions: {
        asignup: signup
      }
    },
    props: ['call_back'],
    components: {
    },
    data: function () {
      return {
        user_name: '',
        user_name_error: false,
        email: '',
        email_error: false,
        password: '',
        password_error: false
      }
    },
    ready () {
    },
    methods: {
      signup: function () {
        if (!this.user_name) {
          this.user_name_error = true
          toast.error('请输入用户名')
          console.log(toast)
          return
        }
        if (!this.email) {
          this.email_error = true
          toast.error('请输入邮箱')
          return
        }
        if (!this.password) {
          this.password_error = true
          toast.error('请输入密码')
          return
        }
        var parm = {
          user_name: this.user_name,
          email: this.email,
          password: this.password
        }
        this.asignup(parm, this.call_back)
      },
      cleanError: function () {
        this.user_name_error = false
        this.email_error = false
        this.password_error = false
      }
    }
  }
</script>
