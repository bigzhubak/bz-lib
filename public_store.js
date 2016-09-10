// 一些公用的 store 方法
import Vue from 'vue'
var api_login = Vue.resource('/api_login{/parm}')
var api_signup = Vue.resource('/api_signup{/parm}')
var api_user_info = Vue.resource('/api_user_info{/parm}')
var api_rich_text = Vue.resource('/api_rich_text{/parm}')
// state
export const state = {
  rich_list: [],
  rich_text: {},
  user_info: {
    user_name: '',
    picture: ''
  },
  loading: false,
  error_info: ''
}
// mutations
export const mutations = {
  CLEAN_RICH_TEXT (state, rich_text) {
    state.rich_text = {}
  },
  SET_RICH_TEXT (state, rich_text) {
    state.rich_text = rich_text
  },
  SET_RICH_LIST (state, rich_list) {
    state.rich_list = rich_list
  },
  SET_USER_INFO (state, user_info) {
    state.user_info = user_info
  },
  SET_LOADING (state, loading) {
    state.loading = loading
  },
  SET_ERROR_INFO (state, error_info) {
    state.error_info = error_info
  },
  SET_SHORT_LIFE_ERROR_INFO (state, error_info, time = 1000) {
    state.error_info = error_info
    setTimeout(
      () => {
        state.error_info = ''
      }, time
    )
  }
}
// actions
export const login = (store, user_name, password, done = null, error = null) => {
  let parm = {}
  parm.user_name = user_name
  parm.password = password

  api_login.save(parm).then(
    (response) => {
      if (response.data.error !== '0') {
        console.log(response.data)
        if (error) error(response)
        throw new Error(response.data.error)
      }
      if (done) {
        done(response)
      }
    },
    (response) => {
      if (error) error(response)
    }
  )
}

export const signup = (store, user_name, password, email, done = null, error = null) => {
  let parm = {}
  parm.user_name = user_name
  parm.password = password
  parm.email = email
  api_signup.save(parm).then(
    function (response) {
      if (response.data.error !== '0') {
        if (error) error(response)
        // throw new Error(response.data.error)
      }
      console.log(done)
      if (done) {
        done(response)
      }
    },
    (response) => {
      // if (error) error(response)
    }
  )
}

export const queryUserInfo = (store, done = null, error = null) => {
  api_user_info.query().then(
    (response) => {
      if (response.data.error !== '0') {
        if (error) error(response)
        throw new Error(response.data.error)
      }
      console.log(response.data.user_info)
      store.dispatch('SET_USER_INFO', response.data.user_info)
      if (done) {
        done(response)
      }
    },
    (response) => {
      if (error) error(response)
    }
  )
}
export const queryRichList = (store, done = null) => {
  let parm = {'all': 1}
  parm = {parm: JSON.stringify(parm)}
  api_rich_text.query(parm).then(
    (response) => {
      if (response.data.error !== '0') {
        throw new Error(response.data.error)
      }
      store.dispatch('SET_RICH_LIST', response.data.rich_text)
      if (done) {
        done(response)
      }
    },
    (response) => {
    }
  )
}
export const queryRichText = (store, id, done = null) => {
  let parm = {id: id}
  parm = {parm: JSON.stringify(parm)}
  api_rich_text.query(parm).then(
    (response) => {
      if (response.data.error !== '0') {
        throw new Error(response.data.error)
      }
      store.dispatch('SET_RICH_TEXT', response.data.rich_text[0])
      if (done) {
        done(response)
      }
    },
    (response) => {
    }
  )
}
