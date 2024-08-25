// #include <iostream>
// #include <vector>
// #include <string>
// using namespace std;

// void simulate(const string &instructions, int pos, int current, vector<bool> &possible, int n)
// {
//     if (current >= instructions.length())
//     {
//         possible[pos] = true;
//         return;
//     }
//     char instruction = instructions[current];
//     if (instruction == 'L')
//     {
//         if (pos > 1)
//             pos--;
//     }
//     else if (instruction == 'R')
//     {
//         if (pos < n)
//             pos++;
//     }
//     else if (instruction == '?')
//     {
//         if (pos > 1)
//             simulate(instructions, pos - 1, current + 1, possible, n);
//         if (pos == 1)
//             simulate(instructions, pos, current + 1, possible, n);
//         if (pos < n)
//             simulate(instructions, pos + 1, current + 1, possible, n);
//         if (pos == n)
//             simulate(instructions, pos, current + 1, possible, n);
//         return;
//     }
//     simulate(instructions, pos, current + 1, possible, n);
// }

// int main()
// {
//     int n, k;
//     string instructions;
//     cin >> n >> k;
//     cin >> instructions;

//     vector<bool> possible(n + 1, false); // 使用 bool 数组来记录可能的终点位置
//     simulate(instructions, k, 0, possible, n);

//     for (int i = 1; i <= n; ++i)
//     {
//         cout << possible[i];
//     }
//     cout << endl;

//     return 0;
// }

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int n, k;
    string instructions;
    cin >> n >> k;
    cin >> instructions;

    vector<vector<bool>> dp(instructions.size() + 1, vector<bool>(n + 1, false));
    dp[0][k] = true;

    for (int i = 0; i < instructions.size(); ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (dp[i][j])
            {
                if (instructions[i] == 'L' && j > 1)
                {
                    dp[i + 1][j - 1] = true;
                }
                else if (instructions[i] == 'R' && j < n)
                {
                    dp[i + 1][j + 1] = true;
                }
                else if (instructions[i] == '?')
                {
                    if (j == 1)
                        dp[i + 1][j] = true;
                    if (j > 1)
                        dp[i + 1][j - 1] = true;
                    if (j < n)
                        dp[i + 1][j + 1] = true;
                    if (j == n)
                        dp[i + 1][j] = true;
                }
            }
        }
    }

    for (int j = 1; j <= n; ++j)
    {
        cout << (dp[instructions.size()][j] ? 1 : 0);
    }
    cout << endl;

    return 0;
}
