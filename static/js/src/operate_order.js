function editPost () {
  /**
   * 发布需求者修改此订单 TODO
   */
}

function cancelPost () {
  /**
   * 发布需求者放弃此需求订单，订单状态转为500
   */
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  $.ajax({
    url: '/api/v1/cancel-post',
    data: JSON.stringify({
      id: $order_id
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

function closeOrderByAuthor () {
  /**
   * 发布需求者放弃让当前开发者接受此需求订单，使需求回归到200的状态 TODO
   */
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  var $user_id = localStorage.getItem('user_id')
  $.ajax({
    url: '/api/v1/close-post-user',
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
      console.log('closePost success!')
      location.assign('/all_orders')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('cannot closePost!')
    }
  })
}

function finishPost () {
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

function acceptOrder () {
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

function closeOrderByDev () {
  /**
   * 开发者放弃接受此订单 TODO
   */
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var $order_id = post_id
  var $user_id = localStorage.getItem('user_id')
  $.ajax({
    url: '/api/v1/close-post-dev',
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
      console.log('cancelOrder success!')
      location.assign('/all_orders')
    },
    error: function (error_msg) {
      console.log(error_msg)
      console.log('cannot cancelOrder!')
    }
  })
}
