<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>BottomLoader</h1>
    <p>
      滚动到底部以后，加载更多内容
    </p>
    <table class="ui celled table">
      <thead>
        <tr><th>参数</th><th>说明</th></tr>
      </thead>
      <tbody>
        <tr v-for="parm in parms"> <td class="single line"> {{parm.parm}} </td> <td> {{parm.desc}} </td></tr>
        <tr>
          <td colspan="2">注意，如果使用的组件有路由，那么最好在切换路由的时候发送消息，解除绑定(参看本例子) <code>this.$broadcast('unbind-scroll')</code></td>
        </tr>
      </tbody>
    </table>
    <code v-text="code">
    </code>
    <div class="ui divider"></div>
    <div class="ui grid">
      <div  v-for="data in datas" class="sixteen wide column">
        <div class="ui card">
          <div class="content">
            <a class="description">{{data}}</a>
          </div>
        </div>
      </div>
    </div>

    <bottom-loader :el="$el" element_class=".ui.card" :call_back="call_back"></bottom-loader>
  </div>
</template>

<script>
  import BottomLoader from './BottomLoader.vue'
  export default {
    components: {
      BottomLoader
    },
    route: {
      deactivate: function (transition) {
        this.$broadcast('unbind-scroll')
        console.log('解除了scroll绑定')
        transition.next()
      }
    },
    data: function () {
      return {
        datas: [1],
        parms: [
          {parm: 'el', desc: '使用该组件的el,主要为了把查找last限定在本el中. !注意, fragment的el是无法传递进去的'},
          {parm: 'element_class', desc: '用于定位last的class .hah.jj 的格式'},
          {parm: 'call_back', desc: '滚到底部的回调函数'}
        ],
        code: `<bottom-loader :el="$el" element_class=".ui.card" :call_back="call_back"></bottom-loader>`
      }
    },
    methods: {
      call_back: function () {
        this.datas.push(this.datas.length + 1)
      },
      run: function () {
        this.$broadcast('confirm')
      }
    }
  }
</script>
