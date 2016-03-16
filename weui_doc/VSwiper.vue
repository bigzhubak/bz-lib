<style lang="less">
  .img.slide {
    height: 16em
  }
  .white-bz {
    background-color: white
  }
  .swiper-pagination {
    top: 90%;
    .swiper-pagination-bullet{ opacity: 1; }
    .swiper-pagination-bullet-active{ background: white; opacity: 1; }
  }
</style>

<template>
  <div class="swiper-container">
    <div class="swiper-wrapper">
      <div class="swiper-slide"><img class="img slide" src="../images/banner.jpg" alt=""></div>
      <div class="swiper-slide"><img class="img slide" src="../images/farm.jpg" alt=""></div>
    </div>
    <div class="swiper-pagination"></div>
  </div>
</template>

<script>
  // import store from '../store'

  import 'swiper/dist/css/swiper.min.css'
  import Swiper from 'swiper'
  export default {
    props: [],
    components: {
    },
    data: function () {
      return {
        remove_card: {},
        card_numbers: ''
      }
    },
    ready () {
      var conf = {
        speed: 1400,
        spaceBetween: 100,
        autoplay: 3000,
        loop: true,
        // If we need pagination
        pagination: '.swiper-pagination'
        // Navigation arrows
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        // And if we need scrollbar
        // scrollbar: '.swiper-scrollbar'
      }
      Swiper('.swiper-container', conf)
    },
    methods: {
    }
  }
</script>
