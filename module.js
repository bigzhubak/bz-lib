// store 的module
import 'whatwg-fetch'

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
    state.rich_list = rich_list
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
  login ({ state, commit }, user_name, password, done = null, error = null) {
    let parm = {}
    parm.user_name = user_name
    parm.password = password
    window.fetch('/api_login', {
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
  queryUserInfo ({ state, commit }, done = null, error = null) {
    window.fetch('/api_user_info', {
      credentials: 'same-origin',
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify()})
    .then(function (response) {
      return response
    }).then(function (response) {
      return response.json()
    }).then(function (data) {
      if (data.error !== '0') {
        throw new Error(data.error)
      }
      console.log(data.user_info)
      commit('SET_USER_INFO', data.user_info)
      if (done) {
        done(data)
      }
    })
  },

  queryRichList ({ state, commit }, done = null) {
    let parm = {'all': 1}
    parm = {parm: JSON.stringify(parm)}
    window.fetch('/api_rich_text', {
      credentials: 'same-origin',
      method: 'get',
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
      console.log(data.rich_text)
      commit('SET_RICH_LIST', data.rich_text)
      if (done) {
        done(data)
      }
    })
  },
  queryRichText ({ state, commit }, id, done = null) {
    let parm = {id: id}
    parm = {parm: JSON.stringify(parm)}
    window.fetch('/api_rich_text', {
      credentials: 'same-origin',
      method: 'get',
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
      console.log(data.rich_text[0])
      commit('SET_RICH_TEXT', data.rich_text[0])
      if (done) {
        done(data)
      }
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

