$(function () { 
  $("#logout").click(function (event) {
    event.preventDefault()
    localStorage.removeItem('jwt')
    location.assign('/index')
  })
})
