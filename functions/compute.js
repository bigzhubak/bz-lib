import $ from 'jquery'
export function calculateHeight (img_height, img_width, max_width) {
  var real_height
  if (max_width <= img_width) {
    real_height = max_width * img_height / img_width
  } else {
    real_height = img_height
  }
  return real_height
}
export function getFitHeight (img_height, img_width) {
  var border, img_border, max_width, message_width, real_height, window_width
  window_width = $(window).width()
  border = 15 * 2
  if (window_width <= 768) {
    message_width = window_width - border
  }
  if (window_width > 768 && window_width < 992) {
    message_width = 750 - border
  }
  if (window_width >= 992 && window_width < 1200) {
    message_width = 970 * (8 / 12) - border
  }
  if (window_width >= 1200) {
    message_width = 1170 * (8 / 12) - border
  }
  img_border = 20
  max_width = message_width - img_border
  real_height = calculateHeight(img_height, img_width, max_width)
  return real_height
}
export function getFitHeightForSemantic (img_height, img_width) {
  var card_content_padding, container_border, grid_margin, max_width, message_width, real_height, window_width
  window_width = $(window).width()
  container_border = 14 * 2
  card_content_padding = 14 * 2
  grid_margin = -14 * 2
  if (window_width < 768) {
    message_width = window_width - container_border
  }
  if (window_width >= 768 && window_width <= 991) {
    message_width = 723
  }
  if (window_width >= 992 && window_width <= 1200) {
    message_width = 933
  }
  if (window_width > 1200) {
    message_width = 1127
    message_width -= grid_margin
    message_width = message_width * 7 / 12
  }
  max_width = message_width - card_content_padding
  real_height = calculateHeight(img_height, img_width, max_width)
  return real_height
}
