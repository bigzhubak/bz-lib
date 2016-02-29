import _ from 'underscore'
import Vue from 'vue'
function initGodMessage (state, god_name) {
  if (state.gods_messages[god_name] === undefined) {
    Vue.set(state.gods_messages, god_name, [])
  }
}
export default {
  REFRESH_UNREAD_MESSAGE_COUNT (state) {
    let unread_messages = _.partition(state.messages, (d)=>{ return d.id > state.last_message_id })[0]
    state.unread_message_count = unread_messages.length
    console.log(state.unread_message_count)
    // state.unread_message_count =
  },
  FILTER_GOD_MESSAGES (state, god_name) { // 从主线messages中把god message 过滤出来，避免页面空白
    initGodMessage(state, god_name)
    if (state.messages.length !== 0 && state.gods_messages[god_name].length === 0) {
      state.gods_messages[god_name] = _.filter(state.messages, (d)=>{ return d.name === god_name })
    }
  },
  SET_GODS_OLD_MESSAGES (state, god_name, messages) {
    initGodMessage(state, god_name)
    state.gods_messages[god_name] = _.uniq(
      messages.reverse().concat(state.gods_messages[god_name]), false, function (item, key, a) {
        return item.id
      }
    )
  },
  SET_GODS_NEW_MESSAGES (state, god_name, messages) {
    initGodMessage(state, god_name)
    state.gods_messages[god_name] = _.uniq(
      state.gods_messages[god_name].concat(messages.reverse()), false, function (item, key, a) {
        return item.id
      }
    )
  },
  SET_GOD_INFO (state, god_info) {
    state.god_info = god_info
  },
  SET_LAST_MESSAGE_ID (state, message_id) {
    state.last_message_id = message_id
  },
  SET_OLD_LOADING (state, loading) {
    state.old_loading = loading
  },
  SET_NEW_LOADING (state, loading) {
    state.new_loading = loading
  },
  SET_OLD_MESSAGES (state, messages) {
    state.messages = _.uniq(
      messages.reverse().concat(state.messages), false, function (item, key, a) {
        return item.id
      }
    )
  },
  SET_INFO (state, header, info) {
    state.info.header = header
    state.info.info = info
  },
  SET_NEW_MESSAGES (state, messages) {
    state.messages = _.uniq(
      state.messages.concat(messages.reverse()), false, function (item, key, a) {
        return item.id
      }
    )
  },
  SET_USER_INFO (state, user_info) {
    state.user_info = user_info
  }
}
