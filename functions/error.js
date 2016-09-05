import toastr from 'toastr'
export function errorHandle (message, source, lineno, colno, error) {
  toastr.error(error.message)
  return false
}
