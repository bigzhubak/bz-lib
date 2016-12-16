export function replaceEmptyStrAsNull (o) {
  for (var property in o) {
    if (o[property] === '') o[property] = null
  }
  return o
}
