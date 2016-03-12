<style less>
  code {
    padding: 2px 4px;
    font-size: 90%;
    color: #c7254e;
    background-color: #f9f2f4;
    border-radius: 4px;
  }
</style>

<template>
  <div class="ui grid container basic segment">
    <div class="four wide column">
      <header class="main-header">
        <nav class="ui vertical menu">
          <a class="header item" href="/#!/"><b>公用组件说明</b></a>
          <div class="item">
            <div class="ui transparent icon input">
              <input v-model="key" type="text" placeholder="Search ...">
              <i class="search icon"></i>
            </div>
          </div>
          <a v-for="c in components|filterBy key|orderBy 'name'" class="item" :data-content="c.desc" v-link="{name:c.name}" >{{c.name}}</a>
        </nav>
      </header>
    </div>
    <div class="twelve wide column">
      <router-view></router-view>
    </div>
  </div>
  <div class="ui vertical footer segment">
    <div class="ui center aligned container">
      <div class="ui horizontal small divided link list">
        <a class="item" href="/sui.html">mobile version</a>
        <a class="item" href="#">created by bz</a>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    data () {
      return {
        components: [
          {name: 'Oauth2', desc: 'Oauth2登录'},
          {name: 'Login', desc: '登录'},
          {name: 'Signup', desc: '用户注册'},
          {name: 'CountUp', desc: '数字渐变效果'},
          {name: 'MenuUserInfo', desc: 'Menu上显示用户信息'},
          {name: 'Confirm', desc: '确认提示框'}
        ],
        key: ''
      }
    },
    watch: {
      // 过滤导致重新渲染menu, 这里重新让pop生效
      'key': function (val, oldVal) {
        $(this.$el).find('.item').popup({ position: 'right center'})
      }
    },
    ready () {
      $(this.$el).find('.item').popup({ position: 'right center'})
    },
    components: {
    },
    computed: {
    },
    methods: {
    }
  }
</script>
