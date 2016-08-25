// 一些公用的 store 方法
import Vue from 'vue'
var api_login = Vue.resource('/api_login{/parm}')
var api_signup = Vue.resource('/api_signup{/parm}')
// state
export const state = {
}
// mutations
export const mutations = {
}
// actions
export const login = (store, parm, call_back = null, error_call_back = null) => {
  api_login.save(parm).then(
    (response) => {
      if (response.data.error !== '0') {
        if (error_call_back) error_call_back(response)
        throw new Error(response.data.error)
      }
      if (call_back) {
        call_back()
      }
    },
    (response) => {
      if (error_call_back) error_call_back(response)
    }
  )
}

export const signup = (store, parm, call_back = null, error_call_back = null) => {
  api_signup.save(parm).then(
    (response) => {
      if (response.data.error !== '0') {
        if (error_call_back) error_call_back(response)
        throw new Error(response.data.error)
      }
      if (call_back) {
        call_back()
      }
    },
    (response) => {
      if (error_call_back) error_call_back(response)
    }
  )
}
