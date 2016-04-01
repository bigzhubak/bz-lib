// import _ from 'underscore'
// import Vue from 'vue'
// import $ from 'jquery'
export default {
  SET_CARDS (state, cards) {
    console.log(cards)
    state.cards = cards
  },
  SET_USER_INFO (state, user_info) {
    state.user_info.user_name = user_info.user_name
    console.log(state)
    console.log(state.user_info.user_name)
  }
}
