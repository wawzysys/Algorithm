---
title: java1
abbrlink: eb7e46a9
date: 2024-03-09 15:58:16
tags: java
---
## 环境配置
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
![20240311153902](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240311153902.png)

## 数据结构常用
### 邻接表
```java
        List<int[]>[] g = new ArrayList[N]; // 邻接表
        Arrays.setAll(g, i -> new ArrayList<>());
```
**List<int[]>[]:**
- 这是一个数组，每个元素都是可以存储整数数组(int[])的list。
- 数组的大小在初始化时固定，并且在其生命周期中不能更改。
- 这种结构允许通过索引直接访问列表，访问时间为O(1)。
### 数组初始化
```java
        int[] dist = new int[n + 5];
        Arrays.fill(dist, Integer.MAX_VALUE );
```
### 双端队列
```java
        Deque<Integer> q = new LinkedList<>();
```
### 快读
```java


    public static Reader in;
    public static void mian(String[] args){
        in = new Reader();
    }
    static class Reader {
        private final BufferedReader br;
        private StringTokenizer st;

        Reader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        boolean hasNext() {
            try {
                while (st == null || !st.hasMoreElements()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (Exception e) {
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
```
### 
```java
private final Set<Integer> s = new HashSet<>();
s.add(val);

s.contains(val);
```
## List
List: List是一个接口，它定义了一个可以按顺序访问的元素集合的基本操作和方法。List是Java集合框架的一部分，它提供了一种方式来存储有序的元素集合。List是一个接口，所以你不能直接实例化一个List。

ArrayList: ArrayList是List接口的一个具体实现。它使用数组的结构来存储元素，这使得元素的随机访问变得非常快。但是，添加或删除元素（尤其是列表的前部）可能比在LinkedList中慢，因为这可能需要移动数组中的其他元素。ArrayList提供了List接口的所有标准操作，并且还添加了一些其他的功能，如确保容量和增加容量。
```java
List<List<Integer>> rooms = new ArrayList<>();
下标从0开始，访问x下标的元素。
rooms.get(x)
```
### ArrayList
`ArrayList`是`Java`中最常用的集合之一，提供了一系列功能来处理动态数组。

```java
// 访问元素
List<Integer> l = new ArrayList<>();
l.get(int index);

for(Integer num : list){

}
//大小
size()
//判空
isEmpty()
//搜索
contains(Object o) //检查列表中是否存在指定的元素。
indexOf(Object o) //返回列表中指定元素的第一个出现的索引，如果列表不包含该元素，则返回-1。
lastIndexOf(Object o) //返回列表中指定元素的最后一个出现的索引，如果列表不包含该元素，则返回-1。
//范围
subList(int l, int r) // 返回一个指定范围的新列表，不会改变原有列表
```
```java
//转换
toArray() //将列表转换为一个数组
```
批量操作
```java
clear() // 移除列表中的所有元素。
```
排序
```java
people.sort((p1, p2) -> p1.age - p2.age);
按照年龄升序
```