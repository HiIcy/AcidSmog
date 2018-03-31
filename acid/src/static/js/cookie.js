var cookie = {
  setCookie (cname, value, expiredays) {
    var exdate = new Date()
    exdate.setTime(exdate.getTime() + expiredays)
    exdate.setDate(exdate.getDate() + expiredays)
    document.cookie = cname + '=' + encodeURI(value) + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString())
  },
  getCookie (name) {
    // FAQ:
    var arr,
      reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)')
    arr = document.cookie.match(reg)
    if (arr) {
      return arr[2]
    } else {
      return null
    }
  },

  delCooike (name) {
    var exp = new Date()
    exp.setTime(exp.getTime() - 1)
    var cval = cookie.getCookie(name)
    if (cval != null) {
      document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;'
    }
  }
}
export default cookie
