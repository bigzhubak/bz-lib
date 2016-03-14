<style lang="less">
</style>

<template>
  <div class="list-block">
    <ul>
      <li v-for="item in items" >
        <a v-link="{name: item.name}" class="item-link item-content">
          <div class="item-inner">
            <div class="item-title">{{item.name}}: {{item.desc}}</div>
          </div>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
  // import store from '../store'
  export default {
    props: ['items'],
    components: {
    },
    data: function () {
      return {
      }
    },
    ready () {
    },
    methods: {
    }
  }
</script>
