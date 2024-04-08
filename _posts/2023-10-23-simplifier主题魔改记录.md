---
layout: default
date: 2023/10/23
title: simplifier主题魔改记录
permalink: /2023/10/simplifier.html
categories:
  - 技术
---

> 基于[simplifier 2020年版本](https://github.com/xiamuguizhi/simplifier "simplifier 2023年最新修改版本") 进行魔改

## 一，修改内容页图片大小
源代码默认图片是 width: 100%;再加上内容也是 width: 100%;，就等于图片占满整个宽度，显得特别丑

编辑主题文件 index.php
在 head标签内添加如下代码
```html
<style>
 /* 默认情况下，照片宽度为50% */
    img {
      width: 50%;
    }

    /* 在手机设备上，照片宽度为100% */
    @media only screen and (max-width: 600px) {
      img {
        width: 100%;
      }
    }
</style>
```
这样做的目的是为了在手机设备上，照片能够占满整个屏幕宽度，而在其他设备上保持一个较小的宽度。

## 二，修改内容区域大小
同上，内容区域占满整个宽度，当行数少时，比较丑

编辑主题文件 index.php
在 head标签内添加如下代码
```html
<style>
html{
      width: 80%;
    }

    
    @media only screen and (max-width: 600px) {
      html{
        width: 100%;
      }
    }
</style>
```
1.默认情况下，整个HTML文档的宽度为80%。
2.当屏幕宽度小于或等于600像素时（即手机设备），整个HTML文档的宽度变为100%。
这样做的目的是为了在手机设备上，整个HTML文档能够占满整个屏幕宽度，而在其他设备上保持一个较小的宽度。