---
layout: default
date: 2024/01/07 17:00:00
title: 修改chatgpt-demo的默认样式
permalink: /2024/01/chatgpt-demo-diy.html
categories:
  - 技术
---

[承接上文](https://blog.yixiao.org/2024/01/chatgpt-demo.html "承接上文")，此时你已经用Fork项目的方式搭建起了chatgpt-demo 

## 1.添加ICP备案号

修改chatgpt-demo/src/pages/index.astro 文件
把
```html
<Layout title="ChatGPT API Demo">
  <main >
    <Header />
    <Generator client:load />
    <Footer />
  </main>
</Layout>

```
改成
```html
<Layout title="Chat">
  <main >
    <Header />
    <Generator client:load />
    <Footer />
    <BackTop/>
  </main>
  <center>
  <p style="font-size:12px;position:fixed;left:0px;bottom:0px;width:100%;color:#d9d9d9;margin-bottom:10px;">
<a target="_blank" rel="nofollow" style="text-decoration:none" href="https://beian.miit.gov.cn/"> 苏ICP备2021005287号-1</a>
	</p>
	</center>
</Layout>
```
如密码页面也要修改也是同理
把 chatgpt-demo/src/pages/password.astro 中的
```html
<Layout title="Password Protection">
  <main class="h-screen col-fcc">
    <div class="op-30">Please input password</div>
    <div id="input_container" class="flex mt-4">
      <input id="password_input" type="password" class="gpt-password-input" />
      <div id="submit" class="gpt-password-submit">
        <div class="i-carbon-arrow-right" />
      </div>
    </div>
  </main>
</Layout>
```
改成
```html
<Layout title="Password">
  <main class="h-screen col-fcc">
    <div class="op-30">Please input password</div>
    <div id="input_container" class="flex mt-4">
      <input id="password_input" type="password" class="gpt-password-input" />
      <div id="submit" class="gpt-password-submit">
        <div class="i-carbon-arrow-right" />
      </div>
    </div>
  </main>
  
       <center>
  <p style="font-size:12px;position:fixed;left:0px;bottom:0px;width:100%;color:#d9d9d9;margin-bottom:10px;">
<a target="_blank" rel="nofollow" style="text-decoration:none" href="https://beian.miit.gov.cn/"> 苏ICP备2021005287号-1</a>
	</p>
	</center>
</Layout>
```
