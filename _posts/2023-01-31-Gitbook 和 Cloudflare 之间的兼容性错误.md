---
layout: default
date: 2023/01/31
title: Gitbook 和 Cloudflare 之间的兼容性错误
permalink: /2023/01/gitbook-cloudflare-error.html
categories:
  - 技术
---

![1697675972.png](https://hkcdn.yixiao.org/typecho/2023/10/19/1697675972.png?x-oss-process=style/sy)
之前使用 Gitbook 绑定自定义域名 read.yixiao.org 做了一篇文档，域名是托管在 Cloudflare 的，使用 CNAME 的方式接入 gitbook，后来不使用 gitbook，改变 CNAME 解析，解析到我自己的服务器，同时开启 Cloudflare 的 CDN，但是访问 read,yixiao.org 依然跳转到 gitbook，一开始我以为是因为 DNS 缓存，但是我等待了 24 个小时，依然如此。

 与[这个情况一样](https://community.cloudflare.com/t/dns-updates-issues-with-cloudflare-partners-like-gitbook/341449).




## 尝试解决
我想了很多办法，重置 DNS，删除 Cloudflare 缓存，但都无法解决
## 联系官方
我尝试联系 Cloudflare，但可惜我是 Free 套餐，无法发工单，所以我无法联系到 Cloudflare 官方

之后在 GitHub 上[联系了](https://github.com/GitbookIO/community/discussions/52) Gitbook 同时发邮件给 Gitbook，一天之后得到回复和解决。


## 解决方案

是 Gitbook 从 Cloudflare 中删除了我的域名，之后就可以了

###  以下为解释原文
>Sorry for the trouble. I just wanted to give some additional context on this specific issue as it has been a recurring problem that we are aware of but sadly cannot be easily resolved.
>
>TL;DR: To regain complete control of your custom hostname after it has been registered on app.gitbook.com, remove this custom hostname from our platform.
>
>For the longer explanation:
>We use Cloudflare to serve HTTPS traffic for all custom hostnames configured by our users.
>
>When a user configures a custom hostname, they point their DNS via CNAME to one of our domains (which, at the end of the chain points to Cloudflare). We then request Cloudflare (using their Cloudflare for SaaS product) to generate an SSL certificate for this hostname and serve the traffic properly.
>
>When users move away from GitBook, they often don't remove their content from GitBook and only change the DNS on their side. We don't request to remove the hostname from Cloudflare for SaaS until the content is deleted from GitBook, as the goal is to avoid breaking links for URLs that are still pointing to GitBook.
>
>We'd expect Cloudflare to always use the DNS setup of the domain as the primary factor for deciding where to route the traffic.
>
>We don't know the rationale behind why Cloudflare routing continues internally routing the traffic to GitBook when the domain is no longer pointing to the GitBook hostname. But it is not us doing that intentionally.



## 总结
这似乎是 Cloudflare 的问题，看[一些帖子](https://news.ycombinator.com/item?id=33715575)，官方计划去年 12 月解决该问题

>simon-cf(I work at Cloudflare):We are going to change the way this works so that the authoritative DNS dictates the behaviour, rather than the internal state where we currently require SSL for SaaS providers to manage off-boarding of their own customers. This work has been planned for some time and we're very pleased it will be done soon!
>
>Current ETA for this is December.


但是至少目前并没有解决，希望尽快解决，这给我带来了很大的困扰。。。。