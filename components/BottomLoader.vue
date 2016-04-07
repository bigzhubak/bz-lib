<style lang="less">
</style>

<template>
  <br>
</template>

<script>
  import $ from 'jquery'
  import _ from 'underscore'
  export default {
    props: {
      el: {
        required: true
      },
      element_class: {
        required: true,
        type: String
      },
      call_back: {
        required: true
      }
    },
    events: {
      'unbind-scroll': function () {
        $(window).unbind('scroll')
      }
    },
    components: {
    },
    data: function () {
      return {
      }
    },
    ready () {
      this.bindScroll()
    },
    methods: {
      bindScroll: function () {
        $(window).scroll(_.throttle(this.doScroll, 200))
      },
      doScroll: function () {
        let last = $(this.el).find(this.element_class).last()
        if (!last.offset()) {
          return
        }
        // 最后一个元素 元素偏移量+元素高度 得到元素底部的像素高度
        // let offset_bottom = last.offset().top + last.height() + 14 - 1.12 // padding
        let offset_bottom = last.offset().top + last.height()// padding
        if ($(window).scrollTop() + $(window).height() > offset_bottom) { // 滚动像素 + 屏幕高度 > 最后一个元素的底部  已经到底部了
          // console.log('bottom')
          this.call_back()
        }
      }
    }
  }
</script>
