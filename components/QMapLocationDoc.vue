<style lang="less">
  .map {
    width: 100%;
    height: 500px;
  }
</style>

<template>
  <div class="ui segment">
    <h1>{{name}}</h1>
    <p>
      {{desc}}
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <q-map :config_map="configMap" class="map"></q-map>
    <q-map-location :loc.sync="loc" ></q-map-location>
    <img @click="toLocation" id="location" class="ui image" src="/static/images/icon_location.png"><img>
  </div>
</template>

<script>
  import $ from 'jquery'
  import QMap from './QMap.vue'
  import QMapLocation from './QMapLocation.vue'
  export default {
    components: {
      QMap,
      QMapLocation
    },
    data: function () {
      return {

        marker: null,
        loc: null,
        name: 'QMapLocation',
        desc: '封装了qq map的定位插件，能取到当前位置',
        parms: [
          {parm: 'loc', desc: '当前位置，要开启 two way'}
        ],
        code: `<q-map-location :loc.sync="loc" ></q-map-location>`
      }
    },
    methods: {
      toLocation: function () {
        if (this.loc) {
          let position = new window.qq.maps.LatLng(this.loc.lat, this.loc.lng)
          window.q_map.panTo(position)
          this.setMark(position)
        } else {
          console.log('定位失败!')
          console.log(this.loc)
        }
      },
      setMark: function (position) {
        if (this.marker) {
          this.marker.setMap(null)
          this.marker = null
        }
        this.marker = new window.qq.maps.Marker(
          {
            position: position,
            map: window.q_map,
            animation: window.qq.maps.MarkerAnimation.DROP
          }
        )
      },
      configMap: function () {
        // 加入按钮
        window.q_map.controls[window.qq.maps.ControlPosition.BOTTOM_RIGHT].push($('#location')[0])
      }
    }
  }
</script>
