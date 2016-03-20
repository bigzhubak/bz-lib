<style lang="less">
</style>

<template>
  <div class="ui segment">
    <h1>Oauth2</h1>
    <p>
      生成 Oauth2 按钮
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr v-show="parms.length===0">
          <td colspan="2"></td>
        </tr>
      </tbody>
    </table>
    <code v-text="code"></code>
    <div class="ui divider"></div>
    <oauth2 :oauths="oauths"></oauth2>
  </div>
</template>

<script>
  import Oauth2 from './Oauth2.vue'
  export default {
    components: {
      Oauth2
    },
    data: function () {
      return {
        oauths: [
          'vk',
          'youtube',
          'facebook',
          'google plus',
          'twitter',
          'github',
          'instagram'
        ],
        parms: [
          {parm: 'oauths', desc: '一个list, 指定要显示的oauth方式: ' + `['vk', 'twitter']`}
        ],
        code: '<oauth2 :oauths="oauths"></oauth2>'
      }
    },
    methods: {
      run: function () {
        alert('用不着运行，这货是直接运行的')
      }
    }
  }
</script>
