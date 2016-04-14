// import _ from 'underscore'
// import Vue from 'vue'
// import $ from 'jquery'
export default {
  SET_LOCATION (state, location) {
    state.location = location
  },
  SET_CARDS (state, cards) {
    console.log(cards)
    state.cards = cards
  },
  SET_USER_INFO (state, user_info) {
    state.user_info = user_info
    state.user_info.user_name = user_info.user_name
  },
  SET_ERROR_INFO (state, error_info) {
    state.error_info = error_info
  }
}
