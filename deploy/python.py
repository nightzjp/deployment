# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: python.py
@time: 2021/6/28 上午11:54
"""

"""
Ubuntu 16.04 python3默认版本为3.5，系统使用python版本为python3.6

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

"""

"""
分享流程
    前期准备
        1. 搭建基础Django框架
        2. 通过编辑器运行
    一、(基础部署)
        1. 代码放在服务器
        2. 阉割部署
        3. 常规化部署
        4. 静态文件收集
        5. 静态文件配置
    二、(单机部署)
        1. 服务器打包镜像
        2. 容器部署
        3. compose构建
    三、(多机部署)
        1. 镜像推送至docker-hub
        2. 多机一键部署
        
    ...负载均衡高可用

"""