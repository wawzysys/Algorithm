#include <iostream>
#include <unordered_map>
#include <cmath>
using namespace std;
int count = 0;
unordered_map<int, int> memo;
int dfs(int n) {
    count += 1;
    // 检查记忆化存储中是否已有答案
    if (memo.find(n) != memo.end()) return memo[n];
    if (n == 0) return 0; // 基本情况

    int minCount = INT_MAX;
    for (int i = 1; i*i <= n; ++i) {
        minCount = min(minCount, dfs(n - i*i) + 1);
    }
    // 存储当前结果到记忆化存储中并返回
    memo[n] = minCount;
    return minCount;
}
int main() {
    int n = 20000; 
    cout << dfs(n) << endl;
    cout << count << endl;
    return 0;
}
