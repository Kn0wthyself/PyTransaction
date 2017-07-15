$(function () { 
  $("#logout").click(function (event) {
    event.preventDefault()
    sessionStorage.removeItem('jwt')
    location.assign('/index')
  })
})
