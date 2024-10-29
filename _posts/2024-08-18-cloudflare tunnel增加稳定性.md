---
layout: default
date: 2024-08-18
title: cloudflare tunnel增加稳定性
permalink: /2024/08/cloudflared.html
---





>如果没有前置软路由，即使使用了以下方法，cloudflared tunnel 在中国大陆使用的稳定性存在问题，并不建议在中国大陆使用

### 1.使用 http2
Cloudflared tunnel 默认使用QUIC(基于UDP),在国内使用会出现连接失败

#### 添加环境变量 

|key|value|
| ------------ | ------------ | 
|TUNNEL_TRANSPORT_PROTOCOL | http2 |

#### 或使用命令行

docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run  **--protocol http2** --token  XXX  

### 2.在一台设备上部署多个cloudflare tunnel ，以防失联


