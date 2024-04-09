---
layout: default
date: 2024/01/07 16:00:00
title: chatgpt-demo部署教程
permalink: /2024/01/chatgpt-demo.html
categories:
  - 技术
---

在去年3月时基于[@anse-app/chatgpt-demo](https://github.com/anse-app/chatgpt-demo "@anse-app/chatgpt-demo") 项目搭建了[chat.panyixiao.com](https://chat.panyixiao.com/ "chat.panyixiao.com"),非常稳定，非常易用，推荐用此项目搭建chatgpt给自己或家人使用

> 如果你不用改变项目的默认样式（比如在网站中加几个字之类），可以直接点击[Deploy with Vercel](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fddiu8081%2Fchatgpt-demo&env=OPENAI_API_KEY&envDescription=OpenAI%20API%20Key&envLink=https%3A%2F%2Fplatform.openai.com%2Faccount%2Fapi-keys)然后直接看第3步配置配置环境变量即可

1.Fork此项目 [@anse-app/chatgpt-demo](https://github.com/anse-app/chatgpt-demo "@anse-app/chatgpt-demo")

![1.png](https://hkcdn.yixiao.org/typecho/2024/01/07/1.png?x-oss-process=style/sy)

点击Fork,下一页全部默认 ，点击 **Create fork**



2.部署到 [Vercel](https://vercel.com/ "Vercel")

使用GitHub注册vercel
点击 Add New -Project

![1704634543.png](https://hkcdn.yixiao.org/typecho/2024/01/07/1704634543.png?x-oss-process=style/sy)

选择你 fork 完成的项目，点击Import

![1704634636.png](https://hkcdn.yixiao.org/typecho/2024/01/07/1704634636.png?x-oss-process=style/sy)

3.配置环境变量 Environment Variables
类似于这样

![1704634867.png](https://hkcdn.yixiao.org/typecho/2024/01/07/1704634867.png?x-oss-process=style/sy)

然后点击Deploy即可

| 名称 | 描述 | 默认 |
| --- | --- | --- |
| `OPENAI_API_KEY` | 你的 OpenAI API Key **必填**| `null` |
| `HTTPS_PROXY` | 为 OpenAI API 提供代理。e.g. `http://127.0.0.1:7890` | `null` |
| `OPENAI_API_BASE_URL` | 请求 OpenAI API 的自定义 Base URL. **如使用第三方api，则必填** | `https://api.openai.com` |
| `HEAD_SCRIPTS` | 在页面的 `</head>` 之前注入分析或其他脚本 | `null` |
| `PUBLIC_SECRET_KEY` | 项目的秘密字符串。用于生成 API 调用的签名 | `null` |
| `SITE_PASSWORD` | 为网站设置密码，支持使用英文逗号创建多个密码。如果未设置，则该网站将是公开的 | `null` |
| `OPENAI_API_MODEL` | 使用的 OpenAI 模型。[模型列表](https://platform.openai.com/docs/api-reference/models/list) | `gpt-3.5-turbo` |

4.对中国大陆用户的特别解释
由于OpenAi api在中国大陆较难付款，所以通常使用第三方api ，我所使用的是[api2d](https://api2d.com/ "api2d")，与原版的区别仅仅是需要替换OPENAI_API_BASE_URL 和OPENAI_API_KEY 这么简单

