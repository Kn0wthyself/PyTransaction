function acceptOrder() {
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  var $user_id = localStorage.getItem('user_id')
  $.ajax({
    url: '/api/v1/accept-post',
    data: JSON.stringify({
      id: $order_id,
      userid: $user_id
    }),
    contentType: 'application/json',
    type: 'POST',
    dataType: 'json',
    headers: {
      'Authorization': 'jwt' + ' ' + localStorage.getItem('jwt')
    },
    success: function (msg) {
      console.log('accept success!')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('cannot accept!')
    }
  })
}
