import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'
import mutations from './mutations'
// import middlewares from './middlewares'

Vue.use(Vuex)

const state = {
  error_info: null,
  qq_map: null, // qq 地图的实例
  user_info: { // 登录的用户信息
    user_name: '',
    bio: '',
    github: '',
    twitter: '',
    instagram: '',
    tumblr: ''
  }
}

const store_lib = new Vuex.Store(
  {
  //  strict: true,
    state,
    actions,
    // middlewares,
    mutations
  }
)
if (module.hot) {
  // 使 actions 和 mutations 成为可热重载模块
  module.hot.accept(
    ['./actions', './mutations'], () => {
      // 获取更新后的模块
      // 因为 babel 6 的模块编译格式问题，这里需要加上 .default
      const newActions = require('./actions').default
      const newMutations = require('./mutations').default
      // 加载新模块
      store_lib.hotUpdate(
        {
          actions: newActions,
          mutations: newMutations
        }
      )
    }
  )
}
export default store_lib
