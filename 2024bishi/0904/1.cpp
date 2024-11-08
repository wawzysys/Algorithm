#include <stdio.h>
#include <ctype.h>

int solution(const char *inbuf, char *outbuf)
{
    // 检查输入是否为 NULL
    if (inbuf == NULL || outbuf == NULL)
    {
        return -1;
    }

    while (*inbuf != '\0')
    {
        *outbuf = tolower((unsigned char)*inbuf); // 转换为小写字母
        inbuf++;
        outbuf++;
    }

    *outbuf = '\0';

    return 0; // 成功处理字符串
}

// 测试函数
int main()
{
    char output[100]; // 确保这个缓冲区足够大

    if (solution("Hello,World", output) == 0)
    {
        printf("Output: %s\n", output); // 应输出 "hello,world"
    }
    else
    {
        printf("Error: Invalid input\n");
    }

    if (solution(NULL, output) == -1)
    {
        printf("Error: Invalid input\n");
    }

    return 0;
}
