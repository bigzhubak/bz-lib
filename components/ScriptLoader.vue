<style lang=less>
</style>

<template>
  <div>
  </div>
</template>

<script>
  // import store from '../store'
  export default {
    props: {
      scripts: {
        type: Array,
        required: true
      }
    },
    components: {
    },
    data: function () {
      return {
      }
    },
    ready () {
      for (var i in this.scripts) {
        this.addScript(this.scripts[i])
      }
      // 没有意义，根本不知道是否已经加载好了
      // this.$dispatch('script-load-done')
    },
    methods: {
      addScript: function (url) {
        var script = document.createElement('script')
        script.type = 'text/javascript'
        script.src = url
        document.body.appendChild(script)
      }
    }
  }
</script>
