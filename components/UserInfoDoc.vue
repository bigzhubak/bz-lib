<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>UserInfo</h1>
    <p>
      用来弹出semantic-ui的"是"和"否"的确认弹出窗口
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr v-show="warning">
          <td colspan="2">{{warning}}</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <user-info :user_info="user_info"></user-info>
  </div>
</template>

<script>
  import UserInfo from './UserInfo.vue'
  import store from '../store'
  export default {
    components: {
      UserInfo
    },
    computed: {
      user_info: function () {
        return store.state.user_info
      }
    },
    ready: function () {
      store.actions.queryUserInfo()
    },
    data: function () {
      return {
        parms: [
          {parm: 'user_info', desc: '用户信息'}
        ],
        warning: '',
        code: `<user-info :user_info="user_info"></user-info>`
      }
    },
    methods: {
      run: function () {
        this.$broadcast('confirm')
      }
    }
  }
</script>
