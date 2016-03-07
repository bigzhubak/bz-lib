<style lang="less">
</style>

<template>
  <div>
    <div class="ui center aligned secondary segment">
      <b>用户登录</b>
    </div>
    <div class="ui segment">
      <div v-show="oauths" class="ui two column middle aligned very relaxed stackable grid">
        <div class="center aligned column">
          <div class="ui large">
            <oauth2-button  v-for="oauth in oauths" :oauth="oauth"></oauth2-button>
          </div>
        </div>
        <div class="ui vertical divider">Or </div>
        <div class="center aligned column">
          <form class="ui form fluid ">
            <div class="field">
              <label>用户名</label>
              <input @focus="cleanError" v-model="user_name" placeholder="请输入邮箱/用户名" type="text">
            </div>
            <div class="field">
              <label>密码</label>
              <input v-model="password" @keyup.enter="login" @focus="cleanError" placeholder="请输入密码"  type="password">
            </div>
            <a @click="login" class="ui blue submit button">登录</a>
          </form>
          <div v-show="error_info" class="ui bottom warning message">
            <i class="icon help"></i>
            (%error_info%)
          </div>
        </div>
      </div>
      <div v-show="oauths==undefined" class="center aligned column">
        <form class="ui form fluid ">
          <div class="field">
            <label>用户名</label>
            <input @focus="cleanError" v-model="user_name" placeholder="请输入邮箱/用户名" type="text">
          </div>
          <div class="field">
            <label>密码</label>
            <input v-model="password" @keyup.enter="login" @focus="cleanError" placeholder="请输入密码"  type="password">
          </div>
          <a @click="login" class="ui blue submit button">登录</a>
        </form>
        <div v-show="error_info" class="ui bottom warning message">
          <i class="icon help"></i>
          (%error_info%)
        </div>
      </div>
    </div>


    <div class="ui small test modal">
      <div class="header">
        不存在用户
      </div>
      <div class="content">
        <p>还没有用户(%user_name%),是否建立?</p>
      </div>
      <div class="actions">
        <div class="ui negative button">
          不用
        </div>
        <div @click="signup" class="ui positive right labeled icon button">
          好的
          <i class="checkmark icon"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  // import store from '../store'
  export default {
    props: [],
    components: {
      'oauth2-button': require('./oauth2-button')
    },
    data: function () {
      return {
        user_name: '',
        password: ''
      }
    },
    ready () {
    },
    methods: {
      login: function () {
      }
    }
  }
</script>
