$(function () { 
  $("#logout").click(function (event) {
    event.preventDefault()
    localStorage.clear()
    location.assign('/index')
  })
})
