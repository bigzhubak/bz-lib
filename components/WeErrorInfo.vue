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
  import store from '../store'
  export default {
    props: {
      show_time: { // 显示时长
        type: Number,
        default: 3000
      }
    },
    computed: {
      error_info: function () {
        return store.state.error_info
      }
    },
    components: {
    },
    watch: {
      'error_info': function (val, oldVal) {
        console.log(val)
        console.log(oldVal)
        if (!val) {
          return
        }
        console.log(val)
        setTimeout(
          () => {
            store.actions.setErrorInfo(null)
          }, this.show_time
        )
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
