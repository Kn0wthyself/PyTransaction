$(function () {
  $('#login').click(function (event) {
    event.preventDefault()
    var $username = $('#username').val()
    var $password = $('#password').val()
    $.ajax({
      url: '/api/v1/login',
      data: JSON.stringify({username: $username, password: $password}),
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      success: function (msg) {
        console.log('login success!')
        // console.log(msg)
        // console.log(msg['token'])
        localStorage.setItem('jwt', msg['token'])
        console.log(localStorage.getItem('jwt'))
        localStorage.setItem('username', $username)
        // location.assign('/user_admin')
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('wrong!')
        alert('密码或账号错误')
      }
    }).done(function () {
      location.assign('/profile')
    })
  })
})
