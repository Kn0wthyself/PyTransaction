$(function () {
  $.ajax({
    url: '/api/v1/basic-info',
    type: 'GET',
    dataType: 'json',
    headers: {'Authorization': 'jwt' + ' ' + localStorage.getItem('jwt')},
    success: function (response) {
      console.log(response)        
      $('#username').val(response['nickname'])
      $('#email').val(response['email'])
    }
  })
})
