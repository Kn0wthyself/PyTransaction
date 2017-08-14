$(function () {
  $('#publish_order').click(function (event) {
    event.preventDefault()
    var $author = parseInt(localStorage.getItem('user_id'))
    var $title = $('#title').val()
    var $content = $('#content').val()
    var $reward = parseInt($('#reward').val())
    var $contact_mobile = parseInt($('#contact_mobile').val())
    var $status = 200
    var $tag = parseInt($('#tag').val())
    var jsonData = JSON.stringify({
      author: $author,
      title: $title,
      content: $content,
      reward: $reward,
      contact_mobile: $contact_mobile,
      status: $status,
      tag: $tag
    })
    console.log(jsonData)
    $.ajax({
      url: '/api/v1/create-posttag',
      data: jsonData,
      contentType: 'application/json',
      type: 'POST',
      dataType: 'json',
      headers: {
        'Authorization': 'jwt' + ' ' + localStorage.getItem('jwt')
      },
      success: function (msg) {
        console.log(msg)
        console.log('post correctly!!')
      },
      error: function (error_msg) {
        console.log(error_msg)
        console.log('wrong!')
      }
    }).done(function () {
      location.assign('/order_list')
    })
  })
})
