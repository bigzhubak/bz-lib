<style lang="less">
</style>

<template>
  <header class="bar bar-nav">
    <a class="button button-link button-nav pull-left back" href="/demos/bar">
      <span class="icon icon-left"></span>
      返回
    </a>
    <a class="button button-link button-nav pull-right">
      下一步
      <span class="icon icon-right"></span>
    </a>
    <h1 class="title">标题</h1>
  </header>
</template>

<script>
  import store from '../store'
  export default {
    props: [],
    components: {
    },
    data: function () {
      return {
        remove_card: {},
        card_numbers: ''
      }
    },
    ready () {
    },
    methods: {
    }
  }
</script>
