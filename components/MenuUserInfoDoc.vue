<style lang="less">
</style>

<template>
  <div>
    <h1>MenuUserInfo</h1>
    <p>
      显示当前登录用户已经相关操作, 通常放在menu上显示下拉菜单
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">这货没有参数, 目前只有logout一个操作</td>
        </tr>
      </tbody>
    </table>
    <pre>
    <code v-text="code">
    </code>
    </pre>
    <button @click='run' class='ui basic button'>
      <i class='icon play'></i>
      运行
    </button>
    <div class="ui segment">
      <menu-user-info></menu-user-info>
    </div>
  </div>
</template>

<script>
  import MenuUserInfo from './MenuUserInfo.vue'
  export default {
    components: {
      MenuUserInfo
    },
    data: function () {
      return {
        parms: [],
        code: '<menu-user-info></menu-user-info>'
      }
    },
    methods: {
      run: function () {
        alert('用不着运行，这货是直接运行的')
      }
    }
  }
</script>
