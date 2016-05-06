<style lang=less>
  .original-text-bz {
    /*保留空格*/
    white-space: pre-wrap;
    /*字体能自动换行*/
    word-wrap:break-word;
  }
  code {
    padding: 2px 4px;
    font-size: 90%;
    color: #c7254e;
    background-color: #f9f2f4;
    border-radius: 4px;
    .original-text-bz;
  }
</style>

<template>
  <div>
    <div class="ui stackable grid container basic segment">
      <div class="four wide column">
        <header class="main-header">
          <nav class="ui vertical menu">
            <a class="header item" href="/#!/"><b>公用组件说明</b></a>
            <div class="item">
              <div class="ui transparent icon input">
                <input v-model="key" @keyup.enter="showFirst" type="text" placeholder="Search ...">
                <i class="search icon"></i>
              </div>
            </div>
            <a v-show="c.name" v-for="c in components|filterBy key|orderBy 'name'" class="item componet" :data-content="c.desc" v-link="{name:c.name}" >{{c.name}}</a>
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
          <a class="item" href="#">Created by bz</a>
          <a class="item" target="_blank" href="http://semantic-ui.com">Semantic-UI</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  import _ from 'underscore'
  import router_conf from './router_conf.js'
  var components = _.values(router_conf)
  export default {
    data () {
      return {
        components: components,
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
      showFirst: function () {
        let target = $(this.$el).find('.componet')
        if (target.length > 0) {
          target[0].click()
        }
      }
    }
  }
</script>
