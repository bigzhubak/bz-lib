// UTC 转 local
import dateFormat from './dateFormat'
export default function (utc_date) {
  utc_date = new Date(utc_date)
  let world_date = dateFormat(utc_date, 'YY-MM-dd hh:mm:ss UTC')
  let local_date = new Date(world_date)
  return local_date
}
