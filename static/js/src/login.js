$(function () {
  $('#login').click(function (event) {
    event.preventDefault()
    var $username = $('#username').val()
    var $password = $('#password').val()
    $.ajax({
      url: '/api/v1/login',
      data: JSON.stringify({
        username: $username,
        password: $password
      }),
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      success: function (msg) {
        console.log('login success!')
        localStorage.setItem('jwt', msg['token'])
        console.log(localStorage.getItem('jwt'))
        localStorage.setItem('username', $username)
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('wrong!')
        alert('密码或账号错误')
      }
    }).done(function () {
      $.ajax({
        url: '/api/v1/basic-info',
        type: 'GET',
        dataType: 'json',
        headers: {
          'Authorization': 'jwt' + ' ' + localStorage.getItem('jwt')
        },
        success: function (response) {
          localStorage.setItem('user_id', response['id'])
          localStorage.setItem('nickname', response['nickname'])
        }
      }).done(function () {
        location.assign('/profile')
      })
    })
  })
})