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
        <tr>
          <td colspan="2">这货没有参数, 目前只有logout一个操作</td>
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
      run: function () {
        alert('用不着运行，这货是直接运行的')
      }
    }
  }
</script>
