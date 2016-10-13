import toastr from 'toastr'
export function errorHandle (message, source, lineno, colno, error) {
  toastr.error(error.message)
  return false
}
export function errorHandlePromise (error, promise) {
  toastr.error(error.reason.message)
}

export function initErrorHandle () {
  console.log('initErrorHandle works')
  window.addEventListener('unhandledrejection', errorHandlePromise)
  window.onerror = errorHandle
}
