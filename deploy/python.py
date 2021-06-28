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