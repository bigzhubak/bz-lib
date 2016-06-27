<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>Modal</h1>
    <p>
      
    <p>{{desc}}</p>
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">注意，触发弹出窗口使用 <code>this.$broadcast('modal')</code></td>
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
    <modal :show_close="true">
      <div class="header">
        这是标题
      </div>
      <div class="content">
        这是内容
      </div>
      <div class="actions">
        这是操作
      </div>
    </modal>
  </div>
</template>

<script>
  import Modal from './Modal.vue'
  export default {
    components: {
      Modal
    },
    data: function () {
      return {
        desc: '用来弹出semantic-ui的 modal 窗口',
        parms: [
          {parm: 'show_close', desc: '是否显示关闭按钮'}
        ],
        code: `
          <modal :show_close="true">
            <div class="header">
              这是标题
            </div>
            <div class="content">
              这是内容
            </div>
            <div class="actions">
              这是操作
            </div>
          </modal>
        `
      }
    },
    methods: {
      call_back: function () {
        window.alert('点击了确认')
      },
      run: function () {
        this.$broadcast('modal')
      }
    }
  }
</script>
