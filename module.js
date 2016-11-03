// store 的module
import 'whatwg-fetch'
import _ from 'lodash'

// state
export const state = {
  rich_list: [],
  rich_text: {},
  user_info: {
    user_name: '',
    picture: ''
  },
  loading: false,
  error_info: '',
  info: ''
}
// mutations
export const mutations = {
  SET_INFO (state, info) {
    state.info = info
  },
  SET_SHORT_LIFE_INFO (state, info, time = 1000) {
    state.info = info
    setTimeout(
      () => {
        state.info = ''
      }, time
    )
  },
  CLEAN_RICH_TEXT (state, rich_text) {
    state.rich_text = {}
  },
  SET_RICH_TEXT (state, rich_text) {
    state.rich_text = rich_text
  },
  SET_RICH_LIST (state, rich_list) {
    state.rich_list = _.unionBy(state.rich_list, rich_list, 'id')
    // state.rich_list = rich_list
  },
  SET_USER_INFO (state, user_info) {
    state.user_info = user_info
  },
  SET_LOADING (state, loading) {
    state.loading = loading
  },
  SET_ERROR_INFO (state, error_info) {
    state.error_info = error_info
  },
  SET_SHORT_LIFE_ERROR_INFO (state, error_info, time = 1000) {
    state.error_info = error_info
    setTimeout(
      () => {
        state.error_info = ''
      }, time
    )
  }
}
// actions
export const actions = {
  get ({ state, commit }, val) {
    let url = ''
    if (typeof val === 'string') {
      url = val
    } else {
      url = val.url + '/' + JSON.stringify(val.body)
    }
    console.log(url)

    commit('SET_LOADING', true)
    return window.fetch(url, {
      credentials: 'same-origin',
      method: 'get',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      commit('SET_LOADING', false)
      return response
    }).then(function (response) {
      return response.json()
    }).then(function (data) {
      if (data.error !== '0') {
        commit('SET_ERROR_INFO', data.error)
        console.log(url + ' error: ' + data.error)
        throw new Error(data.error)
      }
      return data
    })
  },
  post ({ state, commit }, {url, body}) {
    commit('SET_LOADING', true)
    return window.fetch(url, {
      credentials: 'same-origin',
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    .then(function (response) {
      commit('SET_LOADING', false)
      return response
    }).then(function (response) {
      return response.json()
    }).then(function (data) {
      if (data.error !== '0') {
        commit('SET_ERROR_INFO', data.error)
        console.log(url + ' error: ' + data.error)
        throw new Error(data.error)
      }
      return data
    })
  },
  delete ({ state, commit }, url) {
    commit('SET_LOADING', true)
    return window.fetch(url, {
      credentials: 'same-origin',
      method: 'delete',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      commit('SET_LOADING', false)
      return response
    }).then(function (response) {
      return response.json()
    }).then(function (data) {
      if (data.error !== '0') {
        commit('SET_ERROR_INFO', data.error)
        console.log(url + ' error: ' + data.error)
      }
      return data
    })
  },
  put ({ state, commit }, {url, body}) {
    commit('SET_LOADING', true)
    return window.fetch(url, {
      credentials: 'same-origin',
      method: 'put',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    .then(function (response) {
      commit('SET_LOADING', false)
      return response
    }).then(function (response) {
      return response.json()
    }).then(function (data) {
      if (data.error !== '0') {
        commit('SET_ERROR_INFO', data.error)
        console.log(url + ' error: ' + data.error)
        throw new Error(data.error)
      }
      return data
    })
  },
  login ({ state, commit, dispatch }, {user_name, password}) {
    let parm = {}
    parm.user_name = user_name
    parm.password = password
    console.log(parm)
    return dispatch('post', {url: '/api_login', body: parm})
  },
  signup ({ state, commit }, user_name, password, email, done = null, error = null) {
    let parm = {}
    parm.user_name = user_name
    parm.password = password
    parm.email = email

    window.fetch('/api_signup', {
      credentials: 'same-origin',
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(parm)})
      .then(function (response) {
        return response
      }).then(function (response) {
        return response.json()
      }).then(function (data) {
        if (data.error !== '0') {
          throw new Error(data.error)
        }
        if (done) {
          done(data)
        }
      })
  },
  getUserInfo ({ state, commit, dispatch }) {
    return dispatch('get', '/api_user_info').then(function (data) {
      commit('SET_USER_INFO', data.user_info)
    })
  },
  getRichList ({ state, commit, dispatch }) {
    let parm = {'all': 1}
    return dispatch('get', {url: '/api_rich_text', body: parm}).then(function (data) {
      commit('SET_RICH_LIST', data.rich_text)
      return data
    })
  },
  getRichText ({ state, commit, dispatch }, parm) {
    // id or key
    return dispatch('get', {url: '/api_rich_text', body: parm}).then(function (data) {
      commit('SET_RICH_TEXT', data.rich_text[0])
      return data
    })
  }
}

// getters
export const getters = {
}

export default {
  state,
  mutations,
  actions,
  getters
}

