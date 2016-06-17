<style lang="less">
</style>

<template>
  <div class="ui segment">
    <h1>Clipboard</h1>
    <p>
    页面剪贴板 
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="2">注意，将父组件内容插入到slot中</td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <Clipboard>
      <input type="text" v-model="massage">
    </Clipboard>
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
      massage: '复制到clipborad的内容',
      code: `<Clipboard><input type="text"></Clipboard>`
    }
  }
}
</script>
