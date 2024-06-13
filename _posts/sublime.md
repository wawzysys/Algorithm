---
title: sublime
tags: sublime
abbrlink: 3e496c55
date: 2024-03-11 15:48:28
---
## 插件
![20240423173308](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240423173308.png)
![20240423173331](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240423173331.png)
## 快捷键
ctrl + b
ctrl + alt + b
ctrl + s
ctrl + n
## 主题
配色方案 
![20240311154302](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311154302.png)
主题
![20240423164843](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240423164843.png)
字体`Fira Cod`
首选项-设置-复制
![20240311154630](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311154630.png)
```
{
	"ignored_packages":
	[
	],
	"font_face": "Fira Code",
	/*"font_size": 12,*/
	"theme": "Seti Monokai.sublime-theme",
	"color_scheme": "Packages/Theme - Seti Monokai/scheme/Seti Monokai.tmTheme",
	"dark_color_scheme": "Monokai.sublime-color-scheme",
	"light_color_scheme": "Breakers.sublime-color-scheme",

	"sublime_merge_path": "D:\\Sublime Text\\Sublime Merge\\sublime_merge.exe",


"auto_complete": true,
"auto_mathch_enabled": false,
/*"color_scheme": "Packages/User/SublimeLinter/Monokai (SL).tmTheme",*/
/*"font_size": 12,*/
/*"ignored_packages":
[
"Vintage"
],*/
// "auto_complete_triggers": 
// [ 
// {"selector": "text.html", "characters": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.<",},
// {"selector": "text.plain", "characters": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.<",} 
// 	],

	"index_files": true,
	"font_size": 14,
}

```
## 编译系统
### python
```
{
    "cmd": ["E:/Anaconda/envs/test2/python.exe", "-u", "$file"],
    "selector": "source.python",
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "quiet": true
}
```
### java
需要手动更改class名字，目前结果方法没找到。写个模版改一下
```

```
## FastOlympicCoding
### 更改python解释器 
  更改的是`ctrl + alt + b`的解释环境
 * 可以看出下方的和右侧不一样，
 * 这是因为在Sublime Text的默认设置中，Ctrl + B通常用于触发当前激活的构建系统,是之前设置的'test2'
 * `ctrl + alt + b`是`FastOlympicCoding`运行的默认环境python。

![20240205175833](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205175833.png)
**这和本地的环境是一一对应的**
![20240205180443](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205180443.png)

* 1 先按照下图打开：
![20240205175324](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205175324.png)
* 2找到`python`
* 3把`"run_cmd": "python \"{source_file}\"`中的`python`改为自己想要的解释器路径，如下图
![20240205175358](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205175358.png)
更改完毕结果如下
![20240205180536](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240205180536.png)
  
### sublime 配置java环境
- 下载jdk和前文配置`vscode`
- 新建编译系统
工具-编译系统-新建编译系统-复制进去-保存为`java.sublime-build`
```
{
    "cmd": ["javac", "$file_name", "&&", "start","cmd", "/k", "java", "$file_base_name"],
    "shell": true,
    "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
    "working_dir": "$file_path",
    "selector": "source.java",
    "encoding": "GBK",
    "variants": [
        {
            "name": "Terminal",
            "cmd": ["javac", "$file_name", "&&", "start","cmd", "/k", "java", "$file_base_name"],
            "shell_cmd": "",
        },
        {
            "name": "Build",
            "quiet": true,
            "shell_cmd": "javac $file_name && java $file_base_name && del $file_base_name.class",
        }
    ]
}
```
### sublime添加代码模板记得空出class位置
工具-插件开发-新建代码片段-复制代码-保存为-"jm.sublime-snippet"
```
<snippet>
    <content><![CDATA[
//$TM_FILEPATH
import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;
public class ${1:} {
    public static Reader in;
    public static PrintWriter out;
    public static void main(String[] args) {
        out = new PrintWriter(new BufferedOutputStream(System.out));
        in = new Reader();
        int t = in.nextInt();
        while (t-- > 0)
            solve();
        out.close();
    }
    static void solve(){
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        char[][] c = new char[n][m];
        for (int i = 0; i < n; i++) {
            c[i] = in.nextLine().toCharArray();
        }
    }
 
    static class Reader {
        private BufferedReader br;
        private StringTokenizer st;
 
        Reader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
 
        boolean hasNext(){
            try {
                while (st == null || !st.hasMoreElements()) {
                    st = new StringTokenizer(br.readLine());
                }
            }catch (Exception e){
                return false;
            }
            return true;
        }
 
        String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            return st.nextToken();
        }
 
        int nextInt() {
            return Integer.parseInt(next());
        }
 
        int[] nextIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextInt();
            return arr;
        }
 
        long[] nextLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextLong();
            return arr;
        }
 
        long nextLong() {
            return Long.parseLong(next());
        }
 
        String nextLine() {
            String s = "";
            try {
                s = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return s;
        }
    }
}
]]></content>
    <tabTrigger>jp</tabTrigger>
</snippet>

```
输入`jp`(自己设置的)就可以出现代码模板
![20240311153911](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311153911.png)