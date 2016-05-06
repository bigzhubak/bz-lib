import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from './Main.vue'
import './style/weui.less'
import router_conf from './router_conf.js'
import './node_modules/toastr/toastr.less'

Vue.use(VueRouter)

Vue.config.debug = true

const router = new VueRouter(
  {
    history: true,
    saveScrollPosition: true
  }
)

router.map(router_conf)
router.start(Main, 'app')
