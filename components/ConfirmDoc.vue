<style lang="less">
</style>

<template>
  <div>
    <h1>Confirm</h1>
    <p>
      用来弹出semantic-ui的"是"和"否"的确认弹出窗口
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr> <td class="single line"> header </td> <td> 标题内容 </td></tr>
        <tr> <td class="single line"> content </td> <td> 正文内容 </td></tr>
        <tr><td class="single line"> call_back </td> <td> 点击确认后的回调函数</td></tr>
        <tr>
          <td colspan="2">注意，触发弹出窗口使用 <code class=" language-javascript">this.$broadcast('confirm')</code></td>
        </tr>
      </tbody>
    </table>
  </div>
  <code>
  </code>
  <div class='ui center aligned basic segment'>
    <button @click='run' class='ui basic button'>
      <i class='icon play'></i>
      运行
    </button>
  </div>
  <confirm header="标题内容" content="内容正文" :call_back="call_back"></confirm>
</template>

<script>
  import Confirm from './Confirm.vue'
  export default {
    components: {
      Confirm
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
