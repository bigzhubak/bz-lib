import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

Vue.use(VueRouter)

Vue.config.debug = true

var router = new VueRouter()
import ConfirmDoc from '../components/ConfirmDoc.vue'
import MenuUserInfoDoc from '../components/MenuUserInfoDoc.vue'
router.map(
  {
    '/MenuUserInfo': { name: 'MenuUserInfo', component: MenuUserInfoDoc },
    '/Confirm': { name: 'Confirm', component: ConfirmDoc },
    '/': { component: ConfirmDoc }
  }
)
router.start(App, '#app')
