<style lang=less>
</style>

<template>
  <div class="ui small test modal transition hidden">
    <div class="header">
      {{header}}
    </div>
    <div v-html="content" class="content">
    </div>
    <div class="actions">
      <div class="ui negative button">
        取消
      </div>
      <div @click="yes" class="ui positive right labeled icon button">
        确认
        <i class="checkmark icon"></i>
      </div>
    </div>
  </div>
</template>

<script>
  // import store from '../store'
  import $ from 'jquery'
  export default {
    props: ['header', 'content', 'call_back'],
    ready () {
      this.$on('confirm', this.showConfirm)
      // if (!this.id) {
      //   this.id = 'confirm'
      // }
    },
    methods: {
      yes: function () {
        this.call_back()
      },
      showConfirm: function () {
        $(this.$el).modal('show')
      }
    }
  }
</script>
