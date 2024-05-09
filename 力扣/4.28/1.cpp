#include <iostream>
#include <vector>
#include <string>
using namespace std;

void splitStr(string &str, vector<string> &ret, string &sep)
{
    // 寻找分隔字符串在原始字符串中的位置
    size_t pos = str.find(sep);
    if (pos == string::npos)
    {                       // 如果分隔字符串不存在于原始字符串中
        ret.push_back(str); // 将剩余的原始字符串添加到结果向量中
        return;
    }

    // 将分隔字符串之前的子串添加到结果向量中
    ret.push_back(str.substr(0, pos));

    // 截取原始字符串，继续处理剩余部分
    string nextStr = str.substr(pos + sep.length());
    if (!nextStr.empty())
    {
        splitStr(nextStr, ret, sep);
    }
}

int main()
{
    string str = "hello world, this is a test string.";
    vector<string> result;
    string sep = "e";

    splitStr(str, result, sep);

    // 输出分割后的字符串列表
    for (const auto &s : result)
    {
        cout << s << endl;
    }

    return 0;
}
