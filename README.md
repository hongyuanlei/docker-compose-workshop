# docker-compose-workshop


#### docker-compose 是什么？

> docker-compose 是用来定义和运行多个Docker容器应用的工具. 使用docker-compose, 你只需要使用一个YAML文件去配置你应用的服务. 然后，运行一个命令，你就可以根据你的配置去创建并启动所有的service。

#### 为什么要使用 docker-compose?

Docker重现一个容器，Compose重现容器的配置和集群。

#### 编排和部署

- 编排

**定义被部署的对象的各组成部分之间的耦合关系，部署流程中各个动作的执行顺序，部署过程所需要依赖文件和被部署文件的存储位置和获取方式，以及如何验证部署成功**。这些信息都会在编排工具中以指定的格式来要求运维人员自主定义并保存起来，从而保证这个流程能够随时在全新的环境中**有序的重现出来**。

- 部署

按照编排所指定的内容和流程，在目标机器上执行编排指定环境初始化，存放指定的依赖和文件，运行指定的部署动作，最终按照编排中的规则来确认部署成功。

所以：

编排是一个指挥家，他的大脑里存储了整个乐曲此起彼伏的演奏流程。

部署就是整个乐队，他们严格按照指挥的意图用乐器来完成乐谱的执行。

在Compose的世界里，编排和部署的组合结果，就是一朵“容器云”。


#### 如何使用docker-compose?

- Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
- Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
- Run docker-compose up and Compose starts and runs your entire app.


```
version: '3.3'

services:
   db:
     image: mysql:5.7
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
```

如果不使用docker-compose:

```
sudo docker run --name db \
			 -d \
			 --restart always \
			 -e MYSQL_ROOT_PASSWORD=somewordpress \
			 -e MYSQL_DATABASE=wordpress \
			 -e MYSQL_USER=wordpress \
			 -e MYSQL_PASSWORD=wordpress \
			 mysql:5.7

sudo docker run --name wordpress \
			 --restart always \
			 --link db \
			 -e WORDPRESS_DB_HOST=db:3306 \
			 -e WORDPRESS_DB_USER=wordpress \
			 -e WORDPRESS_DB_PASSWORD=wordpress \
			 -p 8000:80 \
			 wordpress:latest

```

#### Install Compose on Linux systems

- Run this command to download the latest version of Docker Compose:

```
$ sudo curl \
		-L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) \
		-o /usr/local/bin/docker-compose
```

- Apply executable permissions to the binary:

```
$ sudo chmod +x /usr/local/bin/docker-compose
```

- Test the installation

```
$ docker-compose --version
```
