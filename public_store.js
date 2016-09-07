// 一些公用的 store 方法
import Vue from 'vue'
var api_login = Vue.resource('/api_login{/parm}')
var api_signup = Vue.resource('/api_signup{/parm}')
var api_user_info = Vue.resource('/api_user_info{/parm}')
// state
export const state = {
  user_info: {
    user_name: '',
    picture: ''
  },
  loading: false,
  error_info: ''
}
// mutations
export const mutations = {
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
