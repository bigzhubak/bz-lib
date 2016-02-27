<template>
  <span></span>
</template>
<style>
</style>
<script>
  export default{
    data () {
      return {}
    },
    props: {
      start: {
        type: Number,
        default: 0
      },
      end: {
        type: Number,
        required: !0
      },
      decimal: {
        type: Number,
        default: 0
      },
      duration: {
        type: Number,
        default: 2.5
      },
      options: {
        type: Object
      }
    },
    computed: {
      startValue: function () {
        return this.start
      },
      endValue: function () {
        return this.end
      },
      decimalValue: function () {
        return this.decimal
      },
      durationValue: function () {
        return this.duration
      }
    },
    watch: {
      'end': function (val, oldVal) {
        this.count_up.update(val)
      }
    },
    ready () {
      // instantiate the countUp for the element
      this.count_up = new window.CountUp(this.$el, this.startValue,
        this.endValue,
        this.decimalValue,
        this.durationValue,
        this.options
      )
      console.log('run start' + this.endValue)
      this.count_up.start()
    }
  }
</script>
