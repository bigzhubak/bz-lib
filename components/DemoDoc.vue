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
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">这货没有参数, 目前只有logout一个操作</td>
        </tr>
      </tbody>
    </table>
  </div>
  <pre>
  <code v-text="code">
  </code>
  </pre>
  <button @click='run' class='ui basic button'>
    <i class='icon play'></i>
    运行
  </button>
  <confirm header="标题内容" content="内容正文" :call_back="call_back"></confirm>
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
        code: "<menu-user-info></menu-user-info>"
      }
    },
    methods: {
      run: function () {
        alert('用不着运行，这货是直接运行的')
      }
    }
  }
</script>
