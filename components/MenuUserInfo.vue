<style lang=less>
</style>

<template>
</div>
<div v-show="user_info.user_name != '' " class="ui simple dropdown item">
   <img :src="avatar" class="ui avatar image">
  <div class="menu">
    <slot name="two"></slot>
    <slot name="three"></slot>
  </div>
</div>
<slot v-show="user_info.user_name === '' " name="one"></slot>
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
      },
      avatar () {
        return store.state.user_info.picture
      }
    },
    ready () {
      this.queryUserInfo()
    },
    methods: {
    }
  }
</script>
