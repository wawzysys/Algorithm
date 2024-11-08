#include<bits\stdc++.h>
using namespace std;
const int N = 1e2 + 5;
int g[N][N];
int vis[N][N];
int n;
int dx[4] = { 0, 1, 0, -1}; 
int dy[4] = { 1, 0, -1, 0};
typedef pair<int, int> pii;
queue<pii> q;
vector<int> splitToInt(const string& str, char delim) {
    vector<int> tokens;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delim)) {
        tokens.push_back(stoi(token));
    }
    return tokens;
}
int main(){
    cin >> n;
    string s;
    getline(cin, s);
    vector<int> a = splitToInt(s, ',');
}


