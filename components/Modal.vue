<style lang=less>
</style>

<template>
  <div class="ui small test modal transition hidden">
    <i v-show="show_close" class="close icon"></i>
    <slot></slot>
  </div>
</template>

<script>
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
