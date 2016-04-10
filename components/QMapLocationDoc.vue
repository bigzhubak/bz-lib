<style lang="less">
</style>

<template>
  <div class="ui segment map">
    <h1>QMapLocation</h1>
    <p>
      QMap 的附加组件，能够定位当前位置
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">失败了！<br>腾讯地图在 app dom 到地图里后，会删除原先的dom
vue 的 component 在路由切换的时候，并不会完全重新传染 html，导致第二次路由切换进共来后，找不到定位按钮这个dom了（之前被腾讯地图删除了）</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <q-map></q-map>
    <q-map-location></q-map-location>
  </div>
</template>

<script>
  import QMap from './QMap.vue'
  import QMapLocation from './QMapLocation.vue'
  export default {
    components: {
      QMap,
      QMapLocation
    },
    data: function () {
      return {
        parms: [
        ],
        code: `<q-map></q-map>`
      }
    },
    methods: {
      call_back: function () {
        alert('点击了确认')
      },
      run: function () {
        this.$broadcast('confirm')
      }
    }
  }
</script>
