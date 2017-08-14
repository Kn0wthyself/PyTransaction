$(function () {
  $.ajax({
    url: '/api/v1/get-all-orders',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      for (var i = 0; i < response.length; i++) {
        console.log(response[i])
        $("#order_list > table > tbody" ).append('<tr>\
        <td>' + response[i]["id"] + '</td>\
        <td>' + response[i]["author_nickname"] + '</td>\
        <td>' + response[i]["developer_nickname"] + '</td>\
        <td>' + response[i]["title"] + '</td>\
        <td>' + response[i]["reward"] + '</td>\
        <td>' + response[i]["tag"] + '</td>\
        <td>' + response[i]["status"] + '</td>\
        <td><a class="btn btn-primary" href="/order_detail/' + response[i]["id"] + '" role="button">查看详情</a></td>\
        </tr>')
      }
    }
  })
})
