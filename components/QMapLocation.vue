<style lang="less">
</style>

<template>
  <iframe id="geoPage" width=0 height=0 frameborder=0  style="display:none;" scrolling="no"
    src="http://apis.map.qq.com/tools/geolocation?key=OB4BZ-D4W3U-B7VVO-4PJWW-6TKDJ-WPB77&referer=myapp">
  </iframe>
</template>

<script>
  export default {
    props: {
      loc: {
        required: true,
        twoWay: true
      }
    },
    components: {
    },
    data: function () {
      return {
      }
    },
    ready () {
      window.addEventListener('message', this.rsync, false)
      this.$on('removeLocationListener', this.removeListener)
    },
    methods: {
      removeListener: function () {
        window.removeEventListener('message', this.rsync, false)
      },
      rsync: function (event) {
        this.loc = event.data
      }
    }
  }
</script>
