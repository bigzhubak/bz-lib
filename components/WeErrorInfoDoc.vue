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
          <td colspan="2">注意，触发弹出窗口通过修改 error_info </td>
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
    <we-error-info :error_info.sync="error_info" :show_time='1000'></we-error-info>
  </div>
</template>

<script>
  import WeErrorInfo from './WeErrorInfo.vue'
  export default {
    components: {
      WeErrorInfo
    },
    data: function () {
      return {
        error_info: '',
        parms: [
          {parm: 'show_time', desc: '提示框持续时间, 0 的时候不自动消失'},
          {parm: 'error_info', desc: '错误信息, 要用sync的方式传入，否则其无法改变，第二次就无法设置了'},
        ],
        code: `<we-error-info :error_info.sync="error_info" :show_time='1000'></we-error-info>`
      }
    },
    methods: {
      run: function () {
        this.error_info = 'test'
      }
    }
  }
</script>
