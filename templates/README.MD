使用bootstrap CDN + jquery

 - index.html 首页
 - join.html 注册页面
 - login.html登录页面
 - admin.html登陆后管理页面
 - profile.html个人信息页

usage>>  
```
python manage.py collectstatic
python manage.py runserver
```

注：  
 - 修改密码在`/profile`

TODO:
 - 确认密码
 - 权限控制
 - 进一步模块化