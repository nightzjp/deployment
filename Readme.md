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
│   ├── __init__.py
│   └── api
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   ├── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── db.sqlite3
├── deploy  部署配置文件
│   ├── nginx  nginx配置
│   │   └── deployment.conf
│   ├── supervisor  supervisor配置
│   │   └── deployment.ini
│   └── uwsgi  uwsgi配置
│       ├── deployment_http.ini
│       └── deployment_socket.ini
├── deployment
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml  docker-compose.yml配置文件
├── manage.py
├── setup.sh  一键部署脚本
├── start.sh  项目启动文件
├── static  静态资源文件
└── templates  静态模板

```

---

## 前期准备

`如未说明，数据库采用postgresql，缓存配置redis，服务器采用Ubuntu16.04 ,python3 默认版本为3.5，系统使用python版本为3.6.x`

```shell
1. 卸载默认python3.5(可不卸载)
sudo apt-get remove python3.5
sudo apt-get remove --auto-remove python3.5

2. 安装python3.6
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6    
    - sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 python3.6-dev

3. 系统依赖
sudo apt install gcc libgmp-dev libmpfr-dev libmpc-dev
sudo apt install libpq-dev python3-dev

4. pip3 安装 
wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate
python3.6 get-pip.py
```

1. 搭建基础Django框架
2. 通过编译器运行

---

## 基础部署

1. 代码放在服务器直接运行 `代码直接通过run运行`

   ```text
   最老掉牙的部署方式(各系统通用) 
   
   1. 后台直接运行python manage.py runserver 127.0.0.1 8888 
   2. nginx监听 http://127.0.0.1:8888端口
   ```

2. 阉割部署 `通过supervisor代替后台指令，可加nginx`

   ```text
   基于方式一部署可增加supervisor管理，nginx做转发
   ```

3. 常规化部署 `uwsgi+supervisor+nginx`

   ```text
   进阶部署(windows 不可用)
   
   1. uwsgi_http: 跟部署方式一类型，中间加了一层uwsgi层
       1.1: nginx监听HTTP端口
   2. uwsgi_socket: 相比http部署小路更高
       1.2: nginx监听socket端口
   
   socket(4)层通信优于HTTP(7)层通信 | 正式环境建议采用socket部署方式
   ```

4. 静态文件配置

   ```python
   # STATIC_CONFIG
   STATIC_URL = '/static/'
   STATIC_ROOT = Path.joinpath(BASE_DIR, "static/")
   # STATICFILES_DIRS = [Path.joinpath(BASE_DIR, 'static')]
   ```

5. 静态文件收集

   ```python
   pipenv run python manage.py collectstatic
   ```

6. nginx静态文件配置

   ```nginx
   server {
     listen                          80;
     server_name                     localhost;
     chunked_transfer_encoding       on;
   
     location /static {
       expires                       30d;
       alias                         /root/deployment/static;
       # root                          /root/deployment/static;
     }
   
     location / {
       proxy_pass                   http://172.17.0.1:8888;
     }
   }
   ```

## 单机docker部署

1. 代码上传至服务器

2. 代码打包镜像

   ```shell
   docker build -t deployment .
   代码打包可能遇到一些坑。根据实际情况处理即可
   ```

3. 容器运行

   ```shell
   Dockerfile部署 | 部署方便，代码统一用0.0.0.0 启动
   项目打包成docker镜像 | 打包可能有坑！
   避免了环境的安装，半一键部署
   1. host模式启动
       docker run -itd  --name deployment -v /root/deployment:/app -p 8888:8888 --network=host deployment:latest
   2. 非host模式启动
       docker run -itd  --name deployment -v /root/deployment:/app -p 8888:8888 deployment:latest
   不指定network=host，则需要修改Dockerfile
   ```

4. compose构建

   ```shell
   docker-compose up -d
   docker-compose ps
   ```

## 多机部署

1. 服务器镜像推送至docker-hub

2. docker-compose.yml一键部署 `基础部署`

   ```bash
   su sh setup.sh 一键部署
   ```

3. docker-compose.yml一键部署 `进阶部署`