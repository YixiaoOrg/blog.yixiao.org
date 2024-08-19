---
layout: default
date: 2024-08-18
title: cloudflare tunnel增加稳定性
permalink: /2024/08/cloudflared.html
---



### 1.使用 http2
Cloudflared tunnel 默认使用QUIC(基于UDP),在国内使用会出现连接失败
添加环境变量 

|key|value|
| ------------ | ------------ | 
|TUNNEL_TRANSPORT_PROTOCOL | http2 |

### 2.在一台设备上部署多个cloudflare tunnel ，以防失联


