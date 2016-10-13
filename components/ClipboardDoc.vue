<style lang="less">
</style>

<template>
  <div class="ui segment">
    <h1>{{title}}</h1>
    <p>
      {{desc}}
    </p>
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
    <clipboard :content="message">
    </clipboard>
  </div>
</template>

<script>
  import Clipboard from './Clipboard.vue'
  export default {
    components: {
      Clipboard
    },
    data: function () {
      return {
        title: 'Clipboard',
        desc: '点击复制',
        parm_desc: `注意，要把ZeroClipboard.swf 放到 /static/ZeroClipboard.swf 才能使用`,
        message: '复制到clipborad的内容',
        code: `<Clipboard><input type="text"></Clipboard>`,
        parms: [
          {parm: 'content', desc: '要copy的文本内容'}
        ]
      }
    }
  }
</script>
