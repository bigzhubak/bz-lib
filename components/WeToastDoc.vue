<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>{{name}}</h1>
    <p>
      {{desc}}
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
    <button @click="run('loading')" class='ui basic button'>
      <i class='icon play'></i>
      loading
    </button>
    <button @click="run('warning')" class='ui basic button'>
      <i class='icon play'></i>
      warning
    </button>
    <button @click="run('info')" class='ui basic button'>
      <i class='icon play'></i>
      info
    </button>

    <button @click="run('success')" class='ui basic button'>
      <i class='icon play'></i>
      success
    </button>

    <we-toast v-show="type==='loading'">
      数据加载中
    </we-toast>
    <we-toast type="warning" v-show="type==='warning'">
      警告你哦
    </we-toast>
    <we-toast type="info" v-show="type==='info'">
      提示信息
    </we-toast>
    <we-toast type="success" v-show="type==='success'">
      成功啦
    </we-toast>
  </div>
</template>

<script>
  import WeToast from './WeToast'
  export default {
    components: {
      WeToast
    },
    data: function () {
      return {
        type: '',
        desc: '用来弹出we-ui的信息提示',
        name: 'WeToast',
        parms: [
          {parm: 'type', desc: 'loading warning info success 任意选一种，默认 loading'}
        ],
        code: `
        <we-toast v-show="type==='loading'">
        数据加载中
        </we-toast>
        `
      }
    },
    methods: {
      run: function (type) {
        this.type = type
        setTimeout(
          () => {
            this.type = ''
          }, 3000
        )
      }
    }
  }
</script>
