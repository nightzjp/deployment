# 代码部署功能测试

部署功能测试代码，后端程序使用python3基于Django框架开发, 以pipenv作为包管理工具.

`.env 文件为项目环境变量配置文件`

## 代码目录结构
```
├── Dockerfile  Dockerfile文件
├── Pipfile  包管理文件
├── Pipfile.lock  包文件依赖
├── Readme.md
├── apps  默认app目录
│   ├── __init__.py
│   └── api
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   ├── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── db.sqlite3
├── deploy  部署配置文件
│   ├── nginx  nginx配置
│   │   └── deployment.conf
│   ├── supervisor  supervisor配置
│   │   └── deployment.ini
│   └── uwsgi  uwsgi配置
│       ├── deployment_http.ini
│       └── deployment_socket.ini
├── deployment
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml  docker-compose.yml配置文件
├── manage.py
├── setup.sh  一键部署脚本
├── start.sh  项目启动文件
├── static  静态资源文件
└── templates  静态模板

```

## 部署

`如未说明，数据库采用postgresql， 缓存配置redis`

### 部署方式一 √
```text
最老掉牙的部署方式(各系统通用) 

1. 后台直接运行python manage.py runserver 127.0.0.1 8888 (为了使项目一直运行，可搭配supervisor管理工具)
2. nginx监听 http://127.0.0.1:8888端口
```


### 部署方式二
```text
进阶部署(windows 不可用)

1. uwsgi_http: 跟部署方式一类型，中间加了一层uwsgi层
    1.1: nginx监听HTTP端口
2. uwsgi_socket: 相比http部署小路更高
    1.2: nginx监听socket端口

socket层通信优于HTTP层通信
```


### 部署方式三
```text
Dockerfile部署 | 部署方便，代码统一用0.0.0.0 启动
项目打包成docker镜像 | 打包可能有坑！
避免了环境的安装，半一键部署
1. host模式启动
    docker run -itd  --name deployment -v /root/deployment:/app -p 8888:8888 --network=host deployment:latest
2. 非host模式启动
    docker run -itd  --name deployment -v /root/deployment:/app -p 8888:8888 deployment:latest
不指定network=host，则需要修改Dockerfile

```


### 部署方式四
```text
Docker-compose部署 | nginx 一并打包
项目打包成docker镜像，docker-compose.yml管理
一键部署
docker-compose up -d

```

### 部署项目五
```text
部署方式四的升级操作

```

