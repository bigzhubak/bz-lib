import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from './Main.vue'

Vue.use(VueRouter)

Vue.config.debug = true

var router = new VueRouter()
import ConfirmDoc from './components/ConfirmDoc'
import MenuUserInfoDoc from './components/MenuUserInfoDoc'
import CountUpDoc from './components/CountUpDoc'
import SignupDoc from './components/SignupDoc'
import LoginDoc from './components/LoginDoc'
import Oauth2Doc from './components/Oauth2Doc'
import WeMain from './components/WeMain'

import {Button, Cell, Toast, Dialog, Progress, Message, Article, Actionsheet, Icons} from './weui_doc'

var rout = {
  '/WeMain': { name: 'WeMain', component: WeMain },
  '/Oauth2': { name: 'Oauth2', component: Oauth2Doc },
  '/Login': { name: 'Login', component: LoginDoc },
  '/Signup': { name: 'Signup', component: SignupDoc },
  '/CountUp': { name: 'CountUp', component: CountUpDoc },
  '/MenuUserInfo': { name: 'MenuUserInfo', component: MenuUserInfoDoc },
  '/Confirm': { name: 'Confirm', component: ConfirmDoc},
  '/': { component: ConfirmDoc }
}

var weui_rout = {
  '/button': {
    component: Button
  },
  '/cell': {
    component: Cell
  },
  '/toast': {
    component: Toast
  },
  '/dialog': {
    component: Dialog
  },
  '/progress': {
    component: Progress
  },
  '/message': {
    component: Message
  },
  '/article': {
    component: Article
  },
  '/actionsheet': {
    component: Actionsheet
  },
  '/icons': {
    component: Icons
  }
}
Object.assign(rout, weui_rout)
router.map(rout)
router.start(Main, '#app')
