import $ from 'jquery'
export function scrollAnimate (time, len) {
  $('html, body').animate(
    {
      scrollTop: '' + len
    }, time
  )
}
export function scrollTo (target, offset = 0) { // 滚动到某个dom, 定位到这个target, offset偏移量
  if (!$(target).offset()) {
  } else {
    let y = $(target).offset().top
    y = y + offset
    window.scrollTo(0, y)
  }
}
