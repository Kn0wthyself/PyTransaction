# PyTransaction

## 项目结构
- `api`: 提供rest api,model配置
- `website`: 提供网站模板渲染
- `py_transaction`: 项目配置目录
- `static`: 静态文件存放目录
- `templates`: 模板存放目录

## 说明
目前暂停前后端在同一项目中开发，后端提供api，前端负责页面模板的开发，由django提供路由功能，
采用djangorestframework作为rest框架。

提供了两个hello world 示例(在本地8000端口启动服务然后访问)
模板：<a href="http://localhost:8000/helloworld">hello world</a>
api:<a href="http://localhost:8000/api/helloworld">hello world</a>

## git工作流程
- 每个人先fork主仓库到自己的项目里，然后clone自己的项目，
- 添加主仓库为上游仓库: `git remote add upstream git@github.com:Kn0wthyself/PyTransaction.git`，
- 每次提交push到自己的远程仓库即可，
- 需要合并到主仓库时，需要先pull上游代码，并处理冲突（如果有）:`git pull upstream develop`，
  再提交pull request到develop分支由管理员审核是否接受合并

## restful api规范
`url`:协议://主机/版本/资源路径，如:`https://localhost/v1/user/1`代表id为1的用户信息，
获取资源列表使用复数形式如获取用户列表：`https://localhost/v1/users`

`请求方式`:目前暂定使用GET、POST、PUT、DELETE四种方式
- `GET`:获取资源
- `POST`:新增资源
- `PUT`:更新资源
- `DELETE`:删除资源

`http状态码`:暂规定使用如下状态码返回
- `200`:表示成功
- `400`:表示请求错误，如参数错误等
- `401`:表示用户未认证
- `403`:表示此用户没有访问权限
- `404`:表示资源不存在
- `405`:表示请求方式不支持

`消息体`:返回的内容应当是json格式的，内容由开发者自己定义

`文档`:暂定使用swagger来编写api文档

`用户认证`:暂定使用jwt token认证


## to后端
- 在api/models下建立各自模块需要的表
- 在api/views下开发各自模块的api
- 在api/serializer下建立各自模块的序列化器

## to前端
- 在templates/下开发各个模块的页面模板
- 在static/下存放js、css等静态文件
- 在website/views下建立每个页面的视图

## 数据库部署
- 1、先在mysql数据库建立数据库    create database pyt;
- 2、设置为当前使用的数据库 use pyt
- 3、创建django访问pyt数据库的账号，并在数据库mysql的表user中检查 create user pyt@localhost identified by 'pyt';
- 4、对pyt@localhost开放访问数据库pyt中所有表的所有权限 grant all privileges on pyt.* to pyt@localhost;
- 5、刷新权限 flush privileges;
- 6、在py_transaction/settings.py 的DATABASES下配置MySql数据库

```python
        DATABASES = {
            'default': {
                #'ENGINE': 'django.db.backends.sqlite3',
                #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'pyt',
                'USER': 'pyt',
                'PASSWORD': 'pyt',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
```

- 7、 python manage.py makemigrations
- 8、 python manage.py migrate