<style lang="less">
  .ui.button.oauth {
    margin: 0.75em
  }
</style>

<template>
  <a v-for="oauth in oauths" href="/{{oauth}}" class="ui {{oauth}} button oauth">
    <i class="{{oauth}} icon"></i>
    {{upperFirst(oauth)}}
  </a>
</template>

<script>
  export default {
    props: ['oauths'],
    computed: {
    },
    components: {
    },
    data: function () {
      return {
      }
    },
    ready () {
    },
    methods: {
      upperFirst: function (string) {
        return string.charAt(0).toUpperCase() + string.substring(1).toLowerCase()
      }
    }
  }
</script>
