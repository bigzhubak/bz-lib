import Confirm from './components/ConfirmDoc'
import MenuUserInfo from './components/MenuUserInfoDoc'
import CountUp from './components/CountUpDoc'
import Signup from './components/SignupDoc'
import Login from './components/LoginDoc'
import Oauth2 from './components/Oauth2Doc'
import WeMain from './components/WeMain'
import Forget from './components/ForgetDoc'
import BottomLoader from './components/BottomLoaderDoc'
import WeSearchBar from './components/WeSearchBarDoc'
import QMap from './components/QMapDoc'
import QMapLocation from './components/QMapLocationDoc'

// desc 是为了menu上显示用，vue-router本身是不需要的
export default {
  '/QMapLocation': { name: 'QMapLocation', component: QMapLocation, desc: 'QMap 的附加组件，能够定位当前位置'},
  '/QMap': { name: 'QMap', component: QMap, desc: 'qq 地图基础组件'},
  '/WeSearchBar': { name: 'WeSearchBar', component: WeSearchBar, desc: 'weui的searchbar组件，有一些js操作'},
  '/BottomLoader': { name: 'BottomLoader', component: BottomLoader, desc: '滚动到底部做些什么'},
  '/Forget': { name: 'Forget', component: Forget, desc: '忘记密码'},
  '/WeMain': { name: 'WeMain', component: WeMain, desc: 'weui组件的入口'},
  '/Oauth2': { name: 'Oauth2', component: Oauth2, desc: 'Oauth2登录'},
  '/Login': { name: 'Login', component: Login, desc: '登录'},
  '/Signup': { name: 'Signup', component: Signup, desc: '用户注册'},
  '/CountUp': { name: 'CountUp', component: CountUp, desc: '数字递增递减动画效果'},
  '/MenuUserInfo': { name: 'MenuUserInfo', component: MenuUserInfo, desc: 'Menu上显示用户信息'},
  '/Confirm': { name: 'Confirm', component: Confirm, desc: '确认提示框'},
  '/': { component: Confirm }
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
