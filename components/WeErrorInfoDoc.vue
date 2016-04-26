<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>WeErrorInfo</h1>
    <p>
      用来弹出we-ui的错误提示图标
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">注意，触发弹出窗口使用 <code>store.actions.setErrorInfo('test')</code></td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <button @click='run' class='ui basic button'>
      <i class='icon play'></i>
      运行
    </button>
    <we-error-info :show_time='1000'></we-error-info>
  </div>
</template>

<script>
  import WeErrorInfo from './WeErrorInfo.vue'
  import store from '../store'
  export default {
    components: {
      WeErrorInfo
    },
    data: function () {
      return {
        parms: [
          {parm: 'show_time', desc: '提示框持续时间'}
        ],
        code: `<we-error-info :show_time='2000'></we-error-info>`
      }
    },
    methods: {
      run: function () {
        store.actions.setErrorInfo('test')
        return
      }
    }
  }
</script>
