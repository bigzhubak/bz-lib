<style lang="less">
  .weui_toast i.icon {
    font-size: 3em;
  }
  .weui_toast_content {
    padding-top: 1.2em;
  }
</style>

<template>
  <div :class="{'weui_loading_toast': type === 'loading'}">
    <div class="weui_mask_transparent"></div>
    <div class="weui_toast">
      <div v-if="type === 'loading'" class="weui_loading" >
        <div v-for="n in 12" class="weui_loading_leaf" :class="'weui_loading_leaf_' + n"></div>
      </div>
      <i v-if="type === 'success'" class="weui_icon_toast" ></i>
      <i v-if="type === 'warning'" class="warning sign icon" ></i>
      <i v-if="type === 'info'" class="info icon" ></i>
      <div class="weui_toast_content"><slot></slot></div>
    </div>
  </div>
</template>

<script>
  import '../static/weui.min.css'
  export default {
    props: {
      type: {
        type: String,
        required: false,
        default: 'loading'
      }
    },
    computed: {
    },
    components: {
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
