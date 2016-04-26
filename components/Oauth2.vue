<style lang=less>
  .ui.button.oauth {
    margin: 0.75em
  }
  @font-face {font-family: 'douban';
    src: url('../assets/douban.eot'); /* IE9*/
    src: url('../assets/douban.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
    url('../assets/douban.woff') format('woff'), /* chrome、firefox */
    url('../assets/douban.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
    url('../assets/douban.svg#douban') format('svg'); /* iOS 4.1- */
  }
  i.icon.douban{
    font-family:"douban" !important;
    font-style:normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
  }
  .ui.douban.button {
    background-color: #66AD70;
    color: #fff;
  }
  .ui.douban.button:hover {
    background-color: #499E55;
  }
  i.icon.douban:before { 
    content: "\e94a";
  }
</style>

<template>
  <a v-for="oauth in oauths" @click="loading" href="/api_{{oauth}}" class="ui {{oauth}} button oauth">
    <i class="{{oauth}} icon"></i>
    {{upperFirst(oauth)}}
  </a>
</template>

<script>
  export default {
    props: ['oauths'],
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
      upperFirst: function (string) {
        return string.charAt(0).toUpperCase() + string.substring(1).toLowerCase()
      },
      loading: function (e) {
        e.target.className += ' loading '
      }
    }
  }
</script>
