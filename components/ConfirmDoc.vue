<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>Confirm</h1>
    <p>
      用来弹出semantic-ui的"是"和"否"的确认弹出窗口
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">
            注意，触发弹出窗口使用 <code>this.$broadcast('confirm')</code>
            <br>
            继承自 modal
          </td>
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
    <confirm header="标题内容" content="内容正文" :call_back="call_back">
    </confirm>
  </div>
</template>

<script>
  import Confirm from './Confirm.vue'
  export default {
    components: {
      Confirm
    },
    data: function () {
      return {
        parms: [
          {parm: 'header', desc: '标题内容'},
          {parm: 'content', desc: '正文内容'},
          {parm: 'call_back', desc: '点击确认后的回调函数'}
        ],
        code: `<confirm header="标题内容" content="内容正文" :call_back="call_back"></confirm>`
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
