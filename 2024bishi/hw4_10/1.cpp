#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;

int main() {
    int n, m;
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    std::cin >> n;
    std::vector<std::string> logs(n);
    std::cin.ignore();  // 忽略上一个输入后的换行符

    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, logs[i]);
    }

    std::cin >> m;
    std::map<std::string, int> ps;
    std::cin.ignore();

    for (int i = 0; i < m; ++i) {
        std::string factor;
        int p;
        std::getline(std::cin, factor, ',');
        std::cin >> p;
        std::cin.ignore();
        ps[factor] = p;
    }

    std::map<std::string, int> charges;
    std::set<std::tuple<std::string, std::string, std::string>> seen;

    for (auto& log : logs) {
        std::string t, cid, bf;
        int d;
        auto pos1 = log.find(',');
        auto pos2 = log.find(',', pos1 + 1);
        auto pos3 = log.find(',', pos2 + 1);

        t = log.substr(0, pos1);
        cid = log.substr(pos1 + 1, pos2 - pos1 - 1);
        bf = log.substr(pos2 + 1, pos3 - pos2 - 1);
        d = std::stoi(log.substr(pos3 + 1));

        if ((0 <= d && d <= 100) && seen.find({t, cid, bf}) == seen.end()) {
            seen.insert({t, cid, bf});
            charges[cid] += ps[bf] * d;
        }
    }

    for (auto& [cid, cost] : charges) {
        std::cout << cid << "," << cost << std::endl;
    }

    return 0;
}
