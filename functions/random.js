var colors = ['red', 'orange', 'yellow', 'olive', 'green', 'teal', 'blue', 'violet', 'purple', 'pink', 'brown', 'grey', 'black' ]
import _ from 'underscore'
export function color () {
  let index = _.random(0, colors.length)
  return colors[index]
}
