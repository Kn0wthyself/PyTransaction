$(function () {
  $('#change-password').click(function (event) {
    event.preventDefault()
    var $oldPassword = $('#old-password').val()
    var $newPassword = $('#new-password').val()
    $.ajax({
      url: '/api/v1/modify-password',
      data: JSON.stringify({old_password: $oldPassword, new_password: $newPassword}),
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      headers: {'Authorization': 'jwt' + ' ' + sessionStorage.getItem('jwt')},
      success: function (msg) {
        console.log('modify password success!')
        sessionStorage.removeItem('jwt')
        location.assign('/login')
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('modify password failed!')
        // console.log(sessionStorage.getItem('jwt')) // for debug
      }
    })
  })
})
