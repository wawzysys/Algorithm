#include <bits/stdc++.h>
#include <vector>
using namespace std;
void solve() {
    int n;
    cin >> n;
    vector<string> stack;

    for (int i = 0; i < n; ++i) {
        string c;
        cin >> c;
        if (!stack.empty() && stack.size() > 1 && stack.back() == c && stack[stack.size() - 2] == c) {
            stack.pop_back();
            stack.pop_back();
        } else {
            stack.push_back(c);
        }
    }
    if(stack.size() == 0) cout << 0;
    else{
        for (int i = 0; i < stack.size(); ++i) {
            cout << stack[i] << " "[i != stack.size() - 1];
        }
    }
}
int main() {
    solve();
    return 0;
}
