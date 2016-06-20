<style lang="less">
</style>

<template>
  <div class="ui left action input inline field">
    <button class="ui teal icon button clipboard" @mouseenter="copyEnter" @mouseleave="copyLeave" data-content="" >
      <i class="copy icon"></i>
    </button>
    <slot></slot>
  </div>
</template>

<script>
  import $ from 'jquery'
  import ZeroClipboard from 'zeroclipboard'
  export default {
    props: [],
    components: {
    },
    data: function () {
      return {}
    },
    ready () {
      ZeroClipboard.config({swfPath: '/static/ZeroClipboard.swf'})
    },
    methods: {
      copyEnter: function (event) {
        $('.button.clipboard').popup({position: 'left center', content: 'Copy to clipboard'})
        let client = new ZeroClipboard($(event.target))
        client.on('copy', function (event) {
          let content = $(event.target).next().val()
          event.clipboardData.setData('text/plain', content)
          $('.button.clipboard').popup({content: 'Copied', position: 'left center', on: 'click'})
        })
      },
      copyLeave: function () {
        $('.button.clipboard').popup('hide')
      }
    }
  }
</script>
