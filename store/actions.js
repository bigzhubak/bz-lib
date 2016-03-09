import Vue from 'vue'
import VueResource from 'vue-resource'

// import _ from 'underscore'
Vue.use(VueResource)
import {getTopRightToast} from '../functions/toast.js'

var toast = getTopRightToast()

var api_user_info = Vue.resource('/api_user_info{/parm}')
var api_signup = Vue.resource('/api_signup{/parm}')
var api_login = Vue.resource('/api_login{/parm}')

export default {
  login: ({ dispatch, state, actions }, parm, call_back = null) => {
    api_login.save(parm).then(
      function (response) {
        if (response.data.error !== '0') {
          toast.error(response.data.error)
          // throw new Error(response.data.error)
        }
        if (call_back) {
          actions.queryUserInfo()
          call_back()
        }
      },
      function (response) {
      }
    )
  },
  signup: ({ dispatch, state, actions }, parm, call_back = null) => {
    api_signup.save(parm).then(
      function (response) {
        if (response.data.error !== '0') {
          toast.error(response.data.error)
          // throw new Error(response.data.error)
          return
        }
        if (call_back) {
          actions.queryUserInfo()
          call_back()
        }
      },
      function (response) {
      }
    )
  },
  queryUserInfo: ({ dispatch, state }) => {
    if (state.user_info.user_name !== '') {
      console.log('had user_info')
      return
    }
    api_user_info.get().then(
      function (response) {
        if (response.data.error !== '0') {
          toast.error(response.data.error)
          return
          // throw new Error(response.data.error)
        }
        dispatch('SET_USER_INFO', response.data.user_info)
      },
      function (response) {
      }
    )
  },
  deleteTodo: 'DELETE_TODO'
}
