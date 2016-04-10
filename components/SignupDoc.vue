<style lang=less>
</style>

<template>
  <div class="page">
    <div class="ui segment ">
      <h1>Signup</h1>
      <p>
        注册
      </p>
      <table class="ui celled table">
        <thead>
          <tr><th>参数</th><th>说明</th></tr>
        </thead>
        <tbody>
          <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
          <tr>
            <td colspan="2"></td>
          </tr>
        </tbody>
      </table>
      <code v-text="code">
      </code>
      <div class="ui divider"></div>
      <signup :call_back="call_back"></signup>
    </div>
  </div>
</template>

<script>
  import Signup from './Signup.vue'
  export default {
    components: {
      Signup
    },
    data: function () {
      return {
        parms: [
          {parm: 'call_back', desc: '成功注册后要干的事，可以传入，也可以不传入'}
        ],
        code: '<signup :call_back="call_back"></signup>'
      }
    },
    methods: {
      call_back: function () {
        alert('注册成功了!')
      }
    }
  }
</script>
