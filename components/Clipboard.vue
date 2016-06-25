<style lang="less">
</style>

<template>
  <div class="ui left action input inline field">
    <button class="ui teal icon button clipboard" @mouseenter="copyEnter" @mouseleave="copyLeave" data-content="" >
      <i class="copy icon"></i>
    </button>
    <input readonly="true" type="text" @focus="selectAll" v-model="content">
  </div>
</template>

<script>
  import $ from 'jquery'
  import ZeroClipboard from 'zeroclipboard'
  export default {
    props: {
      content: {
        required: true,
        type: String
      }
    },
    components: {
    },
    data: function () {
      return {}
    },
    ready () {
      ZeroClipboard.config({swfPath: '/static/ZeroClipboard.swf'})
    },
    methods: {
      selectAll: function (event) {
        $(event.target).select()
      },
      copyEnter: function (event) {
        $('.button.clipboard').popup({position: 'left center', content: '点击复制内容'})
        let client = new ZeroClipboard($(event.target))
        client.on('copy', function (event) {
          let content = $(event.target).next().val()
          event.clipboardData.setData('text/plain', content)
          $('.button.clipboard').popup({content: '已复制', position: 'left center', on: 'click'})
        })
      },
      copyLeave: function () {
        $('.button.clipboard').popup('hide')
      }
    }
  }
</script>
