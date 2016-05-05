<style lang=less>
</style>

<template>
  <modal>
    <div slot="header">
      {{header}}
    </div>
    <div v-html="content" slot="content">
    </div>
    <div slot="actions">
      <div class="ui negative button">
        取消
      </div>
      <div @click="yes" class="ui positive right labeled icon button">
        确认
        <i class="checkmark icon"></i>
      </div>
    </div>
  </modal>
</template>

<script>
  import Modal from './Modal'
  export default {
    components: {
      Modal
    },
    props: ['header', 'content', 'call_back'],
    ready () {
      this.$on('confirm', this.showConfirm)
    },
    methods: {
      yes: function () {
        this.call_back()
      },
      showConfirm: function () {
        this.$broadcast('modal')
      }
    }
  }
</script>
