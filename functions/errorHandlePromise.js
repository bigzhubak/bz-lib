import toastr from 'toastr'
export default function (error, promise) {
  toastr.error(error.reason.message)
}
