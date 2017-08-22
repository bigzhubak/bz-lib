export default function initErrorHandle(callBack) {
  window.addEventListener('unhandledrejection', function(error, promise) {
    callBack(error.reason.message)
  })
  window.onerror = function(message, source, lineno, colno, error) {
    callBack(error.message)
    return false
  }
}
