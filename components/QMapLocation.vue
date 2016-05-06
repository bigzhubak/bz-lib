<style lang=less>
</style>

<template>
  <div>
    <img @click="toLocation"  class="ui image locationicon" src="../images/icon_location.png"><img>
    <img @click="toLocation"  class="ui image locationicon" src="../images/icon_location.png"><img>
    <iframe id="geoPage" width=0 height=0 frameborder=0  style="display:none;" scrolling="no"
      src="http://apis.map.qq.com/tools/geolocation?key=OB4BZ-D4W3U-B7VVO-4PJWW-6TKDJ-WPB77&referer=myapp">
    </iframe>
  </div>
</template>

<script>
  import store from '../store'
  import $ from 'jquery'
  export default {
    props: [],
    components: {
    },
    computed: {
    },
    data: function () {
      return {
        marker: null,
        location: null
      }
    },
    ready () {
      this.checkMapOk()
      this.addlistener()
      this.$on('removeLocationListener', this.removeListener)
    },
    methods: {
      insertButton: function () {
        if ($('.locationicon')[0]) {
          console.log($('.locationicon')[0])
          window.qq_map.controls[window.qq.maps.ControlPosition.BOTTOM_RIGHT].push($('.locationicon')[0])
          console.log('insert ok')
        }
      },
      checkMapOk: function () {
        if (typeof window.qq_map !== 'undefined') {
          this.insertButton()
        } else {
          setTimeout(this.checkMapOk, 100)
        }
      },
      removeListener: function () {
        window.removeEventListener('message', this.rsync, false)
      },
      rsync: function (event) {
        // 接收位置信息
        var loc = event.data
        store.actions.setLocation(loc)
        this.location = loc
        // console.log('location', loc)
      },
      addlistener: function () {
        window.addEventListener('message', this.rsync, false)
      },
      toLocation: function () {
        if (!this.location) { // 还没取到当前位置
          return
        }
        this.toPsotion(this.location.lat, this.location.lng)
      },
      toPsotion: function (lat, lng) {
        var position = new window.qq.maps.LatLng(lat, lng)
        window.qq_map.panTo(position)
        this.setMark(position)
      },
      setMark: function (location) {
        // 腾讯没有提供删除覆盖物的方法，只能临时避免建立多个敷盖物
        if (!this.marker) {
          // 创建marker
          this.marker = new window.qq.maps.Marker(
            {
              position: location,
              map: window.qq_map,
              animation: window.qq.maps.MarkerAnimation.DROP
            }
          )
          // 添加提示窗
          this.info = new window.qq.maps.InfoWindow(
            {
              map: window.qq_map
            }
          )
        } else {
          this.marker.setPosition(location)
        }
      }
    }
  }
</script>
