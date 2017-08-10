$(function () {
  $.ajax({
    url: '/api/v1/get-all-orders',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      for (var i = 0; i < response.length; i++) {
        console.log(response[i])
        $("#order_list > ul" ).append('<li>\
        <h4><a href="#">' + response[i]["author"] + '</a>\
        发布了<a href=/order_detail/' + response[i]["id"] + '>' + response[i]["title"] + '</a></h4>\
        </li>')
      }
    }
  })
})
