<style lang="less">
</style>

<template>
  <div v-show="user_name != '' " class="ui simple dropdown item">
    <i class="dropdown icon"></i> {{user_name}}
    <div class="menu">
      <a href="/logout" class="item">退出登录</a>
    </div>
  </div>
</template>

<script>
  import store from '../store'
  export default {
    computed: {
      user_name () {
        return store.state.user_info.user_name
      }
    },
    ready () {
      store.actions.queryUserInfo()
    },
    methods: {
    }
  }
</script>
