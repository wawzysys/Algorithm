#include <bits/stdc++.h>
using namespace std;
class LRUCache
{
public:
    LRUCache(int capacity) : capacity(capacity) {}

    void query(int key)
    {
        if (cacheMap.find(key) != cacheMap.end())
        {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        }
    }

    void insert(int key)
    {
        if (cacheMap.find(key) != cacheMap.end())
        {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        }
        else
        {
            if (cacheList.size() >= capacity)
            {
                int last = cacheList.back();
                cacheList.pop_back();
                cacheMap.erase(last);
            }
            cacheList.push_front(key);
            cacheMap[key] = cacheList.begin();
        }
    }

    void remove(int key)
    {
        if (cacheMap.find(key) != cacheMap.end())
        {
            cacheList.erase(cacheMap[key]);
            cacheMap.erase(key);
        }
    }

    vector<int> getCacheKeys()
    {
        vector<int> keys(cacheList.begin(), cacheList.end());
        sort(keys.begin(), keys.end());
        return keys;
    }

private:
    int capacity;
    list<int> cacheList;
    unordered_map<int, list<int>::iterator> cacheMap;
};
vector<int> lru_cache_operations(int capacity, const vector<string> &operations)
{
    LRUCache lru_cache(capacity);
    for (const auto &op : operations)
    {
        char action = op[0];
        int key = stoi(op.substr(2));
        if (action == 'Q')
        {
            lru_cache.query(key);
        }
        else if (action == 'A')
        {
            lru_cache.insert(key);
        }
        else if (action == 'D')
        {
            lru_cache.remove(key);
        }
    }
    return lru_cache.getCacheKeys();
}
int main()
{
    int c, m;
    cin >> c >> m;
    cin.ignore();

    vector<string> operations(m);
    for (int i = 0; i < m; ++i)
    {
        getline(cin, operations[i]);
    }
    vector<int> result = lru_cache_operations(c, operations);
    for (size_t i = 0; i < result.size() - 1; ++i)
    {
        cout << result[i] << " ";
    }
    cout << result[result.size() - 1];

    return 0;
}
