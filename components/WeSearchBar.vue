<style lang="less">
</style>

<template>
  <div  v-bind:class="{ 'weui_search_focusing': is_focus || search_key}" class="weui_search_bar">
    <form v-on:submit.prevent="call" class="weui_search_outer">
      <div class="weui_search_inner">
        <i class="weui_icon_search"></i>
        <input v-model="search_key" @focus="focus" @blur="blur" type="search" class="weui_search_input" id="search_input" placeholder="搜索" required/>
        <a href="javascript:" class="weui_icon_clear"></a>
      </div>
      <label v-show="!is_focus && !search_key" for="search_input" class="weui_search_text">
        <i class="weui_icon_search"></i>
        <span>搜索</span>
      </label>
    </form>
    <a v-show="is_focus || search_key" @click="clean" href="javascript:" class="weui_search_cancel">取消</a>
  </div>
</template>

<script>
  // import store from '../store'
  export default {
    props: {
      search: {
        required: true
      },
      focus_run: {
      }
    },
    components: {
    },
    data: function () {
      return {
        search_key: null,
        is_focus: false
      }
    },
    ready () {
    },
    methods: {
      focus: function () {
        this.is_focus = true
        if(this.focus_run) {
          this.focus_run()
        }
      },
      blur: function () {
        this.is_focus = false
      },
      clean: function () {
        this.search_key = null
      },
      call: function () {
        this.search(this.search_key)
      }

    }
  }
</script>
