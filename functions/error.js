import toastr from 'toastr'
export function errorHandle (message, source, lineno, colno, error) {
  toastr.error(error.message)
  return false
}
export function errorHandlePromise (error, promise) {
  toastr.error(error.reason.message)
}

export function initErrorHandle () {
  window.addEventListener('unhandledrejection',
    function (error, promise) {
      toastr.error(error.message)
    }
  )
  window.onerror = function (message, source, lineno, colno, error) {
    toastr.error(error.message)
    return false
  }
}
