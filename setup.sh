#!/bin/bash

echo "系统部署测试平台安装中..."

echo "安装docker"
if ! type docker >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo apt-key fingerprint 0EBFCD88
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    sudo systemctl enable docker
    sudo systemctl start docker

    if ! type docker >/dev/null 2>&1; then
        echo "docker安装失败，请根据报错内容手动安装成功后在执行安装脚本."
        exit
    else
        echo "docker安装成功."
    fi
else
    echo "docker已安装"
fi

echo "安装docker-compose"
if ! type docker-compose >/dev/null 2>&1; then
    sudo curl -L https://github.com/docker/compose/releases/download/1.23.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version
    docker-compose up -d
    if ! type docker >/dev/null 2>&1; then
        echo "docker-compose安装失败，请根据报错内容手动安装成功后在执行安装脚本."
        exit
    else
        echo "docker-compose安装成功."
    fi
else
    echo "docker-compose已安装"
fi

echo "系统安装完毕!"

echo "初始化配置参数"

if type docker-compose >/dev/null 2>&1; then
    echo "初始化配置完成, 服务重启中."

    if ! type docker-compose restart >/dev/null 2>&1; then
      echo "服务重启中"
      docker-compose up -d
    else
      echo ""
    fi

else
    echo "docker-compose未安装, 请重新进行安装"
fi

echo "-----------------------------------------------------------------------------------------------"
echo "执行 docker-compose ps 查看各个容器状态"
echo "执行 docker-compose down -v 删除各个容器"
echo "执行 docker-compose up -d 各个容器初始化"
echo "执行 docker-compose logs -f 服务名称 查看各个容器实时日志"
echo "执行 docker-compose exec -it 服务名称 进入容器"
echo "执行 docker-compose restart 重启所有容器"
echo "-----------------------------------------------------------------------------------------------"
