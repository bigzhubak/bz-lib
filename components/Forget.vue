<style lang="less">
</style>

<template>
  <div class="ui center aligned secondary segment">
    <b>找回密码</b>
  </div>
  <div class="ui segment">
    <form class="ui form fluid ">
      <div class="field">
        <label>邮箱</label>
        <input type="text" v-model="email" class="form-control" placeholder="请输入邮箱地址" @keyup.enter="forget">
      </div>
      <a @click="forget" class="ui blue submit button">发送邮件</a>
    </form>
  </div>
</template>

<script>
  import store from '../store'
  import toastr from 'toastr'
  export default {
    directives: {
    },
    created: function () {
    },
    methods: {
      forget: function () {
        if (!this.email) {
          toastr.error('请输入邮箱')
          return
        }
        // for (key in regexp) {
        //   value = regexp[key]
        //   if (value === false) {
        //     toastr.error('您的邮箱无法验证, 请填写正确的邮箱')
        //     return
        //   }
        // }
        store.actions.forget(this.email)
      }
    }
  }
</script>
