---
title: vscode
tags: vscode - 环境
abbrlink: 849a3ae4
date: 2024-03-27 14:35:39
---
## VSC换python内核
```
ctrl + shift + p
Select Interpreter
```
## 将mackdown转化为别的格式
```
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

## 常用cmd命令
### 删除.exe
```cmd
在文件下的cmd输入：
for /r %i in (*.exe) do del /q %i
```
## 图床
### 快捷键
```
ctrl+alt+u
为什么token会消失？？？
![20240205173934](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205173934.png)
```
### vscode配置java
- 下载jdk，笔者下载的是jdk15.0.1
![20240311145620](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311145620.png)
下载完之后安装即可
- 环境变量配置
打开系统环境变量-点击环境变量-点击系统变量的path-编辑-新建，添加刚刚的安装目录的`bin`和`jre\bin`
![20240311145829](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311145829.png)
![20240311150012](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311150012.png)
![20240311150158](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311150158.png)
- 查看配置正确
`win+r`输入`cmd`,输入`java -version` 和 `javac -version`，如果出现下图所示配置正确
![20240311150420](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311150420.png)
- 下载vscode的java插件
- 编写程序
```java
// import java.util.*;
public class a {
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}
```
![20240311150528](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311150528.png)
- 可以在`.gitignore`中添加运行生成的`.class`文件
![20240311150747](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311150747.png)

### Fira Code

下载字体并安装
![20240325172523](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240325172523.png)
然后再设置中加入


![20240325165226](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240325165226.png)
开启连写
在设置中打开settings
![20240325165349](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240325165349.png)
更改`    "editor.fontLigatures": true,`为true
![20240325172538](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240325172538.png)


### 代码模板
vscode用户自建模板变量：
点击左下角设置齿轮
![20240327142401](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240327142401.png)
点击用户代码片段
![20240327142436](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240327142436.png)
可以选择新建和原有代码片段
提供一个示例
![20240327142541](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240327142541.png)
`prefix`后面是自己设置的快捷键唤起符
`description`是描述
```
TM_SELECTED_TEXT当前选定的文本或空字符串
TM_CURRENT_LINE当前行的内容
TM_CURRENT_WORD光标下单词的内容或空字符串
TM_LINE_INDEX基于零索引的行号
TM_LINE_NUMBER基于一个索引的行号
TM_FILENAME当前文档的文件名
TM_FILENAME_BASE不带扩展名的当前文档的文件名 （比如这里你在用户代码片段中写了${TM_FILENAME_BASE}，在自动生成的代码里就会在这个位置自动填充上你的文件的不含扩展名的文件名）
TM_DIRECTORY当前文档的目录
TM_FILEPATH当前文档的完整文件路径
RELATIVE_FILEPATH当前文档的相对（相对于打开的工作空间或文件夹）文件路径
CLIPBOARD剪贴板的内容
WORKSPACE_NAME打开的工作区或文件夹的名称
WORKSPACE_FOLDER打开的工作区或文件夹的路径
```
```
CURRENT_YEAR本年度
CURRENT_YEAR_SHORT本年度的最后两位数
CURRENT_MONTH以两位数字表示的月份（例如"02"）
CURRENT_MONTH_NAME月份的全名（例如"七月"）
CURRENT_MONTH_NAME_SHORT月份的短名称（例如"Jul"）
CURRENT_DATE以两位数字表示的月份中的某一天（例如"08"）
CURRENT_DAY_NAME日期的名称（例如"星期一"）
CURRENT_DAY_NAME_SHORT日期的短名称（例如"星期一"）
CURRENT_HOUR24 小时制格式的当前小时
CURRENT_MINUTE当前分钟为两位数
CURRENT_SECOND当前第二位为两位数
CURRENT_SECONDS_UNIX自 Unix 纪元以来的秒数
```
[自动转化为snippet网址](https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode)
```
https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode
```