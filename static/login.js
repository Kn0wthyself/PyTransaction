$(function () {
  $('#login').click(function () {
    var $username = $('#username').val()
    var $password = $('#password').val()
    $.ajax({
      url: '/api/v1/login',
      data: JSON.stringify({username: $username, password: $password}),
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      success: function (msg) {
        console.log(msg)
        console.log('hello!')
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('wrong!')
        // console.log(JSON.stringify({username: $username, email: $email, password: $password}))
      }
    })
  })
})
