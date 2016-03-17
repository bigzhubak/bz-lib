import $ from 'jquery'
import {timeLen} from '../functions/time.js'
export default {
  bind: function () {},
  update: function (new_value, old_value) {
    var date_str, el, that_time
    if (new_value) {
      el = $(this.el)
      that_time = new Date(new_value)
      date_str = timeLen(that_time)
      return el.html(date_str)
    }
  },
  unbind: function () {}
}
