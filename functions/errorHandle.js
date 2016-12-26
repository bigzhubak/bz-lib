import toastr from 'toastr'
export default function (message, source, lineno, colno, error) {
  toastr.error(error.message)
  return false
}
