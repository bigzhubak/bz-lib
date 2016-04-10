<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>ScriptLoader</h1>
    <p>
      js 非阻塞加载模块
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">并不能知道是否已经加载完毕，后续要支持loader时候的属性传递</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <script-loader :scripts="scripts"></script-loader>
  </div>
</template>

<script>
  import ScriptLoader from './ScriptLoader.vue'
  export default {
    components: {
      ScriptLoader
    },
    data: function () {
      return {
        parms: [
          { parm: 'scripts', desc: 'js 的url 列表' }
        ],
        code: `<script-loader :scripts="scripts"></script-loader>`,
        scripts: [
          '//github.atool.org/canvas-nest.min.js'
        ]
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
