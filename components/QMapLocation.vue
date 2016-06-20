<style lang="less">
</style>

<template>
  <div v-show="false"></div>
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
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.setLoc, this.showError)
      } else {
        console.log('系统不支持')
      }
    },
    computed: {
    },
    methods: {
      setLoc: function (position) {
        console.log(position)
        this.loc = {}
        this.loc.lat = position.coords.latitude
        this.loc.lng = position.coords.longitude
      },
      showError: function (error) {
        console.log(error)
      }
    }
  }
</script>
