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
        <tr>
          <td colspan="2">这货没有参数, 目前只有logout一个操作</td>
        </tr>
      </tbody>
    </table>
    <div class='ui center aligned basic segment'>
      <button @click='run' class='ui basic button'>
        <i class='icon play'></i>
        运行
      </button>
    </div>
    <menu-user-info></menu-user-info>
  </div>
</template>

<script>
  import MenuUserInfo from './MenuUserInfo.vue'
  export default {
    components: {
      MenuUserInfo
    },
    methods: {
      run: function () {
        alert('用不着运行，这货是直接运行的')
      }
    }
  }
</script>
