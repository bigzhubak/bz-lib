<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>{{name}}</h1>
    <p>{{desc}}</p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-show="parm_desc">
          <td colspan="2" v-html="parm_desc"></td>
        </tr>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <button v-show="run" @click='run' class='ui basic button'>
      <i class='icon play'></i>
      运行
    </button>
    <confirm header="标题内容" content="内容正文" :call_back="call_back"></confirm>
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
        title: 'Demo',
        desc: '就是个demo用来做模板',
        parm_desc: `注意，触发弹出窗口使用 <code>this.$broadcast('confirm')</code>`,
        parms: [
          {parm: 'parm1', desc: '参数1'},
          {parm: 'parm2', desc: '参数2'},
          {parm: 'parm3', desc: '参数3'}
        ],
        code: `<confirm header="标题内容" content="内容正文" :call_back="call_back"></confirm>`
      }
    },
    methods: {
      call_back: function () {
        window.alert('点击了确认')
      },
      run: function () {
        this.$broadcast('confirm')
      }
    }
  }
</script>
