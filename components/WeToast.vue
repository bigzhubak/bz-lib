<style lang="less">
  .weui_toast i.icon {
    font-size: 3em;
  }
  .weui_toast_content {
    padding-top: 1.2em;
  }
</style>

<template>
  <div v-show="error_info">
    <div class="weui_mask_transparent"></div>
    <div class="weui_toast">
      <i class="warning sign icon"></i>
      <p class="weui_toast_content">{{error_info}}</p>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      show_time: { // 显示时长
        type: Number,
        default: 1000
      },
      error_info: {
        type: String,
        required: true
      }
    },
    computed: {
    },
    components: {
    },
    watch: {
      'error_info': function (val, oldVal) {
        if (!val) {
          return
        }
        if (this.show_time !== 0) { // 定时消失
          let _this = this
          setTimeout(
            () => {
              _this.error_info = ''
            }, this.show_time
          )
        }
      }
    },
    data: function () {
      return {
      }
    },
    ready () {
    },
    methods: {
    }
  }
</script>
