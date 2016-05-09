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
        <tr>
          <td colspan="2"></td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <q-map class="map"></q-map>
  </div>
</template>

<script>
  import QMap from './QMap.vue'
  export default {
    components: {
      QMap
    },
    data: function () {
      return {
        name: 'Qmap',
        desc: '目前就是简单的显示了一个腾讯地图, 解决了资源加载问题, 但是污染了window.initMap 名字空间, 以后功能再添加',
        parms: [
        ],
        code: `<q-map></q-map>`
      }
    },
    methods: {
      run: function () {
      }
    }
  }
</script>
