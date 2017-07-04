# PyTransaction

## 项目结构
- `api`: 提供rest api
- `website`: 提供网站模板渲染、model配置
- `py_transaction`: 项目配置目录
- `static`: 静态文件存放目录
- `templates`: 模板存放目录

## 说明
目前暂停前后端在同一项目中开发，后端提供api，前端负责页面模板的开发，由django提供路由功能，
采用djangorestframework作为rest框架。

提供了两个hello world 示例(在本地8000端口启动服务然后访问)
模板：<a href="http://localhost:8000/helloworld">hello world</a>
api:<a href="http://localhost:8000/api/helloworld">hello world</a>