<style less>
  .main.container {
    margin-top: 4em;
  }
</style>

<template>
    <div class="ui grid container basic segment">
      <div class="four wide column">
        <header class="main-header">
          <nav class="ui vertical menu">
            <a class="header item" href="/#!/"><b>公用组件说明</b></a>
            <a class="item" v-link="{name:'Confirm'}" >Confirm</a>
            <a class="item" v-link="{name:'MenuUserInfo'}" >MenuUserInfo</a>
          </nav>
        </header>
      </div>
      <div class="twelve wide column">
        <router-view></router-view>
      </div>
    </div>
</template>

<script>
  export default {
    data () {
      return {
      }
    },
    components: {
    },
    computed: {
    },
    methods: {
    }
  }
</script>
