---
title: 第一个博客
cover: /img/333.jpg
tags:
  - 编程
  - 计算机科学
  - 技术
  - VSCODE
description: vscode的配置
abbrlink: 61585
date: 2024-01-19 23:56:08
---
## VSC换python内核
```
ctrl + shift + p
Select Interpreter
```
## 将mackdown转化为别的格式
```python
下载markdown pdf 插件
ctrl + shife + p 
输入 markdown pdf
```
## 解决markdown pdf 不能输出latex公式问题
在下面路径打开
```html
C://Users/<username>/.vscode/extensions/yzane.markdown-pdf-1.4.1/template/template.html
```
在最后的body和html之间输入
```
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
```
参考：
[VScode中Markdown PDF无法正确输出包含公式的pdf解决方案](https://blog.csdn.net/qq_18506419/article/details/103461825)

### 常用cmd命令
#### 删除.exe
```cmd
在文件下的cmd输入：
for /r %i in (*.exe) do del /q %i
```
~~~