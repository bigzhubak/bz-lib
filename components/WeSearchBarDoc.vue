<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>WeSearchBar</h1>
    <p>
      weui 的 searchbar 封装
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">注意，触发弹出窗口使用 <code>this.$broadcast('confirm')</code></td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <we-search-bar :search="run" :focus_run="focus"></we-search-bar>
  </div>
</template>

<script>
  import WeSearchBar from './WeSearchBar.vue'
  export default {
    components: {
      WeSearchBar
    },
    data: function () {
      return {
        parms: [
          {parm: 'search', desc: '按下查找的回调函数'},
          {parm: 'focus_run', desc: '焦点时候的回调函数(可以不传入)'}
        ],
        code: `<we-search-bar :search="run" :focus_run="focus"></we-search-bar>`
      }
    },
    methods: {
      call_back: function () {
        window.alert('点击了确认')
      },
      run: function (a) {
        window.alert('查找:' + a)
      },
      focus: function () {
        console.log('focus时候，干些什么')
      }
    }
  }
</script>
