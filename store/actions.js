import Vue from 'vue'
import VueResource from 'vue-resource'

// import _ from 'underscore'
Vue.use(VueResource)
import {getTopRightToast} from '../functions/toast.js'

var toast = getTopRightToast()

var api_user_info = Vue.resource('/api_user_info{/parm}')
var api_signup = Vue.resource('/api_signup{/parm}')

export default {
  signup: ({ dispatch, state }, parm, call_back = null) => {
    api_signup.save(parm).then(
      function (response) {
        if (response.data.error !== '0') {
          toast.error(response.data.error)
          throw new Error(response.data.error)
        }
        console.log(call_back)
        if (call_back) {
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
          throw new Error(response.data.error)
        }
        dispatch('SET_USER_INFO', response.data.user_info)
      },
      function (response) {
      }
    )
  },
  deleteTodo: 'DELETE_TODO'
}
