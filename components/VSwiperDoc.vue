<style lang=less>
</style>

<template>
  <div class="ui segment">
    <h1>{{name}}</h1>
    <p>{{desc}}</p>
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
    <button v-show="run" @click='run' class='ui basic button'>
      <i class='icon play'></i>
      运行
    </button>
    <v-swiper>
      <div class="swiper-slide"><a v-link="{name: 'Demo'}"><img class="img slide" src="../images/tomato.jpg" alt=""></a></div>
      <div class="swiper-slide"><a v-link="{name: 'BottomLoader'}"><img class="img slide" src="../images/farm.jpg" alt=""></a></div>
    </v-swiper>
  </div>
</template>

<script>
  import VSwiper from './VSwiper.vue'
  export default {
    components: {
      VSwiper
    },
    data: function () {
      return {
        title: 'VSwiper',
        desc: '传说中的走马灯',
        parm_desc: `component中间加入要走的图片, 要加入class <code>swiper-slie</code>以后再想办想去了这个依赖`,
        parms: [
        ],
        code: `
          <v-swiper>
            <div class="swiper-slide"><a v-link="{name: 'Demo'}"><img class="img slide" src="../images/tomato.jpg" alt=""></a></div>
            <div class="swiper-slide"><a v-link="{name: 'BottomLoader'}"><img class="img slide" src="../images/farm.jpg" alt=""></a></div>
          </v-swiper>
        `
      }
    },
    methods: {
    }
  }
</script>
