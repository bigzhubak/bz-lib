<style lang="less">
</style>

<template>
  <div class="ui segment">
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
          <td colspan="2">加入了3个slot</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <menu-user-info>
      <a slot="one" href="/test" class="item">test</a>
    </menu-user-info>
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
        code: `<menu-user-info>
        <a slot="one" href="/test" class="item">test</a>
        </menu-user-info>`
      }
    },
    methods: {
    }
  }
</script>
