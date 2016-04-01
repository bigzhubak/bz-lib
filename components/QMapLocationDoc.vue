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
          <td colspan="2"></td>
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
