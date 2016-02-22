import $ from 'jquery'
export function scrollAnimate (time, len) {
  $('html, body').animate(
    {
      scrollTop: '' + len
    }, time
  )
}
