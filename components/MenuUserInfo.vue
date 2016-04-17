<style lang=less>
</style>

<template>
</div>
<div v-show="user_info.user_name != '' " class="ui simple dropdown item">
  <i class="dropdown icon"></i> {{user_info.user_name}}
  <div class="menu">
    <slot name="one"></slot>
    <slot name="two"></slot>
    <slot name="three"></slot>
  </div>
</div>
<a href="/" v-show="user_info.user_name === '' " class="item">
  登录
</a>
</div>
</template>

<script>
  import store from '../store'
  import {queryUserInfo} from '../store/actions'
  export default {
    store,
    vuex: {
      actions: {
        queryUserInfo
      }
    },
    computed: {
      user_name () {
        return store.state.user_info.user_name
      },
      user_info () {
        return store.state.user_info
      }
    },
    ready () {
      this.queryUserInfo()
    },
    methods: {
    }
  }
</script>
