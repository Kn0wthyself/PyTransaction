$(function () {
    $.ajax({
        url: '/api/v1/get-order-by-id',
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            $("#order_detail").append('<li><h4><a href="#">' + response[i]["author"] + '</a>' + '发布了' + '<a href=/order/' + response[i]["id"] + '>' + response[i]["title"] + '</a></h4></li>')
        }
    })
})