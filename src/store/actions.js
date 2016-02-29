import Vue from 'vue'
import VueResource from 'vue-resource'
Vue.use(VueResource)

import _ from 'underscore'
import $ from 'jquery'
import {scrollTo} from '../../lib_bz/functions/animate.js'

var god_info_resource = Vue.resource('/api_god_info{/parm}')
var user_info_resource = Vue.resource('/api_get_user_info{/parm}')
var new_resource = Vue.resource('/api_new{/parm}')
var old_resource = Vue.resource('/api_old{/parm}')
var record_resource = Vue.resource('/api_update_last{/parm}')

export default {
  filterGodMessages: ({ dispatch, state }, god_name) => {
    dispatch('FILTER_GOD_MESSAGES', god_name)
  },
  queryGodInfo: ({ dispatch, state }, god_name) => {
    var parm = JSON.stringify(
      { god_name: god_name }
    )
    parm = {parm: parm}
    god_info_resource.get(parm).then(
      function (response) {
        dispatch('SET_GOD_INFO', response.data.god_info)
      },
      function (response) {
      }
    )
  },
  recordLastMessage: ({ dispatch, state }, message_id) => {
    if (state.last_message_id > parseInt(message_id, 10)) {
      console.log('return')
      return
    }
    var parm = JSON.stringify(
      { message_id: message_id }
    )
    record_resource.update(parm).then(
      function (response) {
        console.log(response.data)
        dispatch('SET_LAST_MESSAGE_ID', message_id)
        dispatch('REFRESH_UNREAD_MESSAGE_COUNT')
      },
      function (response) {
      }
    )
  },
  queryOldMessages: ({ dispatch, state }) => {
    dispatch('SET_OLD_LOADING', true)
    var offset = state.messages.length
    var parm = JSON.stringify(
      {
        offset: offset
      }
    )
    parm = {parm: parm}
    old_resource.get(parm).then(
      function (response) {
        dispatch('SET_OLD_MESSAGES', response.data.messages)
        dispatch('SET_INFO', '', '')
        dispatch('SET_OLD_LOADING', false)
      },
      function (response) {
      }
    )
  },
  queryGodOldMessages: ({ dispatch, state }, god_name) => {
    dispatch('SET_OLD_LOADING', true)
    var offset = state.gods_messages[god_name].length
    var parm = JSON.stringify(
      {
        offset: offset,
        god_name: god_name
      }
    )
    parm = {parm: parm}
    old_resource.get(parm).then(
      function (response) {
        dispatch('SET_GODS_OLD_MESSAGES', god_name, response.data.messages)
        dispatch('SET_INFO', '', '')
        dispatch('SET_OLD_LOADING', false)
      },
      function (response) {
      }
    )
  },
  queryNewMessages: ({ dispatch, state }) => {
    dispatch('SET_NEW_LOADING', true)
    new_resource.get().then(
      function (response) {
        if (response.data.info === 'not followed any one') {
          dispatch('SET_INFO', '还未关注任何人呢!', '随机列了一些消息，鼠标放到头像上来关注。')
        }

        if (response.data.messages.length === 0) {
          if (state.messages.length === 0) {
            dispatch('SET_INFO', '消息全被你读完啦，厉害!', '点击按钮看看历史消息？')
          } else {
            // _.delay(scrollAnimate, 500, 500, '-=100')
          }
        } else {
          dispatch('SET_NEW_MESSAGES', response.data.messages)
          _.delay(scrollTo, 500, $('#id_' + response.data.last_message_id))
        }
        dispatch('SET_NEW_LOADING', false)
        dispatch('REFRESH_UNREAD_MESSAGE_COUNT')
      },
      function (response) {
      }
    )
  },
  queryGodNewMessages: ({ dispatch, state, actions }, god_name) => {
    dispatch('SET_NEW_LOADING', true)
    var parm = JSON.stringify(
      {
        god_name: god_name
      }
    )
    parm = {parm: parm}
    new_resource.get(parm).then(
      function (response) {
        if (response.data.messages.length === 0) { // 没有取到数
          console.log(state.gods_messages[god_name].length)
          if (state.gods_messages[god_name].length === 0) { // 可能是url直接访问
            actions.queryGodOldMessages(god_name)
          } else {
            // _.delay(scrollAnimate, 500, 500, '-=100')
          }
        } else {
          dispatch('SET_GODS_NEW_MESSAGES', god_name, response.data.messages)
        }
        dispatch('SET_NEW_LOADING', false)
      },
      function (response) {
      }
    )
  },
  queryUserInfo: ({ dispatch, state }) => {
    if (Object.keys(state.user_info).length === 0) {
      user_info_resource.get().then(
        function (response) {
          console.log(response.data.user_info)
          dispatch('SET_USER_INFO', response.data.user_info)
        },
        function (response) {
        }
      )
    }
  },
  deleteTodo: 'DELETE_TODO'
}
