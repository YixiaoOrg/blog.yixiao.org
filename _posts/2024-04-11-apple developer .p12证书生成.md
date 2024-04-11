---
layout: default
date: 2024/04/11
title: Apple Developer.p12与.mobileprovision生成
permalink: /2024/04/p12mobileprovision.html
categories:
  - 技术
---


>以下需要99$/year购买的iOS Developer Program 和一台运行Mac OS系统的电脑（虚拟机也可以）

 登录 [Apple Developer](https://developer.apple.com) 

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-15-44-02.png?x-oss-process=style/sy)

## 申请 App ID（标识符）
Apple Developer网站点击标识符

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-15-47-45.png?x-oss-process=style/sy)

点 `+` 号

依次选择 `App IDs` `App`

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-15-51-00.png?x-oss-process=style/sy)

按需填写后 两次点击 `Continue` 后即可完成申请

## 申请CSR文件
Mac打开钥匙串访问->证书助理->从证书颁发机构请求证书

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-08-00.jpg?x-oss-process=style/sy)

填入信息后选择存储到磁盘

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-12-35.png?x-oss-process=style/sy)

会生成 `CertificateSigningRequest.certSigningRequest` 文件

##  生成开发者证书 .p12

Apple Developer网站选择Certificates

点击`+`

选择`Apple Development`后 
下一步上传上一步生成的文件

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-18-18.png?x-oss-process=style/sy)

下一步下载`distribution.cer`文件

把`distribution.cer`拖入钥匙串访问 登录 我的证书 ，

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-23-45.png?x-oss-process=style/sy)

对证书右键选择导出，选择.p12作为输出文件格式，点击继续

设置p12文件的密码后即可保存

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-28-15.png?x-oss-process=style/sy)


## 添加设备 

Apple Developer网站点击`Devices` 点击`+`

![sy](https://hkcdn.yixiao.org/uPic/2024/04/11-16-34-03.png?x-oss-process=style/sy)


Device Name随便填写

UUID的获取教程，另行搜索，或使用 [蒲公英 | 一步快速获取 iOS 设备的UDID](https://www.pgyer.com/tools/udid)  获取

## 申请描述文件 .mobileprovision


Apple Developer网站点击`Profiles` 点击`+`

上面选择iOS App Development ，下面一般不用选

iOS App Development 选择刚刚生成的App ID

Offline support (7 day validity) 选择no

下一步选择 证书，选择设备，给证书命名后即可导出`.mobileprovision` 文件

