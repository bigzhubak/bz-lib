export function checkLogin () {
  let user_cookie = window.document.cookie.indexOf('user_id=')
  if (user_cookie === -1) return false
  else return true
}
