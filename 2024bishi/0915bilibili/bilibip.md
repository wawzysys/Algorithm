# 1
实现函数F(x,y)
x和y是字符串，F输出x是否是y的子序列判断:true或false，例如
F('ae','abcde')输出true
F('ea','abcde')输出false
子序列:原始字符串制除一些(也可以不删除)字符而不改变剩余字符相对位置形成的新字符串
示例 1
输入
```
"ae" "abcde"
```
输出
```
true
```
示例2
输入
```
"ea" "abcde"
```
输出
```
false
```

思路：双指针扫一遍
```c++
    bool f(string s, string t) {
        int i, j;
        for(i = 0, j = 0; i < s.size() && j < t.size(); ++j) {
            if(s[i] == t[j]) {
                ++i;
            }
        }
        return i == s.size();
    }

```

# 2
实现函数F(x)
x是一个由[]组成字符串，例如'][]]'
F(x)输出最长有效括号的长度，
例如F('][]]]'')输出2
F(']]')输出0
F('[][]')输出4
示例 1
输入
```
"][]]"
```
输出
```
2
```
示例 2
输入
```
"]]"
```

输出
```
0
```

## 思路：
首先我们初始化一个栈，但是这个栈是用来储存'('在字符数组中对应的索引。
其次我们设置一个数组flag[],只要是有效的括号，其中对应的字符s[i],则flag[i]=1.
我们接着开始遍历字符数组，每当遇到'('便将这个字符的索引压入栈中，再继续遍历字符数组
   当遇到')'时说明这个字符是与栈的顶端的'('配对的，于是将栈的顶端元素弹出。这两个相互匹配
   的字符的索引假如设为i和j,则flag[i]和flag[j]=1.
则我们最终只需要计算flag数组中连续的1的最大长度即可
```java
 int f(String s) {
      int n=s.ll();
      if(n==0) return 0;
      char[] array=new char[n];array=s.toCharArray();
      int[] flag=new int[n];int ans=0;
      Stack<Integer> temp=new Stack<>();
      for(int i=0;i<n;i++)
      {
         if(array[i]=='(')
          temp.push(i);
         else
          {
             if(temp.size()>0){
             int j=temp.pop();
             flag[i]=1;flag[j]=1;}
          }
      }
      int i=0;
      if(flag[i]==0){
        while(i<n&&flag[i]==0) i++;
                    }
      while(i<n)
        { if(flag[i]==1){
            int temp1=0;
            while(i<n&&flag[i]==1)
            {temp1++;i++;}
            ans=Math.max(temp1,ans);
                       }
         else i++;}
      return ans;
    }



```


# 3
实现函数F(x)
x是由0~9数字组成的字符串，例如'123"
F(x)需要判断x是否可以组成1个累加序列，输出这个累加序列

累加序列的定义:
1)至少有3个数字
2)从第3个数字开始，每个数字等于前两个数字的和
例如'12358'，可以组成累加序列1,2,3,5,8，函数输出[1,2.3.5,8]
例如'1202141'，可以组成累加序列1,20,21,41，函数输出[1,20,21,41]
示例 1
输入
"12358"
输出
[1.2.3.5,8]
1示例 2
输入
"1234"
输出
[]


## 思路：
本题思维需要思维一下，就是判断x字符串是否能用一个斐波那契数列组成。
切割生成两个初始数字，并生成斐波那契序列来匹配剩下的字符串部分。用python写可能好一些。
```python
def find_sequence(string):
    ll = len(string)
    max_l = ll - 2 
    for len_first in range(1, max_l + 1):
        if string[0] == '0' and len_first > 1:
            continue
        first_num_str = string[:len_first]
        first_num = int(first_num_str)
        max_len_second = ll - len_first - 1
        for len_second in range(1, max_len_second + 1):
            if string[len_first] == '0' and len_second > 1:
                continue
            second_num_str = string[len_first:len_first+len_second]
            second_num = int(second_num_str)
            num_sequence = [first_num, second_num]
            index = len_first + len_second
            while index < ll:
                next_num = first_num + second_num
                next_num_str = str(next_num)
                next_num_len = len(next_num_str)
                if index + next_num_len > ll or string[index:index+next_num_len] != next_num_str:
                    break
                num_sequence.append(next_num)
                index += next_num_len
                first_num, second_num = second_num, next_num
            if index == ll and len(num_sequence) >= 3:
                return num_sequence
    return []

```