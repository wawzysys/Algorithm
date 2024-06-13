---
title: hexo
tags: hexo
cover: /img/cover/1.png
abbrlink: ab21860c
date: 2024-01-22 03:01:24
description: 配置博客
---
# 发表文章
```
hexo new "name"
```
这篇文章会出现在/source/_post/
# 发表page
```
hexo page "name"
```
# 修改完毕之后在本地查看效果
```
hexo clean
hexo generate
hexo cl && hexo g
hexo serve
```
# 上传
```
hexo d 
```
需要输入ssh密码


## 美化

### 彩色标签云
在`config.yal`中将`aside`中的`card_tags`的`enable`设置为`true`即可

### 用`giscus`实现评论

```
待整理
```
### 实现鼠标彩色
```
待整理
```
### 社交信息

```yaml
social:
  fab fa-github:  "填入github主页"|| Github || '#24292e'
  fas fa-envelope:  mailto:"邮箱" || Email || '#4a7dbe'
  fab fa-qq: fab fa-qq: tencent://AddContact/?fromId=45&fromSubId=1&subcmd=all&uin="QQ号👌"&website=www.oicqzone.com || QQ || '#qq-color-code'
```
### 背景图片and渐变
**⚠️：先在`config.butterfly.yaml`中将`backgroud`设一个图片 `url()`
网上都没有这一步 
但我试了好多次，只加个`css`不出现图片，不知道为什么**
```
background:  url(https://picx.zhimg.com/80/v2-7ee6f104979814d2bf420461e3872475_1440w.webp?source=1def8aca)
写css
然后inject
```
### 代码高亮
```
写css
然后inject
```

## 目前还不会的
### 2024.1.11
- [ ] `giscus`不会将评论顺序默认改成最新的
- [ ] 最新留言or评论不会弄到右边
- [x] 将评论在某些page不显示
- [x] 文章背景虚化   2024.1.22完成
### 待做
- [ ] `about`完善
  

### 图床
#### 用`picgo` app：
![](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240301205606.png)
从粘贴板上传图片快捷键：`ctrl+shift+p`

#### 用vscode + markdowm + picgo(插件)
![20240123001458](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240123001458.png)
`cdn`加速
![20240123001522](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240123001522.png)
从粘贴板上传图片快捷键：`artl+shift+u`

#### `Typora`

文件->偏好设置->图像

![](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240301205545.png)

![](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240301205518.png)

点击**验证图片上传选项**查看是否配置好





### git 子仓库：
```git
cd themes/butterfly
git add .
git commit -m "update"
cd ../../
git add themes/butterfly
git commit -m "update"
git push origin hexo
```
### 将ssh代理改为https
```
temp
```
### 可以单独将public上传到github仓库，不用`hexo d`
```
temp
```
### 副标题
在'_config.yaml'里面更改

```yaml
title: asdaso的blog
subtitle:
  enable: true

  sub:
    - 何其荣幸 何德何能
    - 所有的不平凡都来自平凡
description: 'cs'
keywords:
author: asdaso
language: zh-CN
timezone: ''

```

### 封面不显示正文

`method`选择1表示显示介绍

```
index_post_content:
  method: 1  #description
  length: 500 # if you set method to 2 or 3, the length need to config
```

