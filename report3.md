# 《Web 前端技术实训》第二次作业 文档

软件 03 陈启乾 2020012385

[TOC]

可以在 <https://github.com/ChenQiqian/campus-net/tree/hw3/> 查看本项目及文档。

## 效果及功能 GIF 演示

见 [展示GIF](doc/show.gif)，展示了：

展示了登录界面之后的折线图变化。


## 使用方法

> 本次作业已部署于 <http://net.cqqqwq.com>

### 本地部署

1. 安装依赖：

```
npm install
pip install -r requirements.txt
```

2. 编译静态文件

```
npm run build
```

3. 设置 Flask + Waitress 服务

```
python3 main.py
```

正常情况下，Waitress 服务应该使用 5000 端口。

### Docker 部署

构建镜像：

```bash
docker build campus-net .
```

运行容器：

```bash
docker run -dp 5000:5000 campus-net 
```

可以使用任意用户名及密码登录；登陆后在详情页面下方即可见到折线图。

## 实现说明

本文的实现调用了 [Chart.js](chartjs.org) 的 js 库实现，并且将其封装在了 Vue 的 Component 机制中。

在 LineChart 类中实现了对于 Chart.js 类中 line chart 的封装，并暴露出 data, weight, height 的三个接口。

在 Datacard 类中实现了对于 LineChart 类中表格数据的操控，亦即每两秒更新一次，生成一个随机数，加在目前的折线最后一个流量位置中。

## 遇到的问题及解决方法

### 数据更新

数据很难以进行直接的更新，需要兼顾 Vue 的 Reactive 功能和 Chart.js 的 Reactive 功能。

在 Github 上存在的若干 Vue 的 Cahrtjs 插件均不能使用，因为都会在我试图改变数据的时候卡死。

这里是因为，不能直接用 Vue 的响应式的设计直接绑定到 chartjs 的数据格式上，两侧均会对数据进行一层封装会导致在修改的时候出现死循环。因此必须在中间多垫一层；并且使用 vue 的 watch 特性连接两层。

