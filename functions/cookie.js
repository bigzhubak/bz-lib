import _ from 'underscore'
export function getCookieValue (cookieName) {
  var ca
  ca = document.cookie.split('; ')
  return _.find(
    ca,
    function (cookie) {
      return cookie.indexOf(cookieName) === 0
    }
  )
}
