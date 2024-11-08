#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <set>

using namespace std;

class UnionFind
{
public:
    vector<int> parent;
    UnionFind(int n) : parent(n)
    {
        for (int i = 0; i < n; ++i)
        {
            parent[i] = i;
        }
    }

    int find(int x)
    {
        if (x != parent[x])
        {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY)
        {
            parent[rootY] = rootX;
        }
    }
};

vector<int> splitToInt(const string &str, char delim)
{
    vector<int> tokens;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delim))
    {
        tokens.push_back(stoi(token));
    }
    return tokens;
}

int getResult(int n, vector<int> &confirmed, vector<vector<int>> &matrix)
{
    UnionFind ufs(n);

    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (matrix[i][j] == 1)
            {
                ufs.unionSets(i, j);
            }
        }
    }

    vector<int> cnts(n, 0);
    for (int i = 0; i < n; i++)
    {
        int fa = ufs.find(i);
        cnts[fa]++;
    }

    set<int> confirmed_fa;
    int ans = 0;
    for (int i : confirmed)
    {
        int fa = ufs.find(i);
        if (!confirmed_fa.insert(fa).second)
            continue;
        ans += cnts[fa];
    }

    return ans - confirmed.size();
}

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    string line;
    getline(cin, line);
    vector<int> confirmed = splitToInt(line, ',');

    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
        getline(cin, line);
        matrix[i] = splitToInt(line, ',');
    }

    cout << getResult(n, confirmed, matrix) << endl;
    return 0;
}
