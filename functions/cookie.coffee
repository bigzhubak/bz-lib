
cookie =
  getCookieValue:(cookieName) ->
    ca = document.cookie.split('; ')
    _.find ca, (cookie) ->
      cookie.indexOf(cookieName) == 0

module.exports = cookie
