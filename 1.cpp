#include <iostream>
#include <string>

// 函数trans用于转换字符串s，具体为反转字符串中单词的顺序并转换大小写
std::string trans(const std::string &s, int n)
{
    std::string res; // 存放结果字符串
    int index = 0;   // 用于记录单词插入的位置

    // 从字符串末尾向前遍历字符
    for (int i = n - 1; i >= 0; --i)
    {
        char ch = s[i];
        // 如果当前字符是空格，则在结果字符串中加入空格，并更新插入位置
        if (ch == ' ')
        {
            res += " ";
            index = res.size();
        }
        else
        {
            // 根据字符是大写还是小写进行转换，并插入到最近的单词起始位置
            if (ch >= 'A' && ch <= 'Z')
            {
                res.insert(index, 1, ch + 32); // 大写转小写并插入
            }
            else
            {
                res.insert(index, 1, ch - 32); // 小写转大写并插入
            }
        }
    }
    return res;
}

int main()
{
    std::string s;
    std::getline(std::cin, s);                 // 读取一行文本，包括空格
    std::string result = trans(s, s.length()); // 调用trans函数处理字符串
    std::cout << result << std::endl;          // 输出转换后的字符串
    return 0;
}
