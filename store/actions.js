import Vue from 'vue'
import VueResource from 'vue-resource'

// import _ from 'underscore'
Vue.use(VueResource)

var toast = require('../functions/toast.coffee').getTopRightToast()

var api_user_info = Vue.resource('/api_user_info{/parm}')

export default {
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
