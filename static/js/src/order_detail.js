$(function () {
  var url = window.location.href
  var post_id = url.substring(url.lastIndexOf('/') + 1)
  var accept_post_html = '<button class="btn btn-primary" id="accept_post" onclick="acceptOrder()">接受订单</button>'
  var cancel_order_html = '<button class="btn btn-primary" id="cancel_order" onclick="cancelOrder()">放弃接单</button>'
  var edit_post_html = '<button class="btn btn-primary" id="edit_post" onclick="editPost()">修改需求</button>'
  var cancel_post_html = '<button class="btn btn-primary" id="cancel_post" onclick="cancelPost()">取消需求</button>'
  var finish_post_html = '<button class="btn btn-primary" id="finish_post" onclick="finishPost()">完成需求</button>'
  var operate_html = ''
  $.ajax({
    url: '/api/v1/get-order-by-id/' + post_id,
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      console.log(response)
      if ((parseInt(localStorage.getItem('user_id')) == response[0]['author']) && (response[0]['status']) === 200) {
        operate_html = edit_post_html + '&nbsp;&nbsp;' + cancel_post_html
      } else if ((parseInt(localStorage.getItem('user_id')) == response[0]['author']) && (response[0]['status'] === 300)) {
        operate_html = edit_post_html + '&nbsp;&nbsp;' + cancel_post_html + '&nbsp;&nbsp;' + finish_post_html
      } else if ((parseInt(localStorage.getItem('user_id')) != response[0]['author']) && (response[0]['status'] === 200)) {
        operate_html = accept_post_html
      }
      $('#order_detail').append('<h2>' + response[0]['title'] + '</h2>\
      <h4>No.' + response[0]['id'] + '&nbsp;&nbsp;&nbsp;发布者:' + response[0]['author_nickname'] + '&nbsp;&nbsp;&nbsp;开发者:' + response[0]['developer_nickname'] +'</h4>\
      <h4>报酬：' + response[0]['reward'] + '&nbsp;&nbsp;&nbsp;\
      联系方式:' + response[0]['contact_mobile'] + '&nbsp;&nbsp;&nbsp;\
      Tag:' + response[0]['tag'] + '&nbsp;&nbsp;&nbsp;状态:' + response[0]['status'] + '</h4>\
      <h3>需求内容:</h3>\
      <p>' + response[0]['content'] + '</p>' + operate_html)
    }
  })
})