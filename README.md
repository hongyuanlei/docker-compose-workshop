## Docker Compose

### Docker Compose 是什么？

> docker-compose 是用来定义和运行多个Docker容器应用的工具。

![docker和docker-compose](http://upload-images.jianshu.io/upload_images/1493507-8e1249c7e65b08fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 为什么要使用 Docker Compose?

Dockerfile**重现一个容器**，Compose**重现容器的配置**和**集群**。使用docker-compose, 你只需要使用一个YAML文件去配置你应用的服务. 然后，运行一个命令，你就可以根据你的配置去创建并启动所有的service。

![docker-compose up 启动所有服务](http://upload-images.jianshu.io/upload_images/1493507-8790a11209276554.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Docker Compose做了什么？

- 编排

**定义被部署的对象的各组成部分之间的耦合关系，部署流程中各个动作的执行顺序，部署过程所需要依赖文件和被部署文件的存储位置和获取方式，以及如何验证部署成功**。这些信息都会在编排工具中以指定的格式来要求运维人员自主定义并保存起来，从而保证这个流程能够随时在全新的环境中**有序的重现出来**。

- 部署

按照编排所指定的内容和流程，在目标机器上执行编排指定环境初始化，存放指定的依赖和文件，运行指定的部署动作，最终按照编排中的规则来确认部署成功。

### 乐队和指挥家

![乐队和指挥家](http://upload-images.jianshu.io/upload_images/1493507-c6bb6a70eae83690.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



- **编排是一个指挥家，他的大脑里存储了整个乐曲此起彼伏的演奏流程。**

- **部署就是整个乐队，他们严格按照指挥的意图用乐器来完成乐谱的执行。**

### 编排和部署组合

在Compose的世界里，编排和部署的组合结果，就是**一朵“容器云”**。

### 仅仅使用Compose，能构建自己的容器云吗？

答案是否定的。docker-compose**面向单主机部署**。docker-compose解决的问题局限在**“编排”**二字，甚至连**“部署”**范畴都涉足很少，而在一个能够服务于大众的云平台中，编排与部署也仅仅是其中的一个组成部分而已。

### 如何在Linux系统里安装docker-compose?

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


### 如何使用docker-compose?

- 编写你的应用的Dockerfile。
- 在docker-compose.yml中定义你的应用所依赖的所有服务，这样它们可以在一个隔离的环境中运行.
- 运行`docker-compose build & docker-compose up`来启动和运行你的整个应用.

### Docker Compose初体验（Wordpress应用实例）

- 使用docker-compose

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

- 使用docker cli启动

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

从表面上看，好像使用docker cli手动操作也是可以接受的，不外乎多打几行命令，不妨想象一下，如果管理上百个容器的场景该如何应付。

### Docker Compose进阶体验（HAProxy+Django+Redis应用实例）

![HAProxy+Django+Redis应用架构图](https://user-images.githubusercontent.com/7569085/40724543-de71221e-6453-11e8-8502-5404136ab11c.png)
