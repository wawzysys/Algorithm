小O有一个长度为 n 的数组 a。
他定义数组中的一个等腰直角三元组为一组三个下标(i,j,h)
满足:1<= i < j < k <= n
目ai = ak -aj + 1.
(例如数组[2,1,1,2] 中 (1,3,4) 
就是一个等腰直角三元组因为 1 < 3 < 4 日 a1=a4=a3+1)
现在他想知道，a 中有多少个等腰直角三元组，请你帮他算算吧。
输入描述第一行输入一个正整数 n(3 ≤n ≤2*10^5)表示数组a的长第二行输入n 个正整数 a1,a2,...,an(1 ≤ ai< 10^9),表度示数组 a 的元素。
输出：
在一行上输出一个整数，表示a中“等腰直角三元组”的个数。

输入：
5 
3 2 1 2 3
输出：
3
说明:
共有:
(1,2,5),(1,4,5),(2,3,4)这三个“等腰直角三元组
思路:
元素压缩：由于数组元素可能很大（1 ≤ a[i] < 10^9），我们首先对数组进行压缩，映射每个唯一元素到一个连续的索引。这有助于我们高效地统计频率。

频率统计：
使用一个数组 freq 来统计每个元素在数组中的总出现次数。
使用另一个数组 cnt 来统计当前遍历到位置 j 时，某个元素在 j 之前出现的次数。
遍历数组：
对于每个位置 j，计算 x = a[j] + 1。
查找 x 是否存在于数组中。如果存在，则:
cnt[x] 表示 x 在 j 之前出现的次数（即可能的 i）。
freq[x] 表示 x 在 j 之后出现的次数（即可能的 k）。
将 cnt[x] * freq[x] 加到答案中。
更新 cnt[a[j]] 和 freq[a[j]]

```cpp
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin>>n;
    vector<int> a(n);
    for(auto &x:a) cin>>x;
    // 压缩
    vector<int> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    // freq为后缀频率，cnt为前缀频率
    unordered_map<int, int> m;
    for(auto x:a) m[x]++;
    unordered_map<int, int> cnt;
    ll ans=0;
    for(int j=0;j<n;j++){
        int val = a[j];
        m[val]--; // 当前元素不在后缀中
        int x = val +1;
        if(m.find(x)!=m.end()){
            ll cb = cnt[x];
            ll cf = m[x];
            ans += cb * cf;
        }
        cnt[val]++;
    }
    cout<<ans;
}

```