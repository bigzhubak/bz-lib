import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

Vue.use(VueRouter)

Vue.config.debug = true

var router = new VueRouter()
import ConfirmDoc from './components/ConfirmDoc.vue'
import MenuUserInfoDoc from './components/MenuUserInfoDoc.vue'
import CountUpDoc from './components/CountUpDoc.vue'
import SignupDoc from './components/SignupDoc.vue'
import LoginDoc from './components/LoginDoc.vue'
import Oauth2Doc from './components/Oauth2Doc.vue'

router.map(
  {
    '/Oauth2': { name: 'Oauth2', component: Oauth2Doc },
    '/Login': { name: 'Login', component: LoginDoc },
    '/Signup': { name: 'Signup', component: SignupDoc },
    '/CountUp': { name: 'CountUp', component: CountUpDoc },
    '/MenuUserInfo': { name: 'MenuUserInfo', component: MenuUserInfoDoc },
    '/Confirm': { name: 'Confirm', component: ConfirmDoc},
    '/': { component: ConfirmDoc }
  }
)
router.start(App, '#app')
