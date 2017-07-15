$(function () {
  $('#register').click(function (event) {
    event.preventDefault()
    var $username = $('#username').val()
    var $email = $('#email').val()
    var $password = $('#password').val()

    $.ajax({
      url: '/api/v1/register',
      data: JSON.stringify({username: $username, email: $email, password: $password}),
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
    }).done(function () {
      location.assign('/login')
    })
  })
})
