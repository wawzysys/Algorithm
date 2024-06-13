---
title: c++
abbrlink: 6f1ca842
date: 2024-04-19 20:11:37
tags:
---
## vector
```c++
vector<int> a(n);
// pair
vector<pair<int, int>> b;
b.push_back({1, 2});

// 遍历
for(const  auto& [a, b] : b){
    cout << a << " " << b << endl;
}
```
## 哈希表
```c++
map<int, int> mp = {
    {0, 1}, {4, 1}, {6, 1}, {9, 1}, {8, 2}
};
mp.find(digit) != mp.end()
map<int, PII> mp
for(auto &it : mp){
    cout << it.firtst << " " << it.second.first << " " << it.second.second << endl;
}
```
## readline
```c++
std::vector<T> input()
{
    std::vector<T> a;
    T s;
    while (std::cin >> s)
    {
        a.push_back(s);
        if (std::cin.get() != ' ')
            break;
    }
    return a;
}
//用法
vector<int> a = input<int>();
```
```c++
template <typename T>
vector<T> input()
{
    vector<T> list;
    string input;
    getline(cin, input);
    istringstream stream(input);
    int number;
    while (stream >> number)
    {
        list.push_back(number);
    }
    return list;
}
// 用法
vector<int> a = input<int>();
```