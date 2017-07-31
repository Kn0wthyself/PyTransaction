$(function () {
  $('#post_order').click(function (event) {
    var username = localStorage.getItem('username')
    
    $.ajax({
      url: '/api/v1/#',
      data: JSON.stringify(),
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      success: function (msg) {
        console.log(msg)
        console.log('post correctly!!')
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('wrong!')
      }
    }).done(function () {
      location.assign('/user_admin')
    })
  })
})
