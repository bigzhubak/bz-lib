import ConfirmDoc from './components/ConfirmDoc'
import MenuUserInfoDoc from './components/MenuUserInfoDoc'
import CountUpDoc from './components/CountUpDoc'
import SignupDoc from './components/SignupDoc'
import LoginDoc from './components/LoginDoc'
import Oauth2Doc from './components/Oauth2Doc'
import WeMain from './components/WeMain'
// desc 是为了menu上显示用，vue-router本身是不需要的
export default {
  '/WeMain': { name: 'WeMain', component: WeMain, desc: 'weui组件的入口'},
  '/Oauth2': { name: 'Oauth2', component: Oauth2Doc, desc: 'Oauth2登录'},
  '/Login': { name: 'Login', component: LoginDoc, desc: '登录'},
  '/Signup': { name: 'Signup', component: SignupDoc, desc: '用户注册'},
  '/CountUp': { name: 'CountUp', component: CountUpDoc, desc: '数字递增递减动画效果'},
  '/MenuUserInfo': { name: 'MenuUserInfo', component: MenuUserInfoDoc, desc: 'Menu上显示用户信息'},
  '/Confirm': { name: 'Confirm', component: ConfirmDoc, desc: '确认提示框'},
  '/': { component: ConfirmDoc }
}

import {Button, Cell, Toast, Dialog, Progress, Message, Article, Actionsheet, Icons} from './weui_doc'
var weui_router_conf = {
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
export {weui_router_conf}
