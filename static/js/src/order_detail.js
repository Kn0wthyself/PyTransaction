$(function () {
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  $.ajax({
    url: '/api/v1/get-order-by-id/' + post_id,
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      $('#order_detail').append('<h2>' + response[0]['title'] + '</h2>\
      <h4>No.' + response[0]['id'] + '&nbsp;&nbsp;&nbsp;发布者:' + response[0]['author'] + '</h4>\
      <h4>报酬：' + response[0]['reward'] + '&nbsp;&nbsp;&nbsp;\
      联系方式:' + response[0]['contact_mobile'] + '&nbsp;&nbsp;&nbsp;\
      Tag:' + response[0]['tag'] + '&nbsp;&nbsp;&nbsp;状态:' + response[0]['status'] + '</h4>\
      <h3>需求内容:</h3>\
      <p>' + response[0]['content'] + '</p>\
      <button class="btn btn-primary" id="accept_order" onclick="acceptOrder()">接受订单</button>\
      ')
    }
  })
})