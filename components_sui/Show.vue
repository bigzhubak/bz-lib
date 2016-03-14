<style lang="less">
</style>

<template>
  <div class="content native-scroll">
    <div class="content-inner">
      <list-block-route :items="components"></list-block-route>
    </div>
  </div>
</template>

<script>
  //  import store from '../store'
  import ListBlockRoute from './ListBlockRoute'
  export default {
    props: [],
    components: {
      ListBlockRoute
    },
    data: function () {
      return {
        components: [
          {name: 'ListBlockRoute', desc: '列表'}
        ]
      }
    },
    ready () {
    },
    methods: {
    }
  }
</script>
