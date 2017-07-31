$(function () {
  if (localStorage.getItem('jwt') != null) {
      // $(".valid_after_login").replaceWith("<div class='container'><h2>请登陆后查看</h2></div>")
      location.assign('/user_admim')
  }

})