// 注册的方法, 依赖 vue-resource 和 vuex
import Vue from 'vue'
var api_signup = Vue.resource('/api_signup{/parm}')

export default function (store, parm, call_back = null, error_call_back = null) {
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
