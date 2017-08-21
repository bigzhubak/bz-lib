export default function(warning) {
  let promiseError = function(error, promise) {
    warning(error.reason.message)
  }
  window.addEventListener('unhandledrejection', promiseError)
  window.onerror = warning
}
