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
  }
}
// mutations
export const mutations = {
  SET_USER_INFO (state, user_info) {
    state.user_info = user_info
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
    (response) => {
      if (response.data.error !== '0') {
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

export const queryUserInfo = (store, done = null, error = null) => {
  api_user_info.query().then(
    (response) => {
      if (response.data.error !== '0') {
        if (error) error(response)
        throw new Error(response.data.error)
      }
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
