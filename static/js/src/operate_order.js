function publishOrder() {
  /**
   * 用户发布一个新的需求订单，订单状态为200
   */
  var username = localStorage.getItem('username')
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
    location.assign('/user_admin')
  })
}

function editPost() {
  /**
   * 发布需求者修改此订单 TODO
   */
}

function cancelPost() {
  /**
   * 发布需求者放弃此需求订单，订单状态转为500
   */
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  $.ajax({
    url: '/api/v1/cancel-post',
    data: JSON.stringify({
      id: $order_id,
    }),
    contentType: 'application/json',
    type: 'POST',
    dataType: 'json',
    headers: {
      'Authorization': 'jwt' + ' ' + localStorage.getItem('jwt')
    },
    success: function (msg) {
      console.log('cancel success!')
      location.assign('/all_orders')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('cannot cancel!')
    }
  })
}

function closePost() {
  /**
   * 发布需求者放弃让当前开发者接受此需求订单，使需求回归到200的状态 TODO
   */
}


function finishPost() {
  /**
   * 发布需求者完成此需求订单,订单状态转为400
   */
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  var $user_id = localStorage.getItem('user_id')
  $.ajax({
    url: '/api/v1/finish-post',
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
      console.log('finish success!')
      location.assign('/all_orders')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('finish accept!')
    }
  })
}

function acceptOrder() {
  /**
   * 用户接受一个订单，成为开发者，订单状态转为300
   */
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
      location.assign('/all_orders')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('cannot accept!')
    }
  })
}

function cancelOrder() {
  /**
   * 开发者放弃接受此订单 TODO
   */
}