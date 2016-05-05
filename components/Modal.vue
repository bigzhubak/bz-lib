<style lang=less>
</style>

<template>
  <div class="ui small test modal transition hidden">
    <i v-show="show_close" class="close icon"></i>
    <div class="header">
      <slot name="header"></slot>
    </div>
    <div class="content">
      <slot name="content"></slot>
    </div>
    <div class="actions">
      <slot name="actions"></slot>
    </div>
  </div>
</template>

<script>
  // import store from '../store'
  import $ from 'jquery'
  export default {
    props: {
      show_close: {
        default: false
      }
    },
    ready () {
      this.$on('modal', this.showModal)
    },
    methods: {
      showModal: function () {
        $(this.$el).modal('show')
      }
    }
  }
</script>
