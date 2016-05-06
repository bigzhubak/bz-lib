<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>Forget</h1>
    <p>
      输入邮件来找回用户密码
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">没参数， 后台方法找不到了，以后再说吧</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <forget></forget>
  </div>
</template>

<script>
  import Forget from './Forget'
  export default {
    components: {
      Forget
    },
    data: function () {
      return {
        parms: [
        ],
        code: `<forget></forget>`
      }
    },
    methods: {
      call_back: function () {
        window.alert('点击了确认')
      },
      run: function () {
        this.$broadcast('confirm')
      }
    }
  }
</script>
