O
<style lang="less">
  #map-container {
    min-width: 500px;
    min-height: 500px;
  }
  /*屏蔽腾讯logo */
  div[style="position: absolute; z-index: 1000000; -webkit-user-select: none; left: 7px; bottom: 0px; "],
  div[style="position: absolute; z-index: 1000000; margin: 2px 5px 0px 2px; left: 0px; bottom: 0px; "],
  div[style="position: absolute; z-index: 1000000; -webkit-user-select: none; left: 7px; bottom: 0px;"],
  div[style="position: absolute; z-index: 1000000; margin: 2px 5px 0px 2px; left: 0px; bottom: 0px;"],
  div[style="position: absolute; z-index: 1000000; -webkit-user-select: none; left: 87px; bottom: 0px; "],
  div[style="position: absolute; z-index: 1000000; -webkit-user-select: none; left: 87px; bottom: 0px;"] {
    display: none;
  }
</style>

<template>
  <div id="map-container"></div>
  <img @click="toLocation"  class="ui image locationicon" src="../images/icon_location.png"><img>
  <script-loader :scripts="scripts"></script-loader>
</template>

<script>
  import store from '../store'
  import ScriptLoader from './ScriptLoader'
  import $ from 'jquery'
  export default {
    components: {
      ScriptLoader
    },
    computed: {
    },
    data: function () {
      return {
        scripts: [
          '//map.qq.com/api/js?v=2.exp&callback=initMap'
        ]
      }
    },
    ready () {
      window.initMap = this.initMap
    },
    methods: {
      clearOverlays: function (overlays) { // 删除 mark
        var overlay = overlays.pop()
        while (overlay) {
          overlay.setMap(null)
          overlay = overlays.pop()
        }
      },
      toPsotion: function (lat, lng) {
        var position = new window.qq.maps.LatLng(lat, lng)
        this.map.panTo(position)
        this.setMark(position)
        store.actions.setPosition(position)
      },
      backToLast: function () {
        this.toPsotion(this.position.lat, this.position.lng)
      },
      toLocation: function () {
        if (!this.location) { // 还没取到当前位置
          this.toMiLe()
          return
        }
        this.toPsotion(this.location.lat, this.location.lng)
      },
      initMap: function () {
        window.qq_map = new window.qq.maps.Map(
          document.getElementById('map-container'), {
            zoom: 12,
            zoomControl: false,
            mapTypeId: window.qq.maps.MapTypeId.HYBRID,
            draggable: true,
            draggableCursor: 'crosshair',
            scrollwheel: true,
            disableDoubleClickZoom: true,
            mapTypeControl: false
          }
        )
        window.qq_map.controls[window.qq.maps.ControlPosition.BOTTOM_RIGHT].push($('.locationicon')[0])
      }
    }
  }
</script>
