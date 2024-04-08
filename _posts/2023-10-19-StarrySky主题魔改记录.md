---
layout: default
date: 2023/10/19
title: StarrySky主题魔改记录
permalink: /2023/10/StarrySky.html
categories:
  - 技术
---

> 基于[StarrySky1.0.2版本](https://github.com/mytinfeng/StarrySky "StarrySky1.0.2版本") 进行魔改

## 一：评论区头像服务改为Gravatar

functions.php 原文件 71行到91行
```php
/*解析QQ头像*/
function headportrait($obj){
        
    $reg='/^([1-9][0-9]{4,11})@qq.com$/';
    
    if(preg_match($reg,$obj)){
        
        $qq = preg_replace("/@qq.com/","",$obj);
        
        $qqavatar = file_get_contents('http://ptlogin2.qq.com/getface?appid=1006102&imgtype=3&uin='.$qq);
        
        $arrs = str_replace("pt.setHeader","qqavatarCallBack",$qqavatar);
        
        $arr=explode('"',$arrs);
        
        echo($arr[3]);
        
        
  
    }else{
        $rand = array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f');
        $color = $rand[rand(0,15)].$rand[rand(0,15)].$rand[rand(0,15)].$rand[rand(0,15)].$rand[rand(0,15)].$rand[rand(0,15)];
        echo "https://api.prodless.com/avatar.png?backgroundColor=".$color."&color=fff"; 

    }
    
}
```

其中api.prodless.com/avatar.png 服务无法正常使用，这样如果不是QQ邮箱，其他头像无法加载，为空白

需要进行如下修改，将评论区头像服务改为Gravatar
#### comments.php 36行
原代码
`background: url('<?php headportrait($comments->mail) ?>');`
改为
` background: url('<?php echo get_avatar($comments->mail) ?>');`

#### functions.php
任意位置添加
```php
 function get_avatar($mail, $size = 64) {
    $hash = md5(strtolower(trim($mail)));
    return "https://gravatar.loli.net/avatar/$hash?s=$size";
}
# gravatar.loli.net 为Gravatar的国内镜像，官方源为gravatar.com
```

