<style lang="less">
</style>

<template>
  <div class="ui segment">
    <div>
      <h1>Login</h1>
      <p>
        登录
      </p>
      <table class="ui celled table">
        <thead>
          <tr><th>参数</th><th>说明</th></tr>
        </thead>
        <tbody>
          <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
          <tr v-show="parms.length===0">
            <td colspan="2">这货没有参数</td>
          </tr>
        </tbody>
      </table>
    </div>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <login :call_back="call_back"></login>
  </div>
</template>

<script>
  import Login from './Login.vue'
  export default {
    components: {
      Login
    },
    data: function () {
      return {
        parms: [
          {parm: 'call_back', desc: '登录成功后的回调函数'}
        ],
        code: '<login :call_back="call_back"></login>'
      }
    },
    methods: {
      call_back: function () {
        alert('登录成功')
      }
    }
  }
</script>
