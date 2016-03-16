<style lang="less">
  .ui.header.center.vertical-bz {
    margin-top:1em;
  }
  .ui.tiny.image.quesu{
    margin-top:6.5em;
  }
  .ui.header.center.desc-bz{
    margin-left:0.5em;
    margin-right:0.5em;
  }
  .ui.middle.aligned.tiny.image {
    margin-left:0.5em;
    margin-right:0.5em;
  }

  .ui.tiny.image {
    width:4em;
  }
  .ui.header.center {
    display: inline-block;
  }
  .ui.middle.aligned.tiny.image{
    vertical-align: -50% 
  }
</style>


<template>
  <v-swiper></v-swiper>
  <div class="ui middle aligned center aligned internally celled grid">
    <div class="seven wide column">
      <h3 class="ui header center vertical-bz">缺素图谱
        <div class="sub header">精准测量</div>
      </h3>
      <img class="ui centered tiny image quesu" :src="icon_btn_quesu"></img>
    </div>
    <div class="nine wide column">
      <img class="ui middle aligned tiny image zhishi" :src="icon_btn_knowledge"></img>
      <h3 class="ui header center desc-bz">知识普及
        <div class="sub header">行业知识</div>
      </h3>
      <div class="ui section divider"> </div>
      <h3 class="ui header center desc-bz">鉴别化肥
        <div class="sub header">全面了解</div>
      </h3>
      <img class="ui middle aligned tiny image jianbie" :src="icon_btn_jianbie"></img>
    </div>
  </div>
</template>

<script>
  // import store from '../store'
  import VSwiper from './VSwiper'
  import {Grids, Grid} from 'vue-weui'

  import icon_btn_jianbie from '../images/icon_btn_jianbie.png'
  import icon_btn_knowledge from '../images/icon_btn_knowledge.png'
  import icon_btn_quesu from '../images/icon_btn_quesu.png'

  export default {
    props: [],
    components: {
      Grids,
      Grid,
      VSwiper
    },
    data: function () {
      return {
        icon_btn_jianbie: icon_btn_jianbie,
        icon_btn_knowledge: icon_btn_knowledge,
        icon_btn_quesu: icon_btn_quesu
      }
    },
    ready () {
    },
    methods: {
    }
  }
</script>
