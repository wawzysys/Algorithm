#include <bits/stdc++.h>
using namespace std;
#include <regex>

struct GraphicsCard
{
    string line; // 完整的输入行
    int num;     // 型号编号
    bool ti;     // 是否带有 "Ti"
    int freq;    // 频率
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<GraphicsCard> cards;
    string s;

    // 正则表达式匹配型号编号和 "Ti" 后缀
    regex model_regex(R"((\b[1-9]0[1-9]0\b)(?:\s+(Ti))?)");
    // 正则表达式匹配频率
    regex freq_regex(R"(@\s*(\d+)\s*MHz)");

    while (getline(cin, s))
    {
        GraphicsCard card;
        card.line = s;
        // 提取频率
        smatch freq_match;
        if (regex_search(s, freq_match, freq_regex))
        {
            card.freq = stoi(freq_match[1]);
        }
        else
        {
            card.freq = 0; // 无法解析频率时设为0
        }

        // 提取型号编号和 "Ti" 后缀
        smatch model_match;
        if (regex_search(s, model_match, model_regex))
        {
            card.num = stoi(model_match[1]);
            card.ti = model_match[2].matched;
        }
        else
        {
            card.num = -1; // 无法解析型号编号时设为-1
            card.ti = false;
        }

        cards.push_back(card);
    }

    // 确定最高性能的指标
    int max_num = -1;
    bool max_ti = false;
    int max_freq = -1;

    for (auto &card : cards)
    {
        if (card.num > max_num)
        {
            max_num = card.num;
            max_ti = card.ti;
            max_freq = card.freq;
        }
        else if (card.num == max_num)
        {
            if (card.ti && !max_ti)
            {
                max_ti = true;
                max_freq = card.freq;
            }
            else if (card.ti == max_ti)
            {
                if (card.freq > max_freq)
                {
                    max_freq = card.freq;
                }
            }
        }
    }

    // 输出所有符合最高性能标准的型号
    for (auto &card : cards)
    {
        if (card.num == max_num && card.ti == max_ti && card.freq == max_freq)
        {
            cout << card.line << "\n";
        }
    }
}
