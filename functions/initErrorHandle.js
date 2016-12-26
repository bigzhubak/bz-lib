import errorHandlePromise from './errorHandlePromise'
import errorHandle from './errorHandle'

export default function initErrorHandle () {
  window.addEventListener('unhandledrejection', errorHandlePromise)
  window.onerror = errorHandle
}
