#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_SIZE = 1e6 + 10;
using int64 = long long;
vector<int> graph[MAX_SIZE];
int weights[MAX_SIZE], positions[MAX_SIZE];

void depthFirstSearch(int node, int height)
{
    if (weights[node] <= height)
        return;
    weights[node] = height;
    for (int neighbor : graph[node])
        depthFirstSearch(neighbor, height);
}

signed main()
{
    // jingsaifeiyangyangtigong
    // 争取上省一
    std::ios::sync_with_stdio(false);
    std::cin.tie(0), std::cout.tie(0);
    int nodes, edges;
    cin >> nodes >> edges;
    for (int i = 1; i <= nodes; i++)
        cin >> weights[i];
    while (edges--)
    {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
    }
    iota(positions + 1, positions + nodes + 1, 1);
    sort(positions + 1, positions + nodes + 1, [&](int i, int j)
         { return weights[i] < weights[j]; });

    for (int i = 1; i <= nodes; i++)
    {
        int node = positions[i];
        for (int neighbor : graph[node])
            depthFirstSearch(neighbor, weights[node]);
    }
    int64 result = accumulate(weights + 1, weights + nodes + 1, (int64)0);
    cout << result << '\n';
    for (int i = 1; i <= nodes; i++)
        cout << weights[i] << " \n"[i == nodes];
    return 0;
}