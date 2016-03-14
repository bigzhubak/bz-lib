<style less>
  [v-cloak] {
    display: none;
  }
  .fade-transition {
    transition: opacity .3s ease;
  }
  .fade-enter, .fade-leave {
    opacity: 0;
  }
</style>

<template>
  <div class="page page-current">
    <header class="bar bar-nav">
      <a class="button button-link button-nav pull-left back" href="/sui.html#!/">
        <span class="icon icon-left"></span>
        首页
      </a>
      <h1 class="title">用vue封装的sui mobile</h1>
    </header>
    <router-view transition="fade" transition-mode="out-in" keep-alive></router-view>
  </div>
</template>

<script>
  //  import $ from 'zepto'
  export default {
    data () {
      return {
        components: [
          {name: 'ListBlockRoute', desc: '列表'}
        ]
      }
    },
    watch: {
    },
    ready () {
    },
    components: {
    },
    computed: {
    },
    methods: {
    }
  }
</script>
